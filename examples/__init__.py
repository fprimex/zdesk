from __future__ import print_function

import sys

try:
    import zdeskcfg
except ImportError:
    print('Could not import zdeskcfg, which is used to set up examples.')
    print('Please `pip install zdeskcfg`, or see the PyPI page:')
    print('https://pypi.python.org/pypi/zdeskcfg')
    sys.exit()

from zdesk import Zendesk

################################################################
## NEW CONNECTION CLIENT
################################################################
# Create an object using the [zdesk] section of
# ~/.zdeskcfg and the zdeskcfg module
#zendesk = Zendesk(**zdeskcfg.get_ini_config())

# Create an object using the [zdesk] and [sandbox] sections of
# ~/.zdeskcfg and the zdeskcfg module
zendesk = Zendesk(**zdeskcfg.get_ini_config(section='sandbox'))

# Manually creating a new connection object
#zendesk = Zendesk('https://yourcompany.zendesk.com', 'you@yourcompany.com', 'passwd')

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


################################################################
## ORGANIZATIONS
################################################################

# List
zendesk.organizations_list()

# Create
new_org = {
    'organization': {
        'name': 'Starbucks Corp'
    }
}
result = zendesk.organization_create(data=new_org, complete_response=True)
org_url = result['response']['location']
org_id = get_id_from_url(org_url)

# Show
zendesk.organization_show(id=org_id)

# Delete
zendesk.organization_delete(id=org_id)


################################################################
## USERS (AGENTS)
################################################################

# List
zendesk.users_list()

# Create
new_user = {
    'user': {
        'name': 'Howard Schultz',
        'email': 'howard@starbucks.com',
        'roles': 4,
    }
}
result = zendesk.user_create(data=new_user, complete_response=True)
user_url = result['response']['location']
user_id = get_id_from_url(user_url)

# Show
zendesk.user_show(id=user_id)

# Delete
zendesk.user_delete(id=user_id)


################################################################
## GROUPS
################################################################

# List
zendesk.groups_list()

# Create
new_group = {
    'group': {
        'name': 'Starbucks Group',
        'agents': [
            {
                'agent': 123
            },
        ]
    }
}
result = zendesk.group_create(data=new_group, complete_response=True)
group_url = result['response']['location']
group_id = get_id_from_url(group_url)

# Show
zendesk.group_show(id=group_id)

# Delete
zendesk.group_delete(id=group_id)


################################################################
## TAGS
################################################################

# List
zendesk.tags_list()


################################################################
## TICKET TYPES
################################################################
zendesk.ticket_fields_list()


################################################################
## SEARCH
################################################################
results = zendesk.search(query='type:ticket sort:desc', page=1)

