import pytest

from zdesk import Zendesk, ZendeskError

@pytest.fixture(scope="module", autouse=True)
def expected_ticket_count(zd: Zendesk):
    response = zd.search_count(query="*")
    count = response["count"]
    assert count >= 100, "Please create at least 100 tickets for this test to run"
    return count


def test_search_offset_pagination(zd: Zendesk, expected_ticket_count: int):
    # Try to implement a way to return partial results.
    # This includes refactoring, because results are merged together at the end
    # of pagination.
    try:
        response = zd.search(query="*", get_all_pages=True, cursor_pagination=False)
    except ZendeskError as e:
        assert len(e.partial_results["results"]) == 1000
        assert e.partial_results["count"] == expected_ticket_count
    else:
        assert len(response["results"]) == expected_ticket_count

def test_search_with_cursor_pagination_is_unsupported(zd: Zendesk):
    with pytest.raises(ZendeskError) as e:
        zd.search(query="*", get_all_pages=True, cursor_pagination=True)
    
    assert e.value.partial_results is None