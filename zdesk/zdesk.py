import collections
import copy
import inspect
import sys
import time

import requests
import six

if six.PY2:
    from httplib import responses
    from urlparse import urlsplit
else:
    from http.client import responses
    from urllib.parse import urlsplit

from .zdesk_api import ZendeskAPI


def batch(sequence, callback, size=100, **kwargs):
    """Helper to setup batch requests.

    There are endpoints which support updating multiple resources at once,
    but they are often limited to 100 updates per request.
    This function helps with splitting bigger requests into sequence of
    smaller ones.

    Example:
        def add_organization_tag(organizations, tag):
            request = {'organizations': [
                {
                    'id': org['id'],
                    'tags': org['tags'] + [tag],
                } for org in organizations
            ]}
            job = z.organizations_update_many(request)['job_status']
            return job['id']

        # z = Zendesk(...)
        orgs = z.organizations_list(get_all_pages=True)['organizations']
        job_ids = [job for job in
                   batch(orgs, add_organization_tag, tag='new_tag')]

    Parameters:
        sequence - any sequence you want to split
        callback - function to call with slices of sequence,
            its return value is yielded on each slice
        size - size of chunks, combined with length of sequence determines
            how many times callback is called (defaults to 100)
        **kwargs - any additional keyword arguments are passed to callback
    """
    batch_len, rem = divmod(len(sequence), size)
    if rem > 0:
        batch_len += 1
    for i in range(batch_len):
        offset = i * size
        yield callback(sequence[offset:offset + size], **kwargs)


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

ACCEPT_RETRIES = ZendeskError, requests.RequestException


class Zendesk(ZendeskAPI):
    """ Python API Wrapper for Zendesk"""

    def __init__(self, zdesk_url, zdesk_email=None, zdesk_password=None,
                 zdesk_token=False, headers=None, client_args=None,
                 api_version=2, retry_on=None, max_retries=0):
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
            {'allow_redirects': False, 'timeout': 2}
            or a common one is to disable SSL certficate validation
            {'verify': False}
        retry_on - Specify any exceptions from ACCEPT_RETRIES or non-2xx
            HTTP codes on which you want to retry request.
            Note that calling Zendesk.call with get_all_pages=True can make
            up to (max_retries + 1) * pages.
            Defaults to empty set, but can be any iterable, exception or int,
            which will become set with same values you provided.
        max_retries - How many additional connections to make when
            first one fails. No effect when retry_on evaluates to False.
            Defaults to 0.
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

        self._retry_on = {}
        self._max_retries = 0
        self.retry_on = retry_on
        self.max_retries = max_retries

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

    @property
    def retry_on(self):
        return self._retry_on

    @retry_on.setter
    def retry_on(self, value):
        if value is None:
            self._retry_on = set()
            return

        def _validate(v):
            exc = ("retry_on must contain only non-2xx HTTP codes"
                   "or members of %s" % (ACCEPT_RETRIES, ))

            if inspect.isclass(v):
                if not issubclass(v, ACCEPT_RETRIES):
                    raise ValueError(exc)
            elif isinstance(v, int):
                if 200 <= v < 300:
                    raise ValueError(exc)
            else:
                raise ValueError(exc)

        if isinstance(value, collections.Iterable):
            for v in value:
                _validate(v)
            self._retry_on = set(value)
        else:
            _validate(value)
            self._retry_on = set([value])

    @retry_on.deleter
    def retry_on(self):
        self._retry_on = set()

    @property
    def max_retries(self):
        return self._max_retries

    @max_retries.setter
    def max_retries(self, value):
        try:
            value = int(value)
            if value < 0:
                raise ValueError
        except (TypeError, ValueError):
            raise ValueError("max_retries must be non-negative integer")

        self._max_retries = value

    @max_retries.deleter
    def max_retries(self):
        self._max_retries = 0

    def call(self, path, query=None, method='GET', data=None,
             files=None, get_all_pages=False, complete_response=False,
             retry_on=None, max_retries=0, **kwargs):
        """Make a REST call to the Zendesk web service.

        Parameters:
        path - Path portion of the Zendesk REST endpoint URL.
        query - Query parameters in dict form.
        method - HTTP method to use in making the request.
        data - POST data or multi-part form data to include.
        files - Requests style dict of files for multi-part file uploads.
        get_all_pages - Make multiple requests and follow next_page.
        complete_response - Return raw request results.
        retry_on - Specify any exceptions from ACCEPT_RETRIES or non-2xx
            HTTP codes on which you want to retry request.
            Note that calling Zendesk.call with get_all_pages=True can make
            up to (max_retries + 1) * pages.
            Defaults to empty set, but can be any iterable, exception or int,
            which will become set with same values you provided.
        max_retries - How many additional connections to make when
            first one fails. No effect when retry_on evaluates to False.
            Defaults to 0.
        """

        # Rather obscure way to support retry_on per single API call
        if retry_on and max_retries:
            try:
                _retry_on = self._retry_on
                _max_retries = self._max_retries

                self.retry_on = retry_on
                self.max_retries = max_retries
                return self.call(path=path,
                                 query=query,
                                 method=method,
                                 data=data,
                                 files=files,
                                 get_all_pages=get_all_pages,
                                 complete_response=complete_response)
            finally:
                self._retry_on = _retry_on
                self._max_retries = _max_retries

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
        request_count = 0

        while not all_requests_complete:
            # Make an http request
            # counts request attempts in order to fetch this specific one
            request_count += 1
            try:
                response = self.client.request(method,
                                               url,
                                               params=kwargs,
                                               json=json,
                                               data=data,
                                               headers=self.headers,
                                               files=files,
                                               **self.client_args)
            except requests.RequestException:
                if request_count <= self.max_retries:
                    # we have to bind response to None in case
                    # self.client.request raises an exception and
                    # response holds old requests.Response
                    # (and possibly its Retry-After header)
                    response = None
                    self._handle_retry(response)
                    continue
                else:
                    raise

            # If the response status is not in the 200 range then assume an
            # error and raise proper exception

            code = response.status_code
            try:
                if not 200 <= code < 300:
                    if code == 401:
                        raise AuthenticationError(
                            response.content, code, response)
                    elif code == 429:
                        raise RateLimitError(
                            response.content, code, response)
                    else:
                        raise ZendeskError(
                            response.content, code, response)
            except ZendeskError:
                if request_count <= self.max_retries:
                    self._handle_retry(response)
                    continue
                else:
                    raise

            if response.content.strip() and 'json' in response.headers['content-type']:
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
            request_count = 0

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

    def _handle_retry(self, resp):
        """Handle any exceptions during API request or
        parsing its response status code.

        Parameters:
        resp: requests.Response instance obtained during concerning request
            or None, when request failed

        Returns: True if should retry our request or raises original Exception
        """
        exc_t, exc_v, exc_tb = sys.exc_info()

        if exc_t is None:
            raise TypeError('Must be called in except block.')

        retry_on_exc = tuple(
            (x for x in self._retry_on if inspect.isclass(x)))
        retry_on_codes = tuple(
            (x for x in self._retry_on if isinstance(x, int)))

        if issubclass(exc_t, ZendeskError):
            code = exc_v.error_code
            if exc_t not in retry_on_exc and code not in retry_on_codes:
                six.reraise(exc_t, exc_v, exc_tb)
        else:
            if not issubclass(exc_t, retry_on_exc):
                six.reraise(exc_t, exc_v, exc_tb)

        if resp is not None:
            try:
                retry_after = float(resp.headers.get('Retry-After', 0))
                time.sleep(retry_after)
            except (TypeError, ValueError):
                pass

        return True
