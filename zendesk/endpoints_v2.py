"""
API MAPPING FOR Zendesk API V2
"""

mapping_table = {

    # Tickets
    'list_all_tickets': {
        'path': '/tickets.json',
        'method': 'GET',
    },
    'show_ticket': {
        'path': '/tickets/{{ticket_id}}.json',
        'method': 'GET',
    },
    'show_many_tickets': {
        'path': '/tickets/show_many.json',
        'valid_params': ['ids'],
        'method': 'POST'
    },
    'create_ticket': {
        'path': '/tickets.json',
        'method': 'POST',
    },
    'update_ticket': {
        'path': '/tickets/{{ticket_id}}.json',
        'method': 'PUT',
    },
    'update_many_tickets': {
        'path': '/tickets/update_many.json',
        'valid_params': ['ids'],
        'method': 'PUT',
    },
    'delete_ticket': {
        'path': '/tickets/{{ticket_id}}.json',
        'method': 'DELETE',
    },
    'delete_many_tickets': {
        'path': 'tickets/destroy_many.json',
        'valid_params': ['ids'],
        'method': 'DELETE',
    },
    'list_ticket_collaborators': {
        'path': '/tickets/{{ticket_id}}/collaborators.json',
        'method': 'GET',
    },
    'list_ticket_incidents': {
        'path': '/tickets/{{ticket_id}}/incidents.json',
        'method': 'GET',
    },

    # Ticket Audits
    'list_audits': {
        'path': '/tickets/{{ticket_id}}/audits.json',
        'method': 'GET',
    },
    'mark_audit_as_trusted': {
        'path': '/tickets/{{ticket_id}}/audits/{{audid_id}}/trust.json',
        'method': 'PUT',
    },

    # Incremental Tickets
    'export_incremental_tickets': {
        'path': '/exports/tickets.json',
        'valid_params': ['start_time'],
        'method': 'GET',
    },

    # Ticket Fields
    'list_ticket_fields': {
        'path': '/ticket_fields.json',
        'method': 'GET',
    },
    'show_ticket_field': {
        'path': '/ticket_fields/{{ticket_field_id}}.json',
        'method': 'GET',
    },
    'create_ticket_field': {
        'path': '/ticket_fields.json',
        'method': 'POST',
    },
    'update_ticket_field': {
        'path': '/ticket_fields/{{ticket_field_id}}.json',
        'method': 'PUT',
    },
    'delete_ticket_field': {
        'path': '/ticket_fields/{{ticket_field_id}}.json',
        'method': 'DELETE',
    },
    
    # Views
    'list_views': {
        'path': '/views.json',
        'method': 'GET',
    },
    'list_active_views': {
        'path': '/views/active.json',
        'method': 'GET',
    },
    'get_view': {
        'path': '/views/{{view_id}}.json',
        'method': 'GET',
    },
    'execute_view': {
        'path': '/views/{{view_id}}/execute.json',
        'method': 'GET',
    },
    'preview_view': {
        'path': '/views/preview.json',
        'method': 'POST',
    },
    'count_many_views': {
        'path': '/views/count_many.json',
        'valid_params': ('ids',),
        'method': 'GET',
    },
    'count_view': {
        'path': '/views/{{view_id}}/count.json',
        'method': 'GET',
    },

    # Users
    'list_users': {
        'path': '/users.json',
        'valid_params': ('role','page'),
        'method': 'GET',
    },
    'list_users_in_group': {
        'path': '/groups/{{group_id}}/users.json',
        'valid_params': ('role','page'),
        'method': 'GET',
    },
    'list_users_in_organization': {
        'path': '/organization/{{organization_id}}/users.json',
        'valid_params': ('role','page'),
        'method': 'GET',
    },
    'show_user': {
        'path': '/users/{{user_id}}.json',
        'method': 'GET',
    },
    'create_user': {
        'path': '/users.json',
        'method': 'POST',
    },
    'create_many_users': {
        'path': '/users/create_many.json',
        'method': 'POST',
    },
    'update_user': {
        'path': '/users/{{user_id}}.json',
        'method': 'PUT',
    },
    'delete_user': {
        'path': '/users/{{user_id}}.json',
        'method': 'DELETE',
    },
    'search_user': {
        'path': '/users/search.json',
        'valid_params': ['query', 'external_id'],
        'method': 'GET',
    },
    'show_me': {
        'path': '/users/me.json',
        'method': 'GET',
    },

    # Requests
    'list_requests': {
        'path': '/requests.json',
        'method': 'GET',
    },
    'list_open_requests': {
        'path': '/requests/open.json',
        'method': 'GET',
    },
    'list_solved_requests': {
        'path': '/requests/solved.json',
        'method': 'GET',
    },
    'list_ccd_requests': {
        'path': '/requests/ccd.json',
        'method': 'GET',
    },
    'list_requests_for_user': {
        'path': '/users/{{user_id}}/requests.json',
        'method': 'GET',
    },
    'show_request': {
        'path': '/requests/{{request_id}}.json',
        'method': 'GET',
    },
    'create_request': {
        'path': '/requests.json',
        'method': 'POST',
    },
    'update_request': {
        'path': '/requests/{{request_id}}.json',
        'method': 'PUT',
    },
    'list_comments': {
        'path': '/requests/{{request_id}}/comments.json',
        'method': 'GET',
    },
    'show_comment': {
        'path': '/requests/{{request_id}}/comments/{{comment_id}}.json',
        'method': 'GET',
    },

    # User Identities
    'list_user_identities': {
        'path': '/users/{{user_id}}/identities.json',
        'method': 'GET',
    },
    'show_user_identity': {
        'path': '/users/{{user_id}}/identities/{{identity_id}}.json',
        'method': 'GET',
    },
    'create_user_identity': {
        'path': '/users/{{user_id}}/identities.json',
        'method': 'POST',
    },
    'update_user_identity': {
        'path': '/users/{{user_id}}/identities/{{identity_id}}.json',
        'valid_params': ['identityverified'],
        'method': 'PUT',
    },
    'make_user_identity_primary': {
        'path': '/users/{{user_id}}/identities/{{identity_id}}/make_primary',
        'method': 'PUT',
    },
    'verify_user_identity': {
        'path': '/users/{{user_id}}/identities/{{identity_id}}/verify',
        'method': 'PUT',
    },
    'request_user_identity_verification': {
        'path': '/users/{{user_id}}/identities/{{identity_id}}/request_verification',
        'method': 'PUT',
    },
    'delete_user_identity': {
        'path': '/users/{{user_id}}/identities/{{identity_id}}.json',
        'method': 'DELETE',
    },

    # Groups
    'list_groups': {
        'path': '/groups.json',
        'method': 'GET',
    },
    'list_assignable_groups': {
        'path': '/groups/assignable.json',
        'method': 'GET',
    },
    'show_group': {
        'path': '/groups/{{group_id}}.json',
        'method': 'GET',
    },
    'create_group': {
        'path': '/groups.json',
        'method': 'POST',
    },
    'update_group': {
        'path': '/groups/{{group_id}}.json',
        'method': 'PUT',
    },
    'delete_group': {
        'path': '/groups/{{group_id}}.json',
        'method': 'DELETE',
    },

    # Group Memberships
    'list_memberships': {
        'path': '/group_memberships.json',
        'method': 'GET',
    },
    'list_memberships_for_user': {
        'path': '/users/{{user_id}}/group_memberships.json',
        'method': 'GET',
    },
    'list_memberships_for_group': {
        'path': '/groups/{{group_id}}/group_memberships.json',
        'method': 'GET',
    },
    'list_assignable_memberships': {
        'path': '/group_memberships/assignable.json',
        'method': 'GET',
    },
    'list_assignable_memberships_for_group': {
        'path': 'groups/{{groups_id}}/group_memberships/assignable.json',
        'method': 'GET',
    },
    'show_membership': {
        'path': '/group_memberships/{{group_membership_id}}.json',
        'method': 'GET',
    },
    'show_membership_for_user': {
        'path': '/users/{{user_id}}/group_memberships/{{group_membership_id}}.json',
        'method': 'GET',
    },
    'create_membership': {
        'path': '/group_memberships.json',
        'method': 'POST',
    },
    'create_membership_for_user': {
        'path': '/users/{{user_id}}/group_memberships.json',
        'method': 'POST',
    },
    'delete_membership': {
        'path': '/group_memberships/{{group_membership_id}}.json',
        'method': 'DELETE',
    },
    'delete_membership_for_user': {
        'path': '/users/{{user_id}}/group_memberships/{{group_membership_id}}.json',
        'method': 'DELETE',
    },
    'set_default_membership_for_user': {
        'path': '/users/{{user_id}}/group_memberships/{{group_membership_id}}/make_default.json',
        'method': 'PUT',
    },

    # Custom Agent Rules
    'list_custom_roles': {
        'path': '/custom_roles.json',
        'method': 'GET',
    },

    # Organizations
    'list_organizations': {
        'path': '/organizations.json',
        'method': 'GET',
    },
    'autocomplete_organizations': {
        'path': '/organizations/autocomplete.json',
        'valid_params': ['name'],
        'method': 'GET',
    },
    'show_organization': {
        'path': '/organizations/{{organization_id}}.json',
        'method': 'GET',
    },
    'create_organization': {
        'path': '/organizations.json',
        'method': 'POST',
    },
    'update_organization': {
        'path': '/organizations/{{organization_id}}.json',
        'method': 'PUT',
    },
    'delete_organization': {
        'path': '/organizations/{{organization_id}}.json',
        'method': 'DELETE',
    },

    # Search
    'search': {
        'path': '/search.json',
        'valid_params': ['query'],
        'method': 'GET',
    },
    'anonymous_search': {
        'path': '/portal_search.json',
        'valid_params': ['query'],
        'method': 'GET',
    },

    # Tags
    'list_tags': {
        'path': '/tags.json',
        'method': 'GET',
    },

    # Forums
    'list_forums': {
        'path': '/forums.json',
        'method': 'GET',
    },
    'list_forums_catagory': {
        'path': '/catagories/{{catagory_id}}/forums.json',
        'method': 'GET',
    },
    'show_forum': {
        'path': '/forums/{{forum_id}}.json',
        'method': 'GET',
    },
    'create_forum': {
        'path': '/forums.json',
        'method': 'POST',
    },
    'update_forum': {
        'path': '/forums/{{forum_id}}.json',
        'method': 'PUT',
    },
    'delete_forum': {
        'path': '/forums/{{forum_id}}.json',
        'method': 'DELETE',
    },

    # Forum Subscriptions
    'list_forum_subscriptions': {
        'path': '/forum_subscriptions.json',
        'method': 'GET',
    },
    'list_forum_subscriptions_for_forum': {
        'path': '/forum/{{forum_id}}/subscriptions.json',
        'method': 'GET',
    },
    'show_forum_subscription': {
        'path': '/forum_subscriptions/{{forum_subscription_id}}.json',
        'method': 'GET',
    },
    'create_forum_subscription': {
        'path': '/forum_subscriptions.json',
        'method': 'POST',
    },
    'delete_forum_subscription': {
        'path': '/forum_subscriptions/{{forum_subscription_id}}.json',
        'method': 'DELETE',
    },

    # Categories
    'list_categories': {
        'path': '/categories.json',
        'method': 'GET',
    },
    'show_category': {
        'path': '/category/{{category_id}}.json',
        'method': 'GET',
    },
    'create_category': {
        'path': '/categories.json',
        'method': 'GET',
    },
    'update_category': {
        'path': '/category/{{category_id}}.json',
        'method': 'PUT',
    },
    'delete_category': {
        'path': '/category/{{category_id}}.json',
        'method': 'DELETE',
    },

    # Topics
    'list_topics': {
        'path': '/topics.json',
        'method': 'GET',
    },
    'list_topics_for_forum': {
        'path': '/forums/{{forum_id}}/topics.json',
        'method': 'GET',
    },
    'list_topics_for_user': {
        'path': '/users/{{user_id}}/topics.json',
        'method': 'GET',
    },
    'show_topic': {
        'path': '/topics/{{topic_id}}.json',
        'method': 'GET',
    },
    'show_many_topics': {
        'path': '/topics/show_many.json',
        'valid_params': ['ids'],
        'method': 'GET',
    },
    'create_topics': {
        'path': '/topics.json',
        'method': 'POST',
    },
    'update_topic': {
        'path': '/topics/{{topic_id}}.json',
        'method': 'PUT',
    },
    'delete_topic': {
        'path': '/topics/{{topic_id}}.json',
        'method': 'DELETE',
    },
    
    # Topic Comments
    'list_topic_comments': {
        'path': '/topics/{{topic_id}}/comments.json',
        'method': 'GET',
    },
    'list_topic_comments_for_user': {
        'path': '/users/{{user_id}}/top_comments.json',
        'method': 'GET',
    },
    'show_topic_comment': {
        'path': '/topics/{{topic_id}}/comments/{{comment_id}}.json',
        'method': 'GET',
    },
    'show_topic_comment_for_user': {
        'path': '/users/{{user_id}}/top_comments/{{comment_id}}.json',
        'method': 'GET',
    },
    'create_topic_comments': {
        'path': '/topics/{{topic_id}}/comments.json',
        'method': 'POST',
    },
    'update_topic_comment': {
        'path': '/topics/{{topic_id}}/comments/{{comment_id}}.json',
        'method': 'PUT',
    },
    'delete_topic_comment': {
        'path': '/topics/{{topic_id}}/comments/{{comment_id}}.json',
        'method': 'DELETE',
    },

    # Topic Subscriptions
    'list_topic_subscriptions': {
        'path': '/topic_subscriptions.json',
        'method': 'GET',
    },
    'list_subscriptions_for_topic': {
        'path': '/topic/{{topic_id}}/subscriptions.json',
        'method': 'GET',
    },
    'show_topic_subscription': {
        'path': '/topic_subscriptions/{{topic_subscription_id}}.json',
        'method': 'GET',
    },
    'create_topic_subscription': {
        'path': '/topic_subscriptions.json',
        'method': 'POST',
    },
    'delete_topic_subscription': {
        'path': '/topic_subscriptions/{{topic_subscription_id}}.json',
        'method': 'DELETE',
    },

    # Topic Votes
    'list_topic_votes': {
        'path': '/topics/{{topic_id}}/votes.json',
        'method': 'GET',
    },
    'list_topic_votes_for_user': {
        'path': '/user/{{user_id}}/topic_votes.json',
        'method': 'GET',
    },
    'show_topic_vote': {
        'path': '/topics/{{topic_id}}/vote.json',
        'method': 'GET',
    },
    'create_topic_vote': {
        'path': '/topics/{{topic_id}}/vote.json',
        'method': 'POST',
    },
    'delete_topic_vote': {
        'path': '/topics/{{topic_id}}/vote.json',
        'method': 'DELETE',
    },

    # Account Settings
    'show_account_settings': {
        'path': '/account/settings.json',
        'method': 'GET',
    },

    # Activity Stream
    'list_activities': {
        'path': '/activities.json',
        'method': 'GET',
    },
    'show_activity': {
        'path': '/activities/{{activity_id}}.json',
        'method': 'GET',
    },

    # Attachments
    'upload_attachment': {
        'path': '/uploads.json',
        'method': 'POST',
    },

    # Job Statuses
    'show_job_status': {
        'path': '/job_statuses/{{job_id}}.json',
        'method': 'GET',
    },

    # Locales
    'list_locales': {
        'path': '/locales.json',
        'method': 'GET',
    },
    'list_locales_for_agents': {
        'path': '/locales/agent.json',
        'method': 'GET',
    },
    'show_locale': {
        'path': '/locales/{{locale_id}}.json',
        'method': 'GET',
    },
    'show_current_locale': {
        'path': '/locales/current.json',
        'method': 'GET',
    },

    # Macros
    'list_macros': {
        'path': '/macros.json',
        'method': 'GET',
    },
    'list_active_macros': {
        'path': '/macros/active.json',
        'method': 'GET',
    },
    'show_macro': {
        'path': '/macros/{{macro_id}}.json',
        'method': 'GET',
    },
    'apply_macro': {
        'path': '/macros/{{macro_id}}/apply.json',
        'method': 'GET',
    },
    'apply_macro_for_ticket': {
        'path': '/tickets/{{ticket_id}}/macros/{{macro_id}}/apply.json',
        'method': 'GET',
    },

    # List Satisfaction Ratings
    'list_satisfaction_ratings': {
        'path': '/satisfaction_ratings.json',
        'method': 'GET',
    },
    'list_received_satisfaction_ratings': {
        'path': '/satisfaction_ratings/received.json',
        'method': 'GET',
    },
    'show_satisfaction_rating': {
        'path': '/satisfaction_ratings/{{satisfaction_rating_id}}.json',
        'method': 'GET',
    },

    # Suspended Tickets
    'list_suspended_tickets': {
        'path': '/suspended_tickets.json',
        'method': 'GET',
    },
    'show_suspended_ticket': {
        'path': '/suspended_tickets/{{ticket_id}}.json',
        'method': 'GET',
    },
    'recover_suspended_ticket': {
        'path': '/suspended_tickets/{{ticket_id}}/recover.json',
        'method': 'PUT',
    },
    'recover_many_suspended_tickets': {
        'path': '/suspended_tickets/recover_many.json',
        'valid_params' : ['ids'],
        'method': 'PUT',
    },
    'delete_suspended_ticket': {
        'path': '/suspended_tickets/{{ticket_id}}.json',
        'method': 'DELETE',
    },
    'delete_many_suspended_tickets': {
        'path': '/suspended_tickets/destroy_many.json',
        'valid_params' : ['ids'],
        'method': 'DELETE',
    },
}

# Patch mapping table with correct HTTP Status expected
for method, api_map in mapping_table.iteritems():
    status = 200
    if method.startswith('create_'):
        status = 201
    api_map['status'] = status
