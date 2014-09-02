# Zendesk API Wrapper for Python

Python Zendesk is wrapper for the Zendesk API version 2. This library provides
an easy and flexible way for developers to communicate with their Zendesk
account in their application. 


## Requirements

Python 2 or Python 3

httplib2 is used for authentication and requests

    (pip install | easy_install) httplib2

simplejson is used to serialze and deserialze requests and responses

    (pip install | easy_install) simplejson


## Installation

Zdesk Python Library is available on pypi, so to install zdesk and its
dependencies, run:

    (pip install | easy_install) zdesk


# Example Use

```python
from zdesk import Zendesk, get_id_from_url

# Create a new connection to your Zendesk
zd = Zendesk('https://yourcompany.zendesk.com', 'you@yourcompany.com', 'passwd')

# List tickets as defined by a view
zd.list_tickets(view_id=1) # Must have a view defined

# Create a new ticket
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
ticket_url = zd.create_ticket(data=new_ticket)
ticket_id = get_id_from_url(ticket_url)

# Show a ticket
zd.show_ticket(ticket_id=ticket_id)

# Delete a ticket
zd.delete_ticket(ticket_id=ticket_id)

# More examples in `examples` folder!
```
