"""
API MAPPING

"""

mapping_table = {
    # Rest API: Organizations
    'list_organizations': {
        'path': '/organizations.xml',
        'method': 'GET',
        'status': 200,
    },
    'show_organization': {
        'path': '/organizations/{{organization_id}}.xml',
        'method': 'GET',
        'status': 200,
    },
    'create_organization': {
        'path': '/organizations.xml',
        'method': 'POST',
        'status': 201,
    },
    'update_organization': {
        'path': '/organizations/{{organization_id}}.xml',
        'method': 'PUT',
        'status': 200,
    },
    'delete_organization': {
        'path': '/organizations/{{organization_id}}.xml',
        'method': 'DELETE',
        'status': 200,
    },
    # Rest API: Groups
    'list_groups': {
        'path': '/groups.xml',
        'method': 'GET',
        'status': 200,
    },
    'show_group': {
        'path': '/groups/{{group_id}}.xml',
        'method': 'GET',
        'status': 200,
    },
    'create_group': {
        'path': '/groups.xml',
        'method': 'POST',
        'status': 201,
    },
    'update_group': {
        'path': '/groups/{{group_id}}.xml',
        'method': 'PUT',
        'status': 200,
    },
    'delete_group': {
        'path': '/groups/{{group_id}}.xml',
        'method': 'DELETE',
        'status': 200,
    },
    # Rest API: Tickets
    'list_tickets': {
        'path': '/rules/{{view_id}}.xml?page={{page}}',
        'method': 'GET',
        'status': 200,
    },
    'show_ticket': {
        'path': '/tickets/{{ticket_id}}.xml',
        'method': 'GET',
        'status': 200,
    },
    'create_ticket': {
        'path': '/tickets.xml',
        'method': 'POST',
        'status': 201,
    },
    'update_ticket': {
        'path': '/tickets/{{ticket_id}}.xml',
        'method': 'PUT',
        'status': 200,
    },
    'comment_ticket': {
        'path': '/tickets/{{ticket_id}}.xml',
        'method': 'PUT',
        'status': 200,
    },
    'delete_ticket': {
        'path': '/tickets/{{ticket_id}}.xml',
        'method': 'DELETE',
        'status': 200,
    },
    # Rest API: Attachment
    'create_attachment': {
        'path': '/uploads.xml?filename={{filename}}&amp;token={{token}}',
        'method': 'POST',
        'status': 201,
    },
    # Rest API: Users
    'list_users': {
        'path': '/users.xml?page={{page}}',
        'method': 'GET',
        'status': 200,
    },
    'search_users': {
        'path': '/users.xml?query={{query}}&amp;role={{role}}&amp;page={{page}}',
        'method': 'GET',
    },
    'show_user': {
        'path': '/users/{{user_id}}.xml',
        'method': 'GET',
        'status': 200,
    },
    'create_user': {
        'path': '/users.xml',
        'method': 'POST',
        'status': 201,
    },
    'update_user': {
        'path': '/users/{{user_id}}.xml',
        'method': 'PUT',
        'status': 200,
    },
    'delete_user': {
        'path': '/users/{{user_id}}.xml',
        'method': 'DELETE',
        'status': 200,
    },
    'list_user_identities': {
        'path': '/users/{{user_id}}/user_identities.xml',
        'method': 'GET',
        'status': 200,
    },
    'add_user_email': {
        'path': '/users/{{user_id}}/user_identities.xml',
        'method': 'POST',
        'status': 201,
    },
    'add_twitter_handle': {
        'path': '/users/{{user_id}}/user_identities.xml',
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
        'path': '/tags.xml',
        'method': 'GET',
        'status': 200,
    },
    'list_assets': {
        'path': '/tags/{{tag_id}}.xml?for={{asset_type}}&amp;page={{page}}',
        'method': 'GET',
        'status': 200,
    },
    # Rest API: Ticket Fields
    'list_ticket_fields': {
        'path': '/ticket_fields.xml',
        'method': 'GET',
        'status': 200,
    },
    # Rest API: Macros
    'list_macros': {
        'path': '/macros.xml',
        'method': 'GET',
        'status': 200,
    },
    'evaluate_macro': {
        'path': '/macros/{{macro_id}}/apply.xml?ticket_id={{ticket_id}}',
        'method': 'POST',
        'status': 201,
    },
    # Rest API: Search
    'search': {
        'path': '/search.xml?query={{query}}&amp;page={{page}}',
        'method': 'GET',
        'status': 200,
    },
}