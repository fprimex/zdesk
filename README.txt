Zendesk API Wrapper for Python
=========================================================================================
Python Zendesk is wrapper for the Zendesk API. This library provides an
easy and flexible way for developers to communicate with their Zendesk
account in their application. 


Requirements
-----------------------------------------------------------------------------------------------------
httplib2 is used for authentication and requests

    (pip install | easy_install) httplib2

simplejson is used to serialze and deserialze requests and responses

    (pip install | easy_install) simplejson


Installation
-----------------------------------------------------------------------------------------------------
Zendesk Python Library is available on pypi, so installation should be fairly simple:

    (pip install | easy_install) zendesk


Example Use
-----------------------------------------------------------------------------------------------------

	from zendesk import Zendesk, get_id_from_url

	################################################################
	## NEW CONNECTION CLIENT
	################################################################
	zendesk = Zendesk('https://yourcompany.zendesk.com', 'you@yourcompany.com', 'passwd')

	################################################################
	## TICKETS
	################################################################

	# List
	zendesk.list_tickets(view_id=1) # Must have a view defined

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
	ticket_url = zendesk.create_ticket(data=new_ticket)
	ticket_id = get_id_from_url(ticket_url)

	# Show
	zendesk.show_ticket(ticket_id=ticket_id)

	# Delete
	zendesk.delete_ticket(ticket_id=ticket_id)

	# More examples in `examples` folder!


