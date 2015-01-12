import sys
import re
import base64
import pkg_resources

if sys.version < '3':
    from httplib import responses
    from urllib import urlencode
    from urlparse import urlsplit
else:
    from http.client import responses
    from urllib.parse import urlencode, urlsplit


import httplib2
import simplejson as json

from .zdesk_api import ZendeskAPI

common_params = [
        'page',
        'per_page',
        'sort_by',
        'sort_order',
    ]


def get_id_from_url(url):
    url_id = urlsplit(url).path.split('/')[-1].split('.')[0]
    if url_id.isdigit():
        return url_id
    else:
        return None


class ZendeskError(Exception):
    def __init__(self, msg, code, response):
        self.msg = msg
        self.error_code = code
        self.response = response

    def __str__(self):
        return repr('%s: %s %s' % (self.error_code, self.msg, self.response))


class AuthenticationError(ZendeskError):
    pass


class RateLimitError(ZendeskError):
    pass


class Zendesk(ZendeskAPI):
    """ Python API Wrapper for Zendesk"""


    def __init__(self, zdesk_url, zdesk_email=None, zdesk_password=None,
                 zdesk_token=False, headers=None, client_args=None,
                 api_version=2):
        """
        Instantiates an instance of Zendesk. Takes optional parameters for
        HTTP Basic Authentication

        Parameters:
        zdesk_url - https://company.zendesk.com (use http if not SSL enabled)
        zdesk_email - Specific to your Zendesk account (typically email)
        zdesk_password - Specific to your Zendesk account or your account's
            API token if zdesk_token is True
        zdesk_token - use api token for authentication instead of user's
            actual password
        headers - Pass headers in dict form. This will override default.
        client_args - Pass arguments to http client in dict form.
            {'cache': False, 'timeout': 2}
            or a common one is to disable SSL certficate validation
            {"disable_ssl_certificate_validation": True}
        """
        if not client_args: client_args = {}

        # Set attributes necessary for API
        self.zdesk_url = zdesk_url.rstrip('/')
        self.zdesk_email = zdesk_email
        if zdesk_token:
            self.zdesk_email += "/token"
        self.zdesk_password = zdesk_password

        # Set headers
        self.headers = headers
        if self.headers is None:
            version = pkg_resources.require("zdesk")[0].version
            self.headers = {
                'User-agent': 'Zdesk Python Library v%s' % version,
                'Content-Type': 'application/json'
            }

        # Set http client and authentication
        self.client = httplib2.Http(**client_args)
        if (self.zdesk_email is not None and
                self.zdesk_password is not None):
            self.client.add_credentials(
                self.zdesk_email,
                self.zdesk_password
            )

        if api_version != 2:
            raise ValueError("Unsupported Zendesk API Version: %d" %
                             api_version)

    def call(self, path, query=None, method='GET', status=200, data=None, **kwargs):
        """
        Should probably url-encode GET query parameters on replacement
        """

        # If requested, return all response information
        complete_response = kwargs.pop('complete_response', False)

        # If requested, exhaustively obtain and consolidate requests that
        # contain a next_page attribute
        get_all_pages = kwargs.pop('get_all_pages', False)

        # Support specifying a mime-type other than application/json
        mime_type = kwargs.pop('mime_type', 'application/json')

        # Validate remaining kwargs against valid_params and add
        # params url encoded to url variable.
        for kw in kwargs:
            if kw not in common_params:
                raise TypeError("call to %s got an unexpected keyword argument "
                                "'%s'" % (path, kw))

        for key in kwargs.keys():
            value = kwargs[key]
            if hasattr(value, '__iter__') and not isinstance(value, str):
                kwargs[key] = ','.join(map(str, value))

        if query:
            if kwargs:
                kwargs.update(query)
            else:
                kwargs = query

        url = self.zdesk_url + path

        if kwargs:
            url += '?' + urlencode(kwargs)

        # If credentials are supplied, then always put them in the headers
        if self.zdesk_email and self.zdesk_password:
            auth = base64.b64encode(self.zdesk_email.encode('ascii') + b':' +
                             self.zdesk_password.encode('ascii'))
            self.headers["Authorization"] = "Basic {}".format(
                                                        auth.decode('ascii'))
        elif "Authorization" in self.headers:
            del(self.headers["Authorization"])

        if mime_type == "application/json":
            body = json.dumps(data)
            self.headers["Content-Type"] = "application/json"
        else:
            body = data
            self.headers["Content-Type"] = mime_type

        results = []
        all_requests_complete = False

        while not all_requests_complete:
            # Make an http request
            response, content = self.client.request(
                                    url,
                                    method,
                                    body=body,
                                    headers=self.headers
                                )

            # If the response status is different from status given, then we
            # assume an error and raise proper exception

            response_status = int(response.get('status', 0))

            if response_status != status:
                if response_status == 401:
                    raise AuthenticationError(content, response_status, response)
                elif response_status == 429:
                    # FYI: Check the Retry-After header for how many seconds to sleep
                    raise RateLimitError(content, response_status, response)
                else:
                    raise ZendeskError(content, response_status, response)

            if content.strip():
                content = json.loads(content)

                # set url to the next page if that was returned in the response
                url = content.get('next_page', None)
            else:
                url = None

            if complete_response:
                results.append({
                    'response': response,
                    'content': content,
                    'status': status
                })

            else:
                # Deserialize json content if content exists. In some cases Zendesk
                # returns ' ' strings. Also return false non strings (0, [], (), {})
                if response.get('location'):
                    # Zendesk's response is sometimes the url of a newly created user/
                    # ticket/group/etc and they pass this through 'location'.  Otherwise,
                    # the body of 'content' has our response.
                    results.append(response.get('location'))
                elif content:
                    results.append(content)
                else:
                    results.append(responses[response_status])

            # if there is a next_page, and we are getting pages, then continue
            # making requests
            all_requests_complete = not (get_all_pages and url)

        if get_all_pages and complete_response:
            # Return the list of results from all calls made.
            # This way even if only one page was present the caller will
            # always receive back an iterable value, since multiple pages
            # were requested/expected. This also provides the information for
            # every call, and saves us from having to try to combine all of
            # that ourselves in a sensible way.
            return results

        if len(results) == 1:
            # regardless as to whether all pages were requested, there was
            # only one call and set of results, so just send it back.
            return results[0]

        # Now we need to try to combine or reduce the results:

        hashable = True
        try:
            if len(set(results)) == 1:
                # all responses were the same, so return just the first one.
                # may have a list of locations or response statuses
                return results[0]
        except TypeError:
            # probably we have a list of content dictionaries.
            hashable = False

        if hashable:
            # we have a list of simple objects like strings, but they are not
            # all the same so send them all back.
            return results

        # may have a sequence of response contents
        # (dicts, possibly lists in the future as that is valid json also)
        combined_dict_results = {}
        combined_list_results = []
        for result in results:
            if isinstance(result, list):
                # the result of this call returned a list.
                # extend the combined list with these results.
                combined_list_results.extend(result)
            elif isinstance(result, dict):
                # the result of this call returned a dict. the dict probably
                # has both simple attributes (strings) and complex attributes
                # (lists). if the attribute is a list, we will extend the
                # combined attribute, otherwise we will just take the last
                # attribute value from the last call.
                # the end result is a response that looks like one giant call, to
                # e.g. list tickets, but was actually made by multiple API calls.
                for k in result.keys():
                    v = result[k]
                    if isinstance(v, list):
                        try:
                            combined_dict_results[k].extend(v)
                        except KeyError:
                            combined_dict_results[k] = v
                    else:
                        combined_dict_results[k] = v
            else:
                # returned result is not a dict or a list. don't know how to
                # deal with this, so just send everything back.
                return results

        if combined_list_results and combined_dict_results:
            # there was a mix of list and dict results from the sequence
            # of calls. this case seems very odd to me if it ever happens.
            # at any rate, send everything back uncombined
            return results

        if combined_dict_results:
            return combined_dict_results

        if combined_list_results:
            return combined_list_results

        # I don't expect to make it here, but I suppose it could happen if,
        # perhaps, a sequence of empty dicts were returned or some such.
        # Send everything back.
        return results

