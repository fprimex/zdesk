from zendesk import Zendesk

################################################################
## NEW CONNECTION CLIENT
################################################################
zendesk = Zendesk('https://yourcompany.zendesk.com', 'you@yourcompany.com', 'passwd')

# Are you getting an error such as...
# "SSL routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed"?
zendesk = Zendesk('https://yourcompany.zendesk.com', 'you@yourcompany.com', 'passwd',
    client_args={
        "disable_ssl_certificate_validation": True
    }
)


################################################################
## TICKETS
################################################################

# List
zendesk.list_tickets(view_id=1) # Must have a view defined

# Create
new_ticket = {
    'ticket': { _
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

# Need ticket ID?
from zendesk import get_id_from_url
ticket_id = get_id_from_url(ticket_url)

# Show
zendesk.show_ticket(ticket_id=ticket_id)

# Delete
zendesk.delete_ticket(ticket_id=ticket_id)


################################################################
## ORGANIZATIONS
################################################################

# List
zendesk.list_organizations()

# Create
new_org = {
    'organization': {
        'name': 'Starbucks Corp'
    }
}
org_url = zendesk.create_organization(data=new_org)
org_id = get_id_from_url(org_url)

# Show
zendesk.show_organization(organization_id=org_id)

# Delete
zendesk.delete_organization(organization_id=org_id)


################################################################
## USERS (AGENTS)
################################################################

# List
zendesk.list_users()

# Create
new_user = {
    'user': {
        'name': 'Howard Schultz',
        'email': 'howard@starbucks.com',
        'roles': 4,
    }
}
user_url = zendesk.create_user(data=new_user)
user_id = get_id_from_url(user_url)

# Show
zendesk.show_user(user_id=user_id)

# Delete
zendesk.delete_user(user_id=user_id)


################################################################
## GROUPS
################################################################

# List
zendesk.list_groups()

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
group_url = zendesk.create_group(data=new_group)
group_id = get_id_from_url(group_url)

# Show
zendesk.show_group(group_id=group_id)

# Delete
zendesk.delete_group(group_id=group_id)


################################################################
## TAGS
################################################################

# List
zendesk.list_tags()

# Show
zendesk.list_assets(tag_id=123, asset_type='event') # event | entry


################################################################
## TICKET TYPES
################################################################
zendesk.list_ticket_fields()


################################################################
## SEARCH
################################################################

# http://www.zendesk.com/api/search
# make sure to url-encode the query
results = zendesk.search(query='ticket+sort:desc', page=1)