# Zendesk API Wrapper for Python

Zdesk is a Python wrapper for the Zendesk API. This library provides an
easy and flexible way for developers to communicate with their Zendesk
account in their application.


## Requirements

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

# Example Use

```python
from zdesk import Zendesk

################################################################
## NEW CONNECTION CLIENT
################################################################
# Manually creating a new connection object
zendesk = Zendesk('https://yourcompany.zendesk.com', 'you@yourcompany.com', 'passwd')

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
result = zendesk.ticket_create(data=new_ticket, complete_response=True)

# URL to the created ticket
ticket_url = result['response']['location']

# Need ticket ID?
from zendesk import get_id_from_url
ticket_id = get_id_from_url(ticket_url)

# Show
zendesk.ticket_show(id=ticket_id)

# Delete
zendesk.ticket_delete(id=ticket_id)
```

See the [full example
file](https://github.com/fprimex/zdesk/blob/master/examples/__init__.py) on
github, however this is not anywhere close to covering all of the over 400 REST
API methods.

