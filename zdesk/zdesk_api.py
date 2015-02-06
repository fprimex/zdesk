class ZendeskAPI:
    "Class generated from Zendesk REST API documentation. See api_gen.py."

    def __init__(self):
        pass

    def call(self, path, query=None, method='GET', status=200, data=None, **kwargs):
        pass

    # Duplicate API endpoint discarded: dynamic_content_item_variant_create from developer.zendesk.com/rest_api/docs/core/dynamic_content
    # Duplicate API endpoint discarded: help_center_incremental_articles_list from developer.zendesk.com/rest_api/docs/help_center/articles
    # Duplicate API endpoint discarded: user_fields_reorder from developer.zendesk.com/rest_api/docs/core/user_fields

    def account_settings_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/account_settings"
        api_path = "/api/v2/account/settings.json"
        return self.call(api_path, **kwargs)

    def account_settings_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/account_settings"
        api_path = "/api/v2/account/settings.json"
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def activities_list(self, since=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/activity_stream"
        api_path = "/api/v2/activities.json"
        api_query = {}
        if since:
            api_query.update({
                "since": since,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def activity_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/activity_stream"
        api_path = "/api/v2/activities/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def app_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps.json"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def app_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def app_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def app_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def apps_installation_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/installations.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def apps_installation_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/installations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def apps_installation_requirements(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/installations/{id}/requirements.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def apps_installation_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/installations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def apps_installation_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/installations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def apps_installations_job_status_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/installations/job_statuses/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def apps_installations_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/installations.json"
        return self.call(api_path, **kwargs)

    def apps_job_status_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/job_statuses/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def apps_location_installation_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/app_location_installations"
        api_path = "/api/v2/apps/location_installations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def apps_location_installations_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/app_location_installations"
        api_path = "/api/v2/apps/location_installations.json"
        return self.call(api_path, **kwargs)

    def apps_location_installations_reorder(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/app_location_installations"
        api_path = "/api/v2/apps/location_installations/reorder.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def apps_location_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/app_locations"
        api_path = "/api/v2/apps/locations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def apps_locations_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/app_locations"
        api_path = "/api/v2/apps/locations.json"
        return self.call(api_path, **kwargs)

    def apps_notify_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/notify.json"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def apps_owned_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/owned.json"
        return self.call(api_path, **kwargs)

    def apps_upload_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/uploads.json"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def attachment_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/attachments"
        api_path = "/api/v2/attachments/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def attachment_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/attachments"
        api_path = "/api/v2/attachments/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def audit_log_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/audit_logs"
        api_path = "/api/v2/audit_logs/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def audit_logs_list(self, filter_actor_id=None, filter_created_at=None, filter_ip_address=None, filter_source_type=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/audit_logs"
        api_path = "/api/v2/audit_logs.json"
        api_query = {}
        if filter_actor_id:
            api_query.update({
                "filter[actor_id]": filter_actor_id,
            })
        if filter_created_at:
            api_query.update({
                "filter[created_at]": filter_created_at,
            })
        if filter_ip_address:
            api_query.update({
                "filter[ip_address]": filter_ip_address,
            })
        if filter_source_type:
            api_query.update({
                "filter[source_type]": filter_source_type,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def autocomplete_tags(self, name, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/autocomplete"
        api_path = "/api/v2/autocomplete/tags.json"
        api_query = {}
        api_query.update({
            "name": name,
        })
        return self.call(api_path, query=api_query, **kwargs)

    def automation_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/automations"
        api_path = "/api/v2/automations.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def automation_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/automations"
        api_path = "/api/v2/automations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def automation_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/automations"
        api_path = "/api/v2/automations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def automation_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/automations"
        api_path = "/api/v2/automations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def automations_active_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/automations"
        api_path = "/api/v2/automations/active.json"
        return self.call(api_path, **kwargs)

    def automations_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/automations"
        api_path = "/api/v2/automations.json"
        return self.call(api_path, **kwargs)

    def bookmark_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/bookmarks"
        api_path = "/api/v2/bookmarks.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def bookmark_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/bookmarks"
        api_path = "/api/v2/bookmarks/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def bookmarks_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/bookmarks"
        api_path = "/api/v2/bookmarks.json"
        return self.call(api_path, **kwargs)

    def categories_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/categories"
        api_path = "/api/v2/categories.json"
        return self.call(api_path, **kwargs)

    def category_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/categories"
        api_path = "/api/v2/categories.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def category_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/categories"
        api_path = "/api/v2/categories/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def category_forums(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forums"
        api_path = "/api/v2/categories/{id}/forums.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def category_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/categories"
        api_path = "/api/v2/categories/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def category_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/categories"
        api_path = "/api/v2/category/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def channels_twitter_monitored_twitter_handle_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/monitored_twitter_handles"
        api_path = "/api/v2/channels/twitter/monitored_twitter_handles/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def channels_twitter_monitored_twitter_handles_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/monitored_twitter_handles"
        api_path = "/api/v2/channels/twitter/monitored_twitter_handles.json"
        return self.call(api_path, **kwargs)

    def channels_twitter_ticket_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/channels/twitter/tickets.json"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def channels_twitter_ticket_statuses(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/channels/twitter/tickets/{id}/statuses.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def channels_voice_availability_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/availabilities/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def channels_voice_availability_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/availabilities/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def channels_voice_greeting_categories_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/greeting_categories.json"
        return self.call(api_path, **kwargs)

    def channels_voice_greeting_category_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/greeting_category/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def channels_voice_greeting_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/greetings.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def channels_voice_greeting_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/greetings/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def channels_voice_greeting_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/greetings/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def channels_voice_greeting_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/greetings/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def channels_voice_greetings_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/greetings.json"
        return self.call(api_path, **kwargs)

    def channels_voice_phone_number_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/phone_numbers.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def channels_voice_phone_number_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/phone_numbers/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def channels_voice_phone_number_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/phone_numbers/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def channels_voice_phone_numbers_delete(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/phone_numbers.json"
        return self.call(api_path, method="DELETE", **kwargs)

    def channels_voice_phone_numbers_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/phone_numbers.json"
        return self.call(api_path, **kwargs)

    def channels_voice_phone_numbers_search(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/phone_numbers/search.json"
        return self.call(api_path, **kwargs)

    def channels_voice_stats_agents_activity_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/stats/agents_activity.json"
        return self.call(api_path, **kwargs)

    def channels_voice_stats_current_queue_activity_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/stats/current_queue_activity.json"
        return self.call(api_path, **kwargs)

    def channels_voice_stats_historical_queue_activity_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/voice-api/voice"
        api_path = "/api/v2/channels/voice/stats/historical_queue_activity.json"
        return self.call(api_path, **kwargs)

    def custom_roles_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/custom_roles"
        api_path = "/api/v2/custom_roles.json"
        return self.call(api_path, **kwargs)

    def dynamic_content_item_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/dynamic_content"
        api_path = "/api/v2/dynamic_content/items.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def dynamic_content_item_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/dynamic_content"
        api_path = "/api/v2/dynamic_content/items/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def dynamic_content_item_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/dynamic_content"
        api_path = "/api/v2/dynamic_content/items/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def dynamic_content_item_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/dynamic_content"
        api_path = "/api/v2/dynamic_content/items/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def dynamic_content_item_variant_create(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/dynamic_content"
        api_path = "/api/v2/dynamic_content/items/{id}/variants.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def dynamic_content_item_variant_delete(self, item_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/dynamic_content"
        api_path = "/api/v2/dynamic_content/items/{item_id}/variants/{id}.json"
        api_path = api_path.format(item_id=item_id, id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def dynamic_content_item_variant_show(self, item_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/dynamic_content"
        api_path = "/api/v2/dynamic_content/items/{item_id}/variants/{id}.json"
        api_path = api_path.format(item_id=item_id, id=id)
        return self.call(api_path, **kwargs)

    def dynamic_content_item_variant_update(self, item_id, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/dynamic_content"
        api_path = "/api/v2/dynamic_content/items/{item_id}/variants/{id}.json"
        api_path = api_path.format(item_id=item_id, id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def dynamic_content_item_variants(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/dynamic_content"
        api_path = "/api/v2/dynamic_content/items/{id}/variants.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def dynamic_content_item_variants_update_many_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/dynamic_content"
        api_path = "/api/v2/dynamic_content/items/{id}/variants/update_many.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def dynamic_content_items_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/dynamic_content"
        api_path = "/api/v2/dynamic_content/items.json"
        return self.call(api_path, **kwargs)

    def end_user_identity_create(self, user_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/end_users/{user_id}/identities.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def end_user_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/end_user"
        api_path = "/api/v2/end_users/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def end_user_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/end_user"
        api_path = "/api/v2/end_users/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def exports_tickets(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_export"
        api_path = "/api/v2/exports/tickets.json"
        return self.call(api_path, **kwargs)

    def exports_tickets_sample(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_export"
        api_path = "/api/v2/exports/tickets/sample.json"
        return self.call(api_path, **kwargs)

    def forum_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forums"
        api_path = "/api/v2/forums.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def forum_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forums"
        api_path = "/api/v2/forums/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def forum_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forums"
        api_path = "/api/v2/forums/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def forum_subscription_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forum_subscriptions"
        api_path = "/api/v2/forum_subscriptions.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def forum_subscription_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forum_subscriptions"
        api_path = "/api/v2/forum_subscriptions/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def forum_subscription_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forum_subscriptions"
        api_path = "/api/v2/forum_subscriptions/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def forum_subscriptions(self, forum_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forum_subscriptions"
        api_path = "/api/v2/forums/{forum_id}/subscriptions.json"
        api_path = api_path.format(forum_id=forum_id)
        return self.call(api_path, **kwargs)

    def forum_subscriptions_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forum_subscriptions"
        api_path = "/api/v2/forum_subscriptions.json"
        return self.call(api_path, **kwargs)

    def forum_topics(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/forums/{id}/topics.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def forum_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forums"
        api_path = "/api/v2/forums/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def forums_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forums"
        api_path = "/api/v2/forums.json"
        return self.call(api_path, **kwargs)

    def group_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/groups.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def group_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/groups/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def group_membership_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/group_memberships.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def group_membership_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/group_memberships/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def group_membership_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/group_memberships/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def group_memberships(self, group_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/groups/{group_id}/memberships.json"
        api_path = api_path.format(group_id=group_id)
        return self.call(api_path, **kwargs)

    def group_memberships_assignable(self, group_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/groups/{group_id}/memberships/assignable.json"
        api_path = api_path.format(group_id=group_id)
        return self.call(api_path, **kwargs)

    def group_memberships_assignable_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/group_memberships/assignable.json"
        return self.call(api_path, **kwargs)

    def group_memberships_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/group_memberships.json"
        return self.call(api_path, **kwargs)

    def group_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/groups/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def group_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/groups/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def group_users(self, id, permission_set=None, role=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/groups/{id}/users.json"
        api_path = api_path.format(id=id)
        api_query = {}
        if permission_set:
            api_query.update({
                "permission_set": permission_set,
            })
        if role:
            api_query.update({
                "role": role,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def groups_assignable_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/groups/assignable.json"
        return self.call(api_path, **kwargs)

    def groups_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/groups.json"
        return self.call(api_path, **kwargs)

    def help_center_article_attachment_create(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/article_attachments"
        api_path = "/api/v2/help_center/articles/{id}/attachments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def help_center_article_attachments(self, article_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/article_attachments"
        api_path = "/api/v2/help_center/articles/{article_id}/attachments.json"
        api_path = api_path.format(article_id=article_id)
        return self.call(api_path, **kwargs)

    def help_center_article_attachments_block(self, article_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/article_attachments"
        api_path = "/api/v2/help_center/articles/{article_id}/attachments/block.json"
        api_path = api_path.format(article_id=article_id)
        return self.call(api_path, **kwargs)

    def help_center_article_attachments_inline(self, article_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/article_attachments"
        api_path = "/api/v2/help_center/articles/{article_id}/attachments/inline.json"
        api_path = api_path.format(article_id=article_id)
        return self.call(api_path, **kwargs)

    def help_center_article_bulk_attachment_create(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/articles"
        api_path = "/api/v2/help_center/articles/{id}/bulk_attachments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def help_center_article_comment_create(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/comments"
        api_path = "/api/v2/help_center/articles/{id}/comments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def help_center_article_comment_delete(self, article_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/comments"
        api_path = "/api/v2/help_center/articles/{article_id}/comments/{id}.json"
        api_path = api_path.format(article_id=article_id, id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def help_center_article_comment_show(self, article_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/comments"
        api_path = "/api/v2/help_center/articles/{article_id}/comments/{id}.json"
        api_path = api_path.format(article_id=article_id, id=id)
        return self.call(api_path, **kwargs)

    def help_center_article_comment_update(self, article_id, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/comments"
        api_path = "/api/v2/help_center/articles/{article_id}/comments/{id}.json"
        api_path = api_path.format(article_id=article_id, id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def help_center_article_comments(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/comments"
        api_path = "/api/v2/help_center/articles/{id}/comments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def help_center_article_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/articles"
        api_path = "/api/v2/help_center/articles/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", status=204, **kwargs)

    def help_center_article_down_create(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/votes"
        api_path = "/api/v2/help_center/articles/{id}/down.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def help_center_article_label_create(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/labels"
        api_path = "/api/v2/help_center/articles/{id}/labels.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def help_center_article_label_delete(self, article_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/labels"
        api_path = "/api/v2/help_center/articles/{article_id}/labels/{id}.json"
        api_path = api_path.format(article_id=article_id, id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def help_center_article_labels(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/labels"
        api_path = "/api/v2/help_center/articles/{id}/labels.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def help_center_article_show(self, id, locale=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/articles"
        api_path = "/api/v2/help_center/articles/{id}.json"
        api_path = api_path.format(id=id)
        if locale:
            api_opt_path = "/api/v2/help_center/{locale}/articles/{id}.json"
            api_path = api_opt_path.format(id=id, locale=locale)
        return self.call(api_path, **kwargs)

    def help_center_article_source_locale_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/articles"
        api_path = "/api/v2/help_center/articles/{id}/source_locale.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def help_center_article_subscription_create(self, article_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/subscriptions"
        api_path = "/api/v2/help_center/articles/{article_id}/subscriptions.json"
        api_path = api_path.format(article_id=article_id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def help_center_article_subscription_delete(self, article_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/subscriptions"
        api_path = "/api/v2/help_center/articles/{article_id}/subscriptions/{id}.json"
        api_path = api_path.format(article_id=article_id, id=id)
        return self.call(api_path, method="DELETE", status=204, **kwargs)

    def help_center_article_subscription_show(self, article_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/subscriptions"
        api_path = "/api/v2/help_center/articles/{article_id}/subscriptions/{id}.json"
        api_path = api_path.format(article_id=article_id, id=id)
        return self.call(api_path, **kwargs)

    def help_center_article_subscriptions(self, article_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/subscriptions"
        api_path = "/api/v2/help_center/articles/{article_id}/subscriptions.json"
        api_path = api_path.format(article_id=article_id)
        return self.call(api_path, **kwargs)

    def help_center_article_translation_create(self, article_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/articles/{article_id}/translations.json"
        api_path = api_path.format(article_id=article_id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def help_center_article_translation_show(self, article_id, locale, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/articles/{article_id}/translations/{locale}.json"
        api_path = api_path.format(article_id=article_id, locale=locale)
        return self.call(api_path, **kwargs)

    def help_center_article_translation_update(self, article_id, locale, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/articles/{article_id}/translations/{locale}.json"
        api_path = api_path.format(article_id=article_id, locale=locale)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def help_center_article_translations(self, article_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/articles/{article_id}/translations.json"
        api_path = api_path.format(article_id=article_id)
        return self.call(api_path, **kwargs)

    def help_center_article_translations_missing(self, article_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/articles/{article_id}/translations/missing.json"
        api_path = api_path.format(article_id=article_id)
        return self.call(api_path, **kwargs)

    def help_center_article_up_create(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/votes"
        api_path = "/api/v2/help_center/articles/{id}/up.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def help_center_article_update(self, id, data, locale=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/articles"
        api_path = "/api/v2/help_center/articles/{id}.json"
        api_path = api_path.format(id=id)
        if locale:
            api_opt_path = "/api/v2/help_center/{locale}/articles/{id}.json"
            api_path = api_opt_path.format(id=id, locale=locale)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def help_center_article_votes(self, article_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/votes"
        api_path = "/api/v2/help_center/articles/{article_id}/votes.json"
        api_path = api_path.format(article_id=article_id)
        return self.call(api_path, **kwargs)

    def help_center_articles(self, locale, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/articles"
        api_path = "/api/v2/help_center/{locale}/articles.json"
        api_path = api_path.format(locale=locale)
        return self.call(api_path, **kwargs)

    def help_center_articles_attachment_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/article_attachments"
        api_path = "/api/v2/help_center/articles/attachments.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def help_center_articles_attachment_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/article_attachments"
        api_path = "/api/v2/help_center/articles/attachments/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def help_center_articles_attachment_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/article_attachments"
        api_path = "/api/v2/help_center/articles/attachments/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def help_center_articles_label_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/labels"
        api_path = "/api/v2/help_center/articles/labels/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def help_center_articles_labels_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/labels"
        api_path = "/api/v2/help_center/articles/labels.json"
        return self.call(api_path, **kwargs)

    def help_center_articles_list(self, label_names=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/articles"
        api_path = "/api/v2/help_center/articles.json"
        api_query = {}
        if label_names:
            api_query.update({
                "label_names": label_names,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def help_center_articles_search(self, category=None, label_names=None, locale=None, query=None, section=None, updated_after=None, updated_before=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/search"
        api_path = "/api/v2/help_center/articles/search.json"
        api_query = {}
        if category:
            api_query.update({
                "category": category,
            })
        if label_names:
            api_query.update({
                "label_names": label_names,
            })
        if locale:
            api_query.update({
                "locale": locale,
            })
        if query:
            api_query.update({
                "query": query,
            })
        if section:
            api_query.update({
                "section": section,
            })
        if updated_after:
            api_query.update({
                "updated_after": updated_after,
            })
        if updated_before:
            api_query.update({
                "updated_before": updated_before,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def help_center_categories(self, locale, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/categories"
        api_path = "/api/v2/help_center/{locale}/categories.json"
        api_path = api_path.format(locale=locale)
        return self.call(api_path, **kwargs)

    def help_center_categories_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/categories"
        api_path = "/api/v2/help_center/categories.json"
        return self.call(api_path, **kwargs)

    def help_center_category_articles(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/articles"
        api_path = "/api/v2/help_center/categories/{id}/articles.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def help_center_category_create(self, data, locale=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/categories"
        api_path = "/api/v2/help_center/categories.json"
        if locale:
            api_opt_path = "/api/v2/help_center/{locale}/categories.json"
            api_path = api_opt_path.format(locale=locale)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def help_center_category_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/categories"
        api_path = "/api/v2/help_center/categories/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def help_center_category_section_create(self, id, data, locale=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/sections"
        api_path = "/api/v2/help_center/categories/{id}/sections.json"
        api_path = api_path.format(id=id)
        if locale:
            api_opt_path = "/api/v2/help_center/{locale}/categories/{id}/sections.json"
            api_path = api_opt_path.format(id=id, locale=locale)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def help_center_category_sections(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/sections"
        api_path = "/api/v2/help_center/categories/{id}/sections.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def help_center_category_show(self, id, locale=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/categories"
        api_path = "/api/v2/help_center/categories/{id}.json"
        api_path = api_path.format(id=id)
        if locale:
            api_opt_path = "/api/v2/help_center/{locale}/categories/{id}.json"
            api_path = api_opt_path.format(id=id, locale=locale)
        return self.call(api_path, **kwargs)

    def help_center_category_source_locale_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/categories"
        api_path = "/api/v2/help_center/categories/{id}/source_locale.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def help_center_category_translation_create(self, category_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/categories/{category_id}/translations.json"
        api_path = api_path.format(category_id=category_id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def help_center_category_translation_update(self, category_id, locale, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/categories/{category_id}/translations/{locale}.json"
        api_path = api_path.format(category_id=category_id, locale=locale)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def help_center_category_translations(self, category_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/categories/{category_id}/translations.json"
        api_path = api_path.format(category_id=category_id)
        return self.call(api_path, **kwargs)

    def help_center_category_translations_missing(self, category_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/categories/{category_id}/translations/missing.json"
        api_path = api_path.format(category_id=category_id)
        return self.call(api_path, **kwargs)

    def help_center_category_update(self, id, data, locale=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/categories"
        api_path = "/api/v2/help_center/categories/{id}.json"
        api_path = api_path.format(id=id)
        if locale:
            api_opt_path = "/api/v2/help_center/{locale}/categories/{id}.json"
            api_path = api_opt_path.format(id=id, locale=locale)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def help_center_incremental_articles_list(self, start_time, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/articles"
        api_path = "/api/v2/help_center/incremental/articles.json"
        api_query = {}
        api_query.update({
            "start_time": start_time,
        })
        return self.call(api_path, query=api_query, **kwargs)

    def help_center_locales_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/locales.json"
        return self.call(api_path, **kwargs)

    def help_center_section_access_policy(self, section_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/access_policies"
        api_path = "/api/v2/help_center/sections/{section_id}/access_policy.json"
        api_path = api_path.format(section_id=section_id)
        return self.call(api_path, **kwargs)

    def help_center_section_access_policy_update(self, section_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/access_policies"
        api_path = "/api/v2/help_center/sections/{section_id}/access_policy.json"
        api_path = api_path.format(section_id=section_id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def help_center_section_article_create(self, id, data, locale=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/articles"
        api_path = "/api/v2/help_center/sections/{id}/articles.json"
        api_path = api_path.format(id=id)
        if locale:
            api_opt_path = "/api/v2/help_center/{locale}/sections/{id}/articles.json"
            api_path = api_opt_path.format(id=id, locale=locale)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def help_center_section_articles(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/articles"
        api_path = "/api/v2/help_center/sections/{id}/articles.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def help_center_section_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/sections"
        api_path = "/api/v2/help_center/sections/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def help_center_section_show(self, id, locale=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/sections"
        api_path = "/api/v2/help_center/sections/{id}.json"
        api_path = api_path.format(id=id)
        if locale:
            api_opt_path = "/api/v2/help_center/{locale}/sections/{id}.json"
            api_path = api_opt_path.format(id=id, locale=locale)
        return self.call(api_path, **kwargs)

    def help_center_section_source_locale_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/sections"
        api_path = "/api/v2/help_center/sections/{id}/source_locale.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def help_center_section_subscription_create(self, section_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/subscriptions"
        api_path = "/api/v2/help_center/sections/{section_id}/subscriptions.json"
        api_path = api_path.format(section_id=section_id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def help_center_section_subscription_delete(self, section_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/subscriptions"
        api_path = "/api/v2/help_center/sections/{section_id}/subscriptions/{id}.json"
        api_path = api_path.format(section_id=section_id, id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def help_center_section_subscription_show(self, section_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/subscriptions"
        api_path = "/api/v2/help_center/sections/{section_id}/subscriptions/{id}.json"
        api_path = api_path.format(section_id=section_id, id=id)
        return self.call(api_path, **kwargs)

    def help_center_section_subscriptions(self, section_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/subscriptions"
        api_path = "/api/v2/help_center/sections/{section_id}/subscriptions.json"
        api_path = api_path.format(section_id=section_id)
        return self.call(api_path, **kwargs)

    def help_center_section_translation_create(self, section_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/sections/{section_id}/translations.json"
        api_path = api_path.format(section_id=section_id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def help_center_section_translation_update(self, section_id, locale, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/sections/{section_id}/translations/{locale}.json"
        api_path = api_path.format(section_id=section_id, locale=locale)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def help_center_section_translations(self, section_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/sections/{section_id}/translations.json"
        api_path = api_path.format(section_id=section_id)
        return self.call(api_path, **kwargs)

    def help_center_section_translations_missing(self, section_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/sections/{section_id}/translations/missing.json"
        api_path = api_path.format(section_id=section_id)
        return self.call(api_path, **kwargs)

    def help_center_section_update(self, id, data, locale=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/sections"
        api_path = "/api/v2/help_center/sections/{id}.json"
        api_path = api_path.format(id=id)
        if locale:
            api_opt_path = "/api/v2/help_center/{locale}/sections/{id}.json"
            api_path = api_opt_path.format(id=id, locale=locale)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def help_center_sections(self, locale, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/sections"
        api_path = "/api/v2/help_center/{locale}/sections.json"
        api_path = api_path.format(locale=locale)
        return self.call(api_path, **kwargs)

    def help_center_sections_list(self, include=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/sections"
        api_path = "/api/v2/help_center/sections.json"
        api_query = {}
        if include:
            api_query.update({
                "include": include,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def help_center_translation_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/translations"
        api_path = "/api/v2/help_center/translations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def help_center_user_articles(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/articles"
        api_path = "/api/v2/help_center/users/{id}/articles.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def help_center_user_comments(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/comments"
        api_path = "/api/v2/help_center/users/{id}/comments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def help_center_user_subscriptions(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/subscriptions"
        api_path = "/api/v2/help_center/users/{user_id}/subscriptions.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def help_center_user_votes(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/votes"
        api_path = "/api/v2/help_center/users/{user_id}/votes.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def help_center_vote_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/votes"
        api_path = "/api/v2/help_center/votes/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def help_center_vote_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/help_center/votes"
        api_path = "/api/v2/help_center/votes/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def import_topic(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/import/topics.json"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def import_topic_comment(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/import/topics/{id}/comments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def imports_ticket(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_import"
        api_path = "/api/v2/imports/tickets.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def incremental_organizations_list(self, start_time=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/incremental_export"
        api_path = "/api/v2/incremental/organizations.json"
        api_query = {}
        if start_time:
            api_query.update({
                "start_time": start_time,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def incremental_ticket_events_list(self, start_time=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/incremental_export"
        api_path = "/api/v2/incremental/ticket_events.json"
        api_query = {}
        if start_time:
            api_query.update({
                "start_time": start_time,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def incremental_tickets_list(self, include=None, start_time=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/incremental_export"
        api_path = "/api/v2/incremental/tickets.json"
        api_query = {}
        if include:
            api_query.update({
                "include": include,
            })
        if start_time:
            api_query.update({
                "start_time": start_time,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def incremental_users_list(self, start_time=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/incremental_export"
        api_path = "/api/v2/incremental/users.json"
        api_query = {}
        if start_time:
            api_query.update({
                "start_time": start_time,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def job_status_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/job_statuses"
        api_path = "/api/v2/job_statuses/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def locale_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/locales"
        api_path = "/api/v2/locales/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def locales_agent_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/locales"
        api_path = "/api/v2/locales/agent.json"
        return self.call(api_path, **kwargs)

    def locales_current_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/locales"
        api_path = "/api/v2/locales/current.json"
        return self.call(api_path, **kwargs)

    def locales_detect_best_locale(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/locales"
        api_path = "/api/v2/locales/detect_best_locale.json"
        return self.call(api_path, **kwargs)

    def locales_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/locales"
        api_path = "/api/v2/locales.json"
        return self.call(api_path, **kwargs)

    def locales_public_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/locales"
        api_path = "/api/v2/locales/public.json"
        return self.call(api_path, **kwargs)

    def macro_apply(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros/{id}/apply.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def macro_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros.json"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def macro_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def macro_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def macro_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def macros_active_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros/active.json"
        return self.call(api_path, **kwargs)

    def macros_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros.json"
        return self.call(api_path, **kwargs)

    def oauth_client_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_clients"
        api_path = "/api/v2/oauth/clients.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def oauth_client_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_clients"
        api_path = "/api/v2/oauth/clients/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def oauth_client_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_clients"
        api_path = "/api/v2/oauth/clients/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def oauth_client_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_clients"
        api_path = "/api/v2/oauth/clients/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def oauth_clients_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_clients"
        api_path = "/api/v2/oauth/clients.json"
        return self.call(api_path, **kwargs)

    def oauth_token_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_tokens"
        api_path = "/api/v2/oauth/tokens/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def oauth_token_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_tokens"
        api_path = "/api/v2/oauth/tokens/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def oauth_tokens_current_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_tokens"
        api_path = "/api/v2/oauth/tokens/current.json"
        return self.call(api_path, **kwargs)

    def oauth_tokens_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_tokens"
        api_path = "/api/v2/oauth/tokens.json"
        return self.call(api_path, **kwargs)

    def organization_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def organization_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization_field_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_fields"
        api_path = "/api/v2/organization_fields.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def organization_field_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_fields"
        api_path = "/api/v2/organization_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization_field_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_fields"
        api_path = "/api/v2/organization_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organization_field_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_fields"
        api_path = "/api/v2/organization_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def organization_fields_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_fields"
        api_path = "/api/v2/organization_fields.json"
        return self.call(api_path, **kwargs)

    def organization_related(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/{id}/related.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organization_requests(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/organizations/{id}/requests.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organization_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organization_subscription_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_subscriptions"
        api_path = "/api/v2/organization_subscriptions.json"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_subscription_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_subscriptions"
        api_path = "/api/v2/organization_subscriptions/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization_subscription_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_subscriptions"
        api_path = "/api/v2/organization_subscriptions/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organization_subscriptions(self, organization_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_subscriptions"
        api_path = "/api/v2/organizations/{organization_id}/subscriptions.json"
        api_path = api_path.format(organization_id=organization_id)
        return self.call(api_path, **kwargs)

    def organization_subscriptions_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_subscriptions"
        api_path = "/api/v2/organization_subscriptions.json"
        return self.call(api_path, **kwargs)

    def organization_tag_create(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/organizations/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_tags(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/organizations/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organization_tags_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/organizations/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization_tags_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/organizations/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def organization_tickets(self, organization_id, external_id=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/organizations/{organization_id}/tickets.json"
        api_path = api_path.format(organization_id=organization_id)
        api_query = {}
        if external_id:
            api_query.update({
                "external_id": external_id,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def organization_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def organization_users(self, id, permission_set=None, role=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/organizations/{id}/users.json"
        api_path = api_path.format(id=id)
        api_query = {}
        if permission_set:
            api_query.update({
                "permission_set": permission_set,
            })
        if role:
            api_query.update({
                "role": role,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def organizations_autocomplete(self, name, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/autocomplete.json"
        api_query = {}
        api_query.update({
            "name": name,
        })
        return self.call(api_path, query=api_query, **kwargs)

    def organizations_create_many(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/create_many.json"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organizations_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations.json"
        return self.call(api_path, **kwargs)

    def organizations_search(self, external_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/search.json"
        api_query = {}
        api_query.update({
            "external_id": external_id,
        })
        return self.call(api_path, query=api_query, **kwargs)

    def portal_search(self, query, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/search"
        api_path = "/api/v2/portal/search.json"
        api_query = {}
        api_query.update({
            "query": query,
        })
        return self.call(api_path, query=api_query, **kwargs)

    def problems_autocomplete(self, text, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/problems/autocomplete.json"
        api_query = {}
        api_query.update({
            "text": text,
        })
        return self.call(api_path, query=api_query, method="POST", data=data, **kwargs)

    def problems_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/problems.json"
        return self.call(api_path, **kwargs)

    def recipient_address_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/support_addresses"
        api_path = "/api/v2/recipient_addresses.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def recipient_address_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/support_addresses"
        api_path = "/api/v2/recipient_addresses/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def recipient_address_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/support_addresses"
        api_path = "/api/v2/recipient_addresses/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def recipient_address_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/support_addresses"
        api_path = "/api/v2/recipient_addresses/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def recipient_address_verify(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/support_addresses"
        api_path = "/api/v2/recipient_addresses/{id}/verify.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def recipient_addresses_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/support_addresses"
        api_path = "/api/v2/recipient_addresses.json"
        return self.call(api_path, **kwargs)

    def request_comment_show(self, request_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/{request_id}/comments/{id}.json"
        api_path = api_path.format(request_id=request_id, id=id)
        return self.call(api_path, **kwargs)

    def request_comments(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/{id}/comments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def request_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def request_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def request_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def requests_ccd_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/ccd.json"
        return self.call(api_path, **kwargs)

    def requests_list(self, status=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests.json"
        api_query = {}
        if status:
            api_query.update({
                "status": status,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def requests_open_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/open.json"
        return self.call(api_path, **kwargs)

    def requests_search(self, cc_id=None, organization_id=None, query=None, status=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/search.json"
        api_query = {}
        if cc_id:
            api_query.update({
                "cc_id": cc_id,
            })
        if organization_id:
            api_query.update({
                "organization_id": organization_id,
            })
        if query:
            api_query.update({
                "query": query,
            })
        if status:
            api_query.update({
                "status": status,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def requests_solved_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/solved.json"
        return self.call(api_path, **kwargs)

    def satisfaction_rating_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/satisfaction_ratings"
        api_path = "/api/v2/satisfaction_ratings/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def satisfaction_ratings_list(self, score=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/satisfaction_ratings"
        api_path = "/api/v2/satisfaction_ratings.json"
        api_query = {}
        if score:
            api_query.update({
                "score": score,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def search(self, query, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/search"
        api_path = "/api/v2/search.json"
        api_query = {}
        api_query.update({
            "query": query,
        })
        return self.call(api_path, query=api_query, **kwargs)

    def sessions_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/sessions"
        api_path = "/api/v2/sessions.json"
        return self.call(api_path, **kwargs)

    def sharing_agreements_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/sharing_agreements"
        api_path = "/api/v2/sharing_agreements.json"
        return self.call(api_path, **kwargs)

    def suspended_ticket_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/suspended_tickets"
        api_path = "/api/v2/suspended_tickets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def suspended_ticket_recover(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/suspended_tickets"
        api_path = "/api/v2/suspended_tickets/{id}/recover.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def suspended_ticket_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/suspended_tickets"
        api_path = "/api/v2/suspended_tickets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def suspended_tickets_destroy_many(self, ids, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/suspended_tickets"
        api_path = "/api/v2/suspended_tickets/destroy_many.json"
        api_query = {}
        api_query.update({
            "ids": ids,
        })
        return self.call(api_path, query=api_query, method="DELETE", **kwargs)

    def suspended_tickets_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/suspended_tickets"
        api_path = "/api/v2/suspended_tickets.json"
        return self.call(api_path, **kwargs)

    def suspended_tickets_recover_many(self, ids, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/suspended_tickets"
        api_path = "/api/v2/suspended_tickets/recover_many.json"
        api_query = {}
        api_query.update({
            "ids": ids,
        })
        return self.call(api_path, query=api_query, method="PUT", data=data, **kwargs)

    def tags_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/tags.json"
        return self.call(api_path, **kwargs)

    def target_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/targets"
        api_path = "/api/v2/targets.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def target_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/targets"
        api_path = "/api/v2/targets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def target_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/targets"
        api_path = "/api/v2/targets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def target_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/targets"
        api_path = "/api/v2/targets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def targets_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/targets"
        api_path = "/api/v2/targets.json"
        return self.call(api_path, **kwargs)

    def ticket_audit_make_private(self, ticket_id, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_audits"
        api_path = "/api/v2/tickets/{ticket_id}/audits/{id}/make_private.json"
        api_path = api_path.format(ticket_id=ticket_id, id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def ticket_audit_show(self, ticket_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_audits"
        api_path = "/api/v2/tickets/{ticket_id}/audits/{id}.json"
        api_path = api_path.format(ticket_id=ticket_id, id=id)
        return self.call(api_path, **kwargs)

    def ticket_audits(self, ticket_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_audits"
        api_path = "/api/v2/tickets/{ticket_id}/audits.json"
        api_path = api_path.format(ticket_id=ticket_id)
        return self.call(api_path, **kwargs)

    def ticket_collaborators(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}/collaborators.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_comment_attachment_redact(self, ticket_id, comment_id, attachment_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/attachments"
        api_path = "/api/v2/tickets/{ticket_id}/comments/{comment_id}/attachments/{attachment_id}/redact.json"
        api_path = api_path.format(ticket_id=ticket_id, comment_id=comment_id, attachment_id=attachment_id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def ticket_comment_make_private(self, ticket_id, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_comments"
        api_path = "/api/v2/tickets/{ticket_id}/comments/{id}/make_private.json"
        api_path = api_path.format(ticket_id=ticket_id, id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def ticket_comment_redact(self, ticket_id, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_comments"
        api_path = "/api/v2/tickets/{ticket_id}/comments/{id}/redact.json"
        api_path = api_path.format(ticket_id=ticket_id, id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def ticket_comments(self, ticket_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_comments"
        api_path = "/api/v2/tickets/{ticket_id}/comments.json"
        api_path = api_path.format(ticket_id=ticket_id)
        return self.call(api_path, **kwargs)

    def ticket_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def ticket_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def ticket_field_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_fields"
        api_path = "/api/v2/ticket_fields.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def ticket_field_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_fields"
        api_path = "/api/v2/ticket_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def ticket_field_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_fields"
        api_path = "/api/v2/ticket_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_field_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_fields"
        api_path = "/api/v2/ticket_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def ticket_fields_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_fields"
        api_path = "/api/v2/ticket_fields.json"
        return self.call(api_path, **kwargs)

    def ticket_form_clone(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms/{id}/clone.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def ticket_form_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def ticket_form_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def ticket_form_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_form_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def ticket_forms_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms.json"
        return self.call(api_path, **kwargs)

    def ticket_forms_reorder(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms/reorder.json"
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def ticket_incidents(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}/incidents.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_macro_apply(self, ticket_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/tickets/{ticket_id}/macros/{id}/apply.json"
        api_path = api_path.format(ticket_id=ticket_id, id=id)
        return self.call(api_path, **kwargs)

    def ticket_mark_as_spam(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}/mark_as_spam.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def ticket_merge(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}/merge.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def ticket_metric_show(self, ticket_metric_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_metrics"
        api_path = "/api/v2/ticket_metrics/{ticket_metric_id}.json"
        api_path = api_path.format(ticket_metric_id=ticket_metric_id)
        return self.call(api_path, **kwargs)

    def ticket_metrics(self, ticket_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_metrics"
        api_path = "/api/v2/tickets/{ticket_id}/metrics.json"
        api_path = api_path.format(ticket_id=ticket_id)
        return self.call(api_path, **kwargs)

    def ticket_metrics_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_metrics"
        api_path = "/api/v2/ticket_metrics.json"
        return self.call(api_path, **kwargs)

    def ticket_related(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}/related.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_reset_sla_policy_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}/reset_sla_policy.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def ticket_satisfaction_rating_create(self, ticket_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/satisfaction_ratings"
        api_path = "/api/v2/tickets/{ticket_id}/satisfaction_rating.json"
        api_path = api_path.format(ticket_id=ticket_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def ticket_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_tag_create(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/tickets/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def ticket_tags(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/tickets/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_tags_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/tickets/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def ticket_tags_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/tickets/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def ticket_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def tickets_destroy_many(self, ids, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/destroy_many.json"
        api_query = {}
        api_query.update({
            "ids": ids,
        })
        return self.call(api_path, query=api_query, method="DELETE", **kwargs)

    def tickets_list(self, external_id=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets.json"
        api_query = {}
        if external_id:
            api_query.update({
                "external_id": external_id,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def tickets_mark_many_as_spam(self, ids, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/mark_many_as_spam.json"
        api_query = {}
        api_query.update({
            "ids": ids,
        })
        return self.call(api_path, query=api_query, method="PUT", data=data, **kwargs)

    def tickets_recent_list(self, external_id=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/recent.json"
        api_query = {}
        if external_id:
            api_query.update({
                "external_id": external_id,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def tickets_show_many(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/show_many.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def tickets_update_many_update(self, ids, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/update_many.json"
        api_query = {}
        api_query.update({
            "ids": ids,
        })
        return self.call(api_path, query=api_query, method="PUT", data=data, **kwargs)

    def topic_comment_create(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/topics/{id}/comments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def topic_comment_delete(self, topic_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/topics/{topic_id}/comments/{id}.json"
        api_path = api_path.format(topic_id=topic_id, id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def topic_comment_show(self, topic_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/topics/{topic_id}/comments/{id}.json"
        api_path = api_path.format(topic_id=topic_id, id=id)
        return self.call(api_path, **kwargs)

    def topic_comment_update(self, topic_id, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/topics/{topic_id}/comments/{id}.json"
        api_path = api_path.format(topic_id=topic_id, id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def topic_comments(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/topics/{id}/comments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def topic_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/topics.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def topic_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/topics/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def topic_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/topics/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def topic_subscription_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_subscriptions"
        api_path = "/api/v2/topic_subscriptions.json"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def topic_subscription_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_subscriptions"
        api_path = "/api/v2/topic_subscriptions/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def topic_subscription_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_subscriptions"
        api_path = "/api/v2/topic_subscriptions/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def topic_subscriptions(self, topic_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_subscriptions"
        api_path = "/api/v2/topics/{topic_id}/subscriptions.json"
        api_path = api_path.format(topic_id=topic_id)
        return self.call(api_path, **kwargs)

    def topic_subscriptions_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_subscriptions"
        api_path = "/api/v2/topic_subscriptions.json"
        return self.call(api_path, **kwargs)

    def topic_tag_create(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/topics/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def topic_tags(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/topics/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def topic_tags_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/topics/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def topic_tags_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/topics/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def topic_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/topics/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def topic_vote(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_votes"
        api_path = "/api/v2/topics/{id}/vote.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, status=404, **kwargs)

    def topic_vote_create(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_votes"
        api_path = "/api/v2/topics/{id}/vote.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def topic_vote_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_votes"
        api_path = "/api/v2/topics/{id}/vote.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def topic_votes(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_votes"
        api_path = "/api/v2/topics/{id}/votes.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def topics_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/topics.json"
        return self.call(api_path, **kwargs)

    def topics_show_many(self, ids, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/topics/show_many.json"
        api_query = {}
        api_query.update({
            "ids": ids,
        })
        return self.call(api_path, query=api_query, method="POST", data=data, **kwargs)

    def trigger_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def trigger_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def trigger_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def trigger_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def triggers_active_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers/active.json"
        return self.call(api_path, **kwargs)

    def triggers_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers.json"
        return self.call(api_path, **kwargs)

    def triggers_reorder(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers/reorder.json"
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def upload_create(self, data, filename=None, token=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/attachments"
        api_path = "/api/v2/uploads.json"
        api_query = {}
        if filename:
            api_query.update({
                "filename": filename,
            })
        if token:
            api_query.update({
                "token": token,
            })
        return self.call(api_path, query=api_query, method="POST", status=201, data=data, **kwargs)

    def upload_delete(self, token, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/attachments"
        api_path = "/api/v2/uploads/{token}.json"
        api_path = api_path.format(token=token)
        return self.call(api_path, method="DELETE", **kwargs)

    def user_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def user_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def user_field_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_fields"
        api_path = "/api/v2/user_fields.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def user_field_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_fields"
        api_path = "/api/v2/user_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def user_field_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_fields"
        api_path = "/api/v2/user_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def user_field_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_fields"
        api_path = "/api/v2/user_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def user_fields_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_fields"
        api_path = "/api/v2/user_fields.json"
        return self.call(api_path, **kwargs)

    def user_fields_reorder(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_fields"
        api_path = "/api/v2/user_fields/reorder.json"
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def user_forum_subscriptions(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forum_subscriptions"
        api_path = "/api/v2/users/{user_id}/forum_subscriptions.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_group_membership_create(self, user_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/users/{user_id}/group_memberships.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def user_group_membership_delete(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/users/{user_id}/group_memberships/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def user_group_membership_make_default(self, user_id, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/users/{user_id}/group_memberships/{id}/make_default.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def user_group_membership_show(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/users/{user_id}/group_memberships/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, **kwargs)

    def user_group_memberships(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/users/{user_id}/group_memberships.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_groups(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/users/{user_id}/groups.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_identities(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_identity_create(self, user_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def user_identity_delete(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def user_identity_make_primary(self, user_id, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities/{id}/make_primary"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def user_identity_show(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, **kwargs)

    def user_identity_update(self, user_id, id, identity_verified, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        api_query = {}
        api_query.update({
            "identity[verified]": identity_verified,
        })
        return self.call(api_path, query=api_query, method="PUT", data=data, **kwargs)

    def user_identity_verify(self, user_id, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities/{id}/verify"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def user_merge(self, user_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{user_id}/merge.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def user_organization_subscriptions(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_subscriptions"
        api_path = "/api/v2/users/{user_id}/organization_subscriptions.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_organizations(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/users/{user_id}/organizations.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_password_create(self, user_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{user_id}/password.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def user_password_update(self, user_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{user_id}/password.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def user_related(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{id}/related.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def user_requests(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/users/{id}/requests.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def user_session_delete(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/sessions"
        api_path = "/api/v2/users/{user_id}/sessions/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def user_session_show(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/sessions"
        api_path = "/api/v2/users/{user_id}/sessions/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, **kwargs)

    def user_sessions(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/sessions"
        api_path = "/api/v2/users/{user_id}/sessions.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_sessions_delete(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/sessions"
        api_path = "/api/v2/users/{user_id}/sessions.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def user_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def user_tickets_ccd(self, user_id, external_id=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/users/{user_id}/tickets/ccd.json"
        api_path = api_path.format(user_id=user_id)
        api_query = {}
        if external_id:
            api_query.update({
                "external_id": external_id,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def user_tickets_requested(self, user_id, external_id=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/users/{user_id}/tickets/requested.json"
        api_path = api_path.format(user_id=user_id)
        api_query = {}
        if external_id:
            api_query.update({
                "external_id": external_id,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def user_topic_comment_show(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/users/{user_id}/topic_comments/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, **kwargs)

    def user_topic_comments(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/users/{id}/topic_comments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def user_topic_subscriptions(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_subscriptions"
        api_path = "/api/v2/users/{user_id}/topic_subscriptions.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_topic_votes(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_votes"
        api_path = "/api/v2/users/{id}/topic_votes.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def user_topics(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/users/{id}/topics.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def user_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def users_autocomplete(self, name, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/autocomplete.json"
        api_query = {}
        api_query.update({
            "name": name,
        })
        return self.call(api_path, query=api_query, **kwargs)

    def users_create_many(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/create_many.json"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def users_list(self, permission_set=None, role=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users.json"
        api_query = {}
        if permission_set:
            api_query.update({
                "permission_set": permission_set,
            })
        if role:
            api_query.update({
                "role": role,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def users_me(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/me.json"
        return self.call(api_path, **kwargs)

    def users_me_merge(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/me/merge.json"
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def users_me_oauth_clients(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_clients"
        api_path = "/api/v2/users/me/oauth/clients.json"
        return self.call(api_path, **kwargs)

    def users_me_sessions_delete(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/sessions"
        api_path = "/api/v2/users/me/sessions.json"
        return self.call(api_path, method="DELETE", **kwargs)

    def users_search(self, external_id=None, query=None, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/search.json"
        api_query = {}
        if external_id:
            api_query.update({
                "external_id": external_id,
            })
        if query:
            api_query.update({
                "query": query,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def users_show_many(self, ids, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/show_many.json"
        api_query = {}
        api_query.update({
            "ids": ids,
        })
        return self.call(api_path, query=api_query, **kwargs)

    def view_count(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}/count.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def view_create(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views.json"
        return self.call(api_path, method="POST", status=201, data=data, **kwargs)

    def view_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def view_execute(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}/execute.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def view_export(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}/export.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def view_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def view_tickets(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}/tickets.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def view_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def views_active_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/active.json"
        return self.call(api_path, **kwargs)

    def views_compact(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/compact.json"
        return self.call(api_path, **kwargs)

    def views_count_many_list(self, ids, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/count_many.json"
        api_query = {}
        api_query.update({
            "ids": ids,
        })
        return self.call(api_path, query=api_query, **kwargs)

    def views_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views.json"
        return self.call(api_path, **kwargs)

    def views_preview(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/preview.json"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def views_preview_count(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/preview/count.json"
        return self.call(api_path, **kwargs)


