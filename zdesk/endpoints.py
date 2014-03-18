"""
API MAPPING

"""

mapping_table = {
    # Rest API: Organizations
    'list_organizations': {
        'path': '/organizations.json',
        'method': 'GET',
        'status': 200,
    },
    'show_organization': {
        'path': '/organizations/{{organization_id}}.json',
        'method': 'GET',
        'status': 200,
    },
    'create_organization': {
        'path': '/organizations.json',
        'method': 'POST',
        'status': 201,
    },
    'update_organization': {
        'path': '/organizations/{{organization_id}}.json',
        'method': 'PUT',
        'status': 200,
    },
    'delete_organization': {
        'path': '/organizations/{{organization_id}}.json',
        'method': 'DELETE',
        'status': 200,
    },
    # Rest API: Groups
    'list_groups': {
        'path': '/groups.json',
        'method': 'GET',
        'status': 200,
    },
    'show_group': {
        'path': '/groups/{{group_id}}.json',
        'method': 'GET',
        'status': 200,
    },
    'create_group': {
        'path': '/groups.json',
        'method': 'POST',
        'status': 201,
    },
    'update_group': {
        'path': '/groups/{{group_id}}.json',
        'method': 'PUT',
        'status': 200,
    },
    'delete_group': {
        'path': '/groups/{{group_id}}.json',
        'method': 'DELETE',
        'status': 200,
    },
    # Rest API: Tickets
    'list_tickets': {
        'path': '/rules/{{view_id}}.json',
        'valid_params': ('page', ),
        'method': 'GET',
        'status': 200,
    },
    'show_ticket': {
        'path': '/tickets/{{ticket_id}}.json',
        'method': 'GET',
        'status': 200,
    },
    'create_ticket': {
        'path': '/tickets.json',
        'method': 'POST',
        'status': 201,
    },
    'update_ticket': {
        'path': '/tickets/{{ticket_id}}.json',
        'method': 'PUT',
        'status': 200,
    },
    'comment_ticket': {
        'path': '/tickets/{{ticket_id}}.json',
        'method': 'PUT',
        'status': 200,
    },
    'delete_ticket': {
        'path': '/tickets/{{ticket_id}}.json',
        'method': 'DELETE',
        'status': 200,
    },
    # Rest API: Attachment
    'create_attachment': {
        'path': '/uploads.json',
        'valid_params': ('filename', 'token'),
        'method': 'POST',
        'status': 201,
    },
    # Rest API: Users
    'list_users': {
        'path': '/users.json',
        'valid_params': ('page', ),
        'method': 'GET',
        'status': 200,
    },
    'search_users': {
        'path': '/users.json',
        'valid_params': ('query', 'role', 'page'),
        'method': 'GET',
        'status': 200,
    },
    'show_user': {
        'path': '/users/{{user_id}}.json',
        'method': 'GET',
        'status': 200,
    },
    'create_user': {
        'path': '/users.json',
        'method': 'POST',
        'status': 201,
    },
    'update_user': {
        'path': '/users/{{user_id}}.json',
        'method': 'PUT',
        'status': 200,
    },
    'delete_user': {
        'path': '/users/{{user_id}}.json',
        'method': 'DELETE',
        'status': 200,
    },
    'list_user_identities': {
        'path': '/users/{{user_id}}/user_identities.json',
        'method': 'GET',
        'status': 200,
    },
    'add_user_email': {
        'path': '/users/{{user_id}}/user_identities.json',
        'method': 'POST',
        'status': 201,
    },
    'add_twitter_handle': {
        'path': '/users/{{user_id}}/user_identities.json',
        'method': 'POST',
        'status': 201,
    },
    'make_identity_primary': {
        'path': '/users/{{user_id}}/user_identities/{{identity_id}}/make_primary',
        'method': 'POST',
        'status': 200,
    },
    'delete_identity': {
        'path': '/users/{{user_id}}/user_identities/{{identity_id}}',
        'method': 'DELETE',
        'status': 200,
    },
    # Rest API: Tags
    'list_tags': {
        'path': '/tags.json',
        'method': 'GET',
        'status': 200,
    },
    'list_assets': {
        'path': '/tags/{{tag_id}}.json',
        'valid_params': ('asset_type', 'page'),
        'method': 'GET',
        'status': 200,
    },
    # Rest API: Ticket Fields
    'list_ticket_fields': {
        'path': '/ticket_fields.json',
        'method': 'GET',
        'status': 200,
    },
    # Rest API: Macros
    'list_macros': {
        'path': '/macros.json',
        'method': 'GET',
        'status': 200,
    },
    'evaluate_macro': {
        'path': '/macros/{{macro_id}}/apply.json',
        'valid_params': ('ticket_id', ),
        'method': 'POST',
        'status': 201,
    },
    # Rest API: Search
    'search': {
        'path': '/search.json',
        'valid_params': ('query', 'page'),
        'method': 'GET',
        'status': 200,
    },
}
