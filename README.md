# Zdesk is seeking a contributing team or maintainer

Active development on zdesk has been pretty slow for some time now. The zdesk
port is not official, and has been authored by just myself (Brent). While I
have received contributions, I am just one person. Add in a very busy personal
life and no direct professional obligation to maintain this library and you
have a recipe for stagnation.

I am seeking to connect with users who would be interested in contributing to
this project directly (commit access), or otherwise a suitable maintainer to
pass this library on to. I think there is a lot of promise in the generator
approach to do some more interesting things, but I simply cannot find the time
to code it up myself.

If you are interested, please email me directly: brent@fprimex.com

# Special thanks to HashiCorp

A big 'thank you' to [HashiCorp](https://www.hashicorp.com) for finding enough
value in this library and the utilities I've written that use it to allow me to
spend some more time on it.

# Note about documentation on github

Please refer to the documentation for the specific release you are running.

Releases are listed [here](https://github.com/fprimex/zdesk/releases).

# Zendesk API Wrapper for Python

Zdesk is a Python wrapper for the Zendesk API. This library provides an
easy and flexible way for developers to communicate with their Zendesk
account in their application.

See the [Zendesk developer site](https://developer.zendesk.com/) for API
documentation. The underlying `zdesk_api` module has been [automatically
generated](https://github.com/fprimex/zdgen)
from this documentation.

## Requirements

Zdesk works with both Python 2 and Python 3. Tested on Python 2.7.15 and 3.7.0.

The requests package is used for authentication and requests

    pip install requests

Note that if you are on an earlier version of Python on particular platforms,
you can receive [an
error](https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning)
from `urllib3`, which is packaged in with `requests`. The simplest solution is
to install or update the packages specified in the
[solution](https://urllib3.readthedocs.org/en/latest/security.html#pyopenssl).

    pip install pyopenssl ndg-httpsclient pyasn1

This should be all that is required. If additional steps are required this may
be a `zdesk` bug, so please [report it](https://github.com/fprimex/zdesk/issues).

## Installation

Zdesk is available on pypi, so installation should be fairly simple:

    pip install zdesk

## Related projects

* [zdeskcfg](https://github.com/fprimex/zdeskcfg): Automatically configure your
  zdesk scripts from a configuration file and command line arguments.
* [zdgrab](https://github.com/fprimex/zdgrab): Download and decompress ticket attachments.

# Notes on module usage

## Authentication

Zdesk supports three methods of authorizing to Zendesk instances: basic
authentication with a password, basic authentication with an API token, and
OAuth authentication with an OAuth bearer token. All three are supported by
`zdeskcfg` as well.

The options are as follows, by precedence:

* `zdesk_oauth` - OAuth bearer token. An implicit grant token that works with
this option can be generated at the [Zendesk developer
site](https://developer.zendesk.com/requests/new).

* `zdesk_email` + `zdesk_api` - Basic authentication with a Zendesk account email
and an API token as generated from
`https://your-company.zendesk.com/agent/admin/api/settings`.

* `zdesk_email` + `zdesk_password` - Basic authentication with a Zendesk account
email and the password for that user.

* `zdesk_email` + `zdesk_password` + `zdesk_token = True` - Basic authentication
with a Zendesk account email and an API token, indicating that the password
supplied is actually an API token. This option is deprecated in favor of
`zdesk_email` + `zdesk_api` and will be removed in a future release.

## API Keyword args

Zdesk attempts to identify query string parameters from the online
documentation. All query string parameters are optional (default to `None`),
and are provided for convenience and reference.

However, it is very difficult, if not impossible,  to accurately capture all
valid query parameters for a particular endpoint from the documentation. So,
zdesk passes all provided kwargs on to the Zendesk API as query string
parameters without validation, except those that it has reserved for its own
use. The current reserved kwargs (described in more detail below) are:

* `complete_response`
* `get_all_pages`
* `mime_type`
* `retry_on`
* `max_retries`
* `raw_query`
* `retval`

There are a few common query string parameters that the Zendesk API accepts for
many calls. The current list at the time of this writing is:

* `include`
* `page`
* `per_page`
* `sort_by`
* `sort_order`

## Results returned and getting all HTTP response info

Under normal circumstances, when a call is made and the response indicates
success, the value returned will be formatted to simplify usage. So if a JSON
response is returned with the expected return code, then instead of getting
back all of the HTTP response information, headers and all, the only thing that
is returned is the JSON, which will already be deserialized. In some cases,
only a single string in a particular header (location) is returned, and so
that will be the return value.

Passing `complete_response=True` will cause all response information to be
returned, which is the result of a `requests.request`.

## Getting a specific part of a result

The Zendesk service sometimes changes what exactly is returned and the
automatic return value determination may not be desired. Additionally, it can
be tedious to always request `complete_response=True` and working with all of
that information. So, now it is possible to pass `retval` in order to request a
specific part of the request. Valid values are `'content'`, `'code'`,
`'location'`, and `'headers'`.

For example, you may not care to retrieve the `location` from a ticket
creation, but you do want to check the HTTP return code to ensure success. You
can now pass `retval='code'` and then simply check to ensure that the code is
equal to (the integer) `201`.

## Getting all pages

There is a common pattern where a request will return one page of data along
with a `next_page` location. In order to retrieve all results, it is necessary
to continue retrieving every `next_page` location. The results then all need to
be processed together. A loop to get all pages ends up stamped throughout
Zendesk code, since many API methods return paged lists of objects.

As a convenience, passing `get_all_pages` to any API method will do this for
you, and will also merge all responses. The result is a single, large object
that appears to be the result of one single call. The logic for this
combination and reduction is well documented in the
[source](https://github.com/fprimex/zdesk/blob/master/zdesk/zdesk.py#L534)
(look for the line reading `Now we need to try to combine or reduce the
results`, if the line number has shifted since this writing).

## MIME types for data

By default, all `data` passed to requests is assumed to be of MIME type
`application/json`. The value of `data` in this default case should be a JSON
object, and it will automatically be converted using `json.dumps` for the
request.

Some endpoints such as those that allow file uploads expect `data` to be of a
different MIME type, and so this can be specified using the `mime_type` keyword
argument.

If working with files of an unknown MIME type, a module such as
[python-magic](https://pypi.python.org/pypi/python-magic/) can be useful. The
following code has worked well with zdesk scripts:

    # import, configure, and connect to Zendesk as shown in the example code.
    # zd = Zendesk(...

    import magic

    fname = 'my_file'

    mime_type = magic.from_file(fname, mime=True)
    if type(mime_type) is bytes:
        mime_type = mime_type.decode()

    with open(fname, 'rb') as fp:
        fdata = fp.read()

    response = zd.upload_create(filename=fname,
            data=fdata, mime_type=mime_type, complete_response=True)

    upload_token = response['content']['upload']['token']

## Multipart file uploads (Help Center attachments)

In addition to the `data` argument, zdesk methods can also take a `files`
argument. This is a tuple which is passed directly to the `requests` module, so
you may wish to reference [their
documentation](http://requests.readthedocs.org/en/latest/user/quickstart/#post-a-multipart-encoded-file).

Here is an example of using the `help_center_article_attachment_create` method.

    zd.help_center_article_attachment_create(article_id='205654433', data={},
            files={'file':('attach.zip', open('attach.zip', 'rb'))})

The `data` parameter should always be supplied, containing any desired optional
parameters such as `data={'inline':'true'}`, or `{}` otherwise. The file data
can be provided directly in the tuple, and the MIME type can be explicitly
specified.

    with open('attach.zip', 'rb') as f:
        fdata = f.read()

    zd.help_center_article_attachment_create(article_id='205654433', data={},
            files={'file':('attach.zip', fdata, 'application/zip')})

## Raw query strings

In some cases it is necessary to pass query parameters that are the same
parameter but differ by value, such as multiple `start_time` or `end_time`
values. This makes it impossible to use a simple dictionary of query parameters
and values. To enable this use case it is now possible to pass a string,
starting with `?`, using `raw_query`. This value overrides all query parameters
that are named or passed with `kwargs`, and is appended to the URL. The string
will be appropriately encoded by `requests`, so there is no need to pre-encode
it before passing.

## Rate limits and retrying

It is possible to retry all requests made by an instance of `Zendesk` by
providing `retry_on` and `max_retries` to `__init__`.
In addition, it is also possible to retry one `Zendesk.call` without modifying
it's attributes - simply by supplying those kwargs to `Zendesk.call`.

`retry_on` specifies on which exceptions raised you want to retry your request.
There is also possibility to retry on specific non-200 HTTP codes, also by
specyfing them in `retry_on`. `ZendeskError` and `requests.RequestsError`
combined are catch-alls.

`max_retries` controls how many attempts are made if first request fails.
Note that with `get_all_pages` this can make up to `(max_retries + 1) * pages`
requests. Currently there is no support for exponential backoff.

# Example Use

```python
from zdesk import Zendesk

################################################################
## NEW CONNECTION CLIENT
################################################################
# Manually creating a new connection object
zendesk = Zendesk('https://yourcompany.zendesk.com', 'you@yourcompany.com', 'passwd')

# If using an API token, you can create connection object using
# zendesk = Zendesk('https://yourcompany.zendesk.com', 'you@yourcompany.com', 'token', True)
# True specifies that the token is being used instead of the password

# See the zdeskcfg module for more sophisticated configuration at
# the command line and via a configuration file.
# https://github.com/fprimex/zdeskcfg

################################################################
## TICKETS
################################################################

# List
zendesk.tickets_list()

# Create
new_ticket = {
    'ticket': {
        'requester': {
            'name': 'Howard Schultz',
            'email': 'howard@starbucks.com',
        },
        'subject':'My Starbucks coffee is cold!',
        'description': 'please reheat my coffee',
        'tags': ['coffee', 'drinks'],
        'ticket_field_entries': [
            {
                'ticket_field_id': 1,
                'value': 'venti'
            },
            {
                'ticket_field_id': 2,
                'value': '$10'
            }
        ]
    }
}
# Create the ticket and get its URL
result = zendesk.ticket_create(data=new_ticket)

# Need ticket ID?
from zdesk import get_id_from_url
ticket_id = get_id_from_url(result)

# Show
zendesk.ticket_show(id=ticket_id)

# Delete
zendesk.ticket_delete(id=ticket_id)
```

See the [full example
file](https://github.com/fprimex/zdesk/blob/master/examples/example.py) on
github, however this is not anywhere close to covering all of the over 400 REST
API methods.

