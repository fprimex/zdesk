Zendesk API Wrapper for Python
=========================================================================================
Python Zendesk is wrapper for the Zendesk API. This library provides an
easy and flexible way for developers to communicate with their Zendesk
account in their application. 


Requirements
-----------------------------------------------------------------------------------------------------
httplib2 is used for authentication and requests

    (pip install | easy_install) httplib2

dict2xml is used to create XML documents that will be posted to
Zendesk. This module is included with this distribution, but credit goes to
Vojtech Rylko: https://github.com/vojtarylko/dict2xml


Installation
-----------------------------------------------------------------------------------------------------
Zendesk Python Library is available on pypi, so installation should be fairly simple:

    (pip install | easy_install) zendesk


Example Use
-----------------------------------------------------------------------------------------------------

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
	        'requester-name': 'Howard Schultz',
	        'requester-email': 'howard@starbucks.com',
	        'subject':'My Starbucks coffee is cold!',
	        'description': 'please reheat my coffee',
	        'set-tags': 'coffee drinks',
	        'ticket-field-entries': {
	            '@type': 'array',
	            'ticket-field-entry': [
	                {'ticket-field-id': 1, 'value': 'venti'},
	                {'ticket-field-id': 2, 'value': '$10'}
	            ]
	        },
	    }
	}
	post_data = Zendesk.dict2xml(new_ticket)
	ticket_url = zendesk.create_ticket(xml_data=post_data)
	ticket_id = get_id_from_url(ticket_url)

	# Show
	zendesk.show_ticket(ticket_id=ticket_id)

	# Delete
	zendesk.delete_ticket(ticket_id=ticket_id)           

	# More examples in `examples` folder!


