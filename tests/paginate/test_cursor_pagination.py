import pytest

from zdesk import Zendesk

@pytest.fixture(scope="module", autouse=True)
def expected_ticket_count(zd: Zendesk):
    response = zd.tickets_count_list()
    count = response["count"]["value"]
    assert count >= 100, "Please create at least 100 tickets for this test to run"
    return count


def test_ticket_cursor_pagination(zd: Zendesk, expected_ticket_count: int):
    response = zd.tickets_list(get_all_pages=True)
    tickets = response["tickets"]
    assert len(tickets) == expected_ticket_count

def test_ticket_cursor_pagination_custom_page_size(zd: Zendesk, expected_ticket_count: int):
    response = zd.tickets_list(page_size=50, get_all_pages=True)
    tickets = response["tickets"]
    assert len(tickets) == expected_ticket_count


def test_ticket_offset_pagination(zd: Zendesk, expected_ticket_count: int):
    response = zd.tickets_list(per_page=100, get_all_pages=True, cursor_pagination=False)
    tickets = response["tickets"]
    assert len(tickets) == expected_ticket_count
