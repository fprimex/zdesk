import re
from zendesk import Zendesk

def get_id_from_url(url):
    match = re.match(r".*/(?P<identifier>\d+)\.xml", url)
    if match and match.group('identifier'):
        return match.group('identifier')


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
post_data = Zendesk.dict2xml(new_org)
org_url = zendesk.create_organization(xml_data=post_data)
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
post_data = Zendesk.dict2xml(new_user)
user_url = zendesk.create_user(xml_data=post_data)
user_id = get_id_from_url(user_url)

# Show
zendesk.show_user(group_id=user_id)

# Delete
zendesk.delete_user(group_id=user_id)


################################################################
## GROUPS
################################################################

# List
zendesk.list_groups()

# Create
new_group = {
    'group': {
        'name': 'Starbucks Group',
        'agents': {
            '@type': 'array',
            'agent': 123,
        }
    }
}
post_data = Zendesk.dict2xml(new_group)
group_url = zendesk.create_group(xml_data=post_data)
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