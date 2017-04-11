from __future__ import print_function

import sys

from zdesk import Zendesk

################################################################
# NEW CONNECTION CLIENT
################################################################

# README: To configure this example so that it will actually execute, you need
# to provide a valid Zendesk URL and login information. You have two options:
#
# 1. Install the zdeskcfg module and use it to configure your Zendesk object.
#
# To do this, first `pip install zdeskcfg`, then create a file `~/.zdeskcfg`
# with contents similar to the following:
#
# [zdesk]
# email = you@example.com
# password = t2EVLKMUtt2EVLKMUtt2EVLKMUtt2EVLKMUt
# url = https://example.zendesk.com
# token = 1
#
# [sandbox]
# url = https://example-sandbox22012201.zendesk.com
#
# 2. Provide a manual configuration below by editing the testconfig variable.
#
# In either case, you can use your actual password and set `token = 0` or
# `zdesk_token = False`, but it is a very good idea to configure an API token
# by visiting this URL at your own Zendesk instance:
# https://example.zendesk.com/settings/api/

try:
    import zdeskcfg

    # Create an object using the [zdesk] section of
    # ~/.zdeskcfg and the zdeskcfg module
    # zendesk = Zendesk(**zdeskcfg.get_ini_config())

    # Create an object using the [zdesk] and [sandbox] sections of
    # ~/.zdeskcfg and the zdeskcfg module
    zendesk = Zendesk(**zdeskcfg.get_ini_config(section='sandbox'))

except ImportError:
    testconfig = {
            'zdesk_email': 'you@example.com',
            'zdesk_password': 't2EVLKMUtt2EVLKMUtt2EVLKMUtt2EVLKMUt',
            'zdesk_url': 'https://example-sandbox22012201.zendesk.com',
            'zdesk_token': True
            }

    if testconfig['zdesk_url'] == \
            'https://example-sandbox22012201.zendesk.com':
        print(
            'Could not import zdeskcfg and no manual configuration provided.')
        print(
            'Please `pip install zdeskcfg` or edit example with '
            'manual configuration.')
        sys.exit()

    else:
        zendesk = Zendesk(**testconfig)

# Are you getting an error such as...
# "SSL routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed"?
# zendesk = Zendesk(
#    'https://yourcompany.zendesk.com', 'you@yourcompany.com', 'passwd',
#    client_args={
#        "disable_ssl_certificate_validation": True
#    }
# )


################################################################
# TICKETS
################################################################

# List
zendesk.tickets_list()

# Create
new_ticket = {
    'ticket': {
        'requester_name': 'Howard Schultz',
        'requester_email': 'howard@starbucks.com',
        'subject': 'My Starbucks coffee is cold!',
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

# If a response results in returning a [location] header, then that
# will be what is returned.
# Create a ticket and get its URL.
result = zendesk.ticket_create(data=new_ticket)

# Alternatively, you can get the complete response and get the location
# yourself. This can be useful for getting other response items that are
# not normally returned, such as result['content']['upload']['token']
# when using zendesk.upload_create()
#
# result = zendesk.ticket_create(data=new_ticket, complete_response=True)
# ticket_url = result['response']['location']
# ticket_id = get_id_from_url(ticket_url)

# Need ticket ID?
from zdesk import get_id_from_url
ticket_id = get_id_from_url(result)

# Show
zendesk.ticket_show(id=ticket_id)

# Ticket comments and uploads / attachments
commentbody = "Attaching example Python file"

# must be in the examples directory when executing so this file can be found
fname = '__init__.py'

with open(fname, 'rb') as fp:
    fdata = fp.read()

# MIME types can be detected with the magic module:
# import magic
# mime_type = magic.from_file(fname, mime=True)
# if type(mime_type) is bytes:
#    mime_type = mime_type.decode()

# But this file is known
mime_type = 'text/plain'

upload_result = zendesk.upload_create(
    fdata, filename=fname, mime_type=mime_type, complete_response=True)

# for making additional uploads
upload_token = upload_result['content']['upload']['token']

data = {
    "ticket": {
        "id": ticket_id,
        "comment": {
            "public": False,
            "body": commentbody
        }
    }
}

# I like to add this separately, because it's not an uncommon use case
# to have an automated ticket update that may or may not have uploads.
if upload_token != "":
    data['ticket']['comment']['uploads'] = [upload_token]

# Post the comment to the ticket, which should reference the upload
response = zendesk.ticket_update(ticket_id, data)

# Delete
zendesk.ticket_delete(id=ticket_id)


################################################################
# ORGANIZATIONS
################################################################

# List
zendesk.organizations_list()

# Create
new_org = {
    'organization': {
        'name': 'Starbucks Corp'
    }
}
result = zendesk.organization_create(data=new_org)
org_id = get_id_from_url(result)

# Show
zendesk.organization_show(id=org_id)

# Delete
zendesk.organization_delete(id=org_id)


################################################################
# USERS (AGENTS)
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
result = zendesk.user_create(data=new_user)
user_id = get_id_from_url(result)

# Show
zendesk.user_show(id=user_id)

# Delete
zendesk.user_delete(id=user_id)


################################################################
# GROUPS
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
result = zendesk.group_create(data=new_group)
group_id = get_id_from_url(result)

# Show
zendesk.group_show(id=group_id)

# Delete
zendesk.group_delete(id=group_id)


################################################################
# TAGS
################################################################

# List
zendesk.tags_list()


################################################################
# TICKET TYPES
################################################################
zendesk.ticket_fields_list()


################################################################
# SEARCH
################################################################
results = zendesk.search(query='type:ticket sort:desc', page=1)
