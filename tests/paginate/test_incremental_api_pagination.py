import datetime

from zdesk import Zendesk

days_ago = 60
start_time = (datetime.datetime.now() - datetime.timedelta(days=days_ago)).timestamp()
incremental_api_page_size = 1000

def test_incremental_ticket_pagination(zd: Zendesk):
    response = zd.incremental_tickets_list(get_all_pages=True, cursor_pagination=False, start_time=start_time)
    time_pagination_tickets = response["tickets"]
    assert response["end_time"] > start_time
    assert response["end_of_stream"] is True
    assert len(time_pagination_tickets) > incremental_api_page_size

    response = zd.incremental_tickets_cursor_list(get_all_pages=True, cursor_pagination=False, start_time=start_time)
    cursor_pagination_tickets = response["tickets"]
    assert response["end_of_stream"] is True

    # time pagination provides some duplicates
    time_pagination_ticket_ids = {ticket["id"] for ticket in time_pagination_tickets}
    cursor_pagination_tickets_ids = {ticket["id"] for ticket in cursor_pagination_tickets}
    assert time_pagination_ticket_ids == cursor_pagination_tickets_ids
