import copy
import sys

if sys.version_info.major < 3:
    from httplib import responses
    from urlparse import urlsplit
else:
    from http.client import responses
    from urllib.parse import urlsplit

import requests

from .zdesk_api import ZendeskAPI


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
        # Set attributes necessary for API
        self._zdesk_url = None
        self._zdesk_email = None
        self._zdesk_password = None
        self._zdesk_token = False

        self.client = requests.Session()

        self.zdesk_url = zdesk_url.rstrip('/')
        self.zdesk_email = zdesk_email
        self.zdesk_password = zdesk_password
        self.zdesk_token = zdesk_token

        # Set headers
        self.client_args = copy.deepcopy(client_args) or {}
        self.headers = copy.deepcopy(headers) or {}

        if api_version != 2:
            raise ValueError("Unsupported Zendesk API Version: %d" %
                             api_version)

    def _update_auth(self):
        if self.zdesk_email and self.zdesk_password:
            self.client.auth = (self.zdesk_email, self.zdesk_password)
        else:
            self.client.auth = None

    @property
    def zdesk_url(self):
        return self._zdesk_url

    @zdesk_url.setter
    def zdesk_url(self, value):
        self._zdesk_url = value

    @zdesk_url.deleter
    def zdesk_url(self):
        self._zdesk_url = None

    @property
    def zdesk_email(self):
        if self.zdesk_token:
            return self._zdesk_email + '/token'
        else:
            return self._zdesk_email

    @zdesk_email.setter
    def zdesk_email(self, value):
        self._zdesk_email = value
        self._update_auth()

    @zdesk_email.deleter
    def zdesk_email(self):
        self._zdesk_email = None
        self._update_auth()

    @property
    def zdesk_password(self):
        return self._zdesk_password

    @zdesk_password.setter
    def zdesk_password(self, value):
        self._zdesk_password = value
        self._update_auth()

    @zdesk_password.deleter
    def zdesk_password(self):
        self._zdesk_password = None
        self._update_auth()

    @property
    def zdesk_token(self):
        return self._zdesk_token

    @zdesk_token.setter
    def zdesk_token(self, value):
        self._zdesk_token = bool(value)
        self._update_auth()

    @zdesk_token.deleter
    def zdesk_token(self):
        self._zdesk_token = False
        self._update_auth()

    def call(self, path, query=None, method='GET', data=None,
             files=None, get_all_pages=False, complete_response=False,
             **kwargs):
        """Make a REST call to the Zendesk web service.

        Parameters:
        path - Path portion of the Zendesk REST endpoint URL.
        query - Query parameters in dict form.
        method - HTTP method to use in making the request.
        data - POST data or multi-part form data to include.
        files - Requests style dict of files for multi-part file uploads.
        get_all_pages - Make multiple requests and follow next_page.
        complete_response - Return raw request results.
        """

        # Support specifying a mime-type other than application/json
        mime_type = kwargs.pop('mime_type', 'application/json')

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

        if files:
            # Sending multipart file. data contains parameters.
            json = None
            self.headers.pop('Content-Type', None)
        elif (mime_type == 'application/json' and
                (method == 'POST' or method == 'PUT')):
            # Sending JSON data.
            json = data
            data = {}
            self.headers.pop('Content-Type', None)
        elif (mime_type != 'application/json' and
                (method == 'POST' or method == 'PUT')):
            # Uploading an attachment, probably.
            # Specifying the MIME type is required.
            json = None
            self.headers['Content-Type'] = mime_type
        else:
            # Probably a GET or DELETE. Not sending JSON or files.
            json = None
            self.headers.pop('Content-Type', None)

        results = []
        all_requests_complete = False

        while not all_requests_complete:
            # Make an http request
            response = self.client.request(method,
                                           url,
                                           params=kwargs,
                                           json=json,
                                           data=data,
                                           headers=self.headers,
                                           files=files,
                                           **self.client_args)

            # If the response status is not in the 200 range then assume an
            # error and raise proper exception

            if response.status_code < 200 or response.status_code > 299:
                if response.status_code == 401:
                    raise AuthenticationError(
                        response.content, response.status_code, response)
                elif response.status_code == 429:
                    # FYI: Check the Retry-After header for how
                    # many seconds to sleep
                    raise RateLimitError(
                        response.content, response.status_code, response)
                else:
                    raise ZendeskError(
                        response.content, response.status_code, response)

            if response.content.strip():
                content = response.json()

                # set url to the next page if that was returned in the response
                url = content.get('next_page', None)
            else:
                content = response.content
                url = None

            if complete_response:
                results.append({
                    'response': response,
                    'content': content,
                    'status': response.status_code
                })

            else:
                # Deserialize json content if content exists.
                # In some cases Zendesk returns ' ' strings.
                # Also return false non strings (0, [], (), {})
                if response.headers.get('location'):
                    # Zendesk's response is sometimes the url of a newly
                    # created user/ticket/group/etc and they pass this through
                    # 'location'.  Otherwise, the body of 'content'
                    # has our response.
                    results.append(response.headers.get('location'))
                elif content:
                    results.append(content)
                else:
                    results.append(responses[response.status_code])

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
                # the end result is a response that looks like one giant call,
                # to e.g. list tickets, but was actually made by multiple API
                # calls.
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
