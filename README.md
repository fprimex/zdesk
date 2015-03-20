# Zendesk API Wrapper for Python

Zdesk is a Python wrapper for the Zendesk API. This library provides an
easy and flexible way for developers to communicate with their Zendesk
account in their application.

See the [Zendesk developer site](https://developer.zendesk.com/) for API
documentation. The underlying `zdesk_api` module has been automatically
generated from this documentation.

## Requirements

Zdesk works with both Python 2 and Python 3. Tested on Python 2.7.5 and 3.4.1.

httplib2 is used for authentication and requests

    (pip install | easy_install) httplib2

simplejson is used to serialze and deserialze requests and responses

    (pip install | easy_install) simplejson

## Installation

Zdesk is available on pypi, so installation should be fairly simple:

    (pip install | easy_install) zdesk

## Related projects

* [zdeskcfg](https://github.com/fprimex/zdeskcfg): Automatically configure your
  zdesk scripts from a configuration file and command line arguments.
* [zdgrab](https://github.com/fprimex/zdgrab): Download and decompress ticket attachments.

# Notes on module usage

## API Keyword args

There are a few keyword arguments that every API method accepts that
corresponds with Zendesk API query string options for most calls. These are
kept in `zdesk.common_params`. The current list at the time of this writing is:

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
only a single string in a particular heading (location) is returned, and so
that will be the return value.

Passing `complete_response=True` will cause all response information to be
returned, which is the result of an `httplib2.client.request`.

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
[source](https://github.com/fprimex/zdesk/blob/master/zdesk/zdesk.py#L235)
(look for the line reading `Now we need to try to combine or reduce the
results`, if the line number has shifted since this writing).

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

# Are you getting an error such as...
# "SSL routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed"?
#zendesk = Zendesk('https://yourcompany.zendesk.com', 'you@yourcompany.com', 'passwd',
#    client_args={
#        "disable_ssl_certificate_validation": True
#    }
#)


################################################################
## TICKETS
################################################################

# List
zendesk.tickets_list()

# Create
new_ticket = {
    'ticket': {
        'requester_name': 'Howard Schultz',
        'requester_email': 'howard@starbucks.com',
        'subject':'My Starbucks coffee is cold!',
        'description': 'please reheat my coffee',
        'set_tags': 'coffee drinks',
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
file](https://github.com/fprimex/zdesk/blob/master/examples/__init__.py) on
github, however this is not anywhere close to covering all of the over 400 REST
API methods.

