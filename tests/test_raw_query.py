import time

from zdesk import get_id_from_url

from zdesk_common import islocation, isstatuscode

def test_raw_query(zd):
    new_ticket = {
        'ticket': {
            'subject': 'zdesk raw_query ticket',
            'description': 'test ticket description',
            'tags': ['raw_query_test'],
        }
    }

    # create
    result = zd.ticket_create(data=new_ticket, retval='location')

    assert islocation(result), \
        'Create raw_query_test ticket response is not a location string'

    # get id from url
    ticket_id = get_id_from_url(result)

    assert ticket_id.isdigit(), \
        'Returned created raw_query_test ticket ID is not a string of decimal digits'

    response_query = zd.ticket_show(ticket_id, include='comment_count')
    response_raw = zd.ticket_show(ticket_id,
                                  raw_query='?include=comment_count',
                                  retval ='content')

    assert 'comment_count' in response_query['ticket'], \
        'query failed to include comment_count'
    
    assert 'comment_count' in response_raw['ticket'], \
        'raw_query failed to include comment_count'
    
    #    response_query = zd.search(query='tags:raw_query_test', retval='content')
    #
    #    # It can take a bit to populate the search index
    #    while len(response_query['results']) == 0:
    #        time.sleep(4)
    #        response_query = zd.search(query='tags:raw_query_test',
    #                                   retval='content')
    #
    #    response_raw = zd.search(raw_query='?query=tags:raw_query_test',
    #                             retval='content')
    #
    #    # It can take a bit to populate the search index
    #    while len(response_raw['results']) == 0:
    #        time.sleep(4)
    #        response_raw = zd.search(raw_query='?query=tags:raw_query_test',
    #                                 retval='content')
    #
    #    assert response_query['results'][0]['id'] == int(ticket_id), \
    #        'query search returned incorrect ticket'
    #
    #    assert response_raw['results'][0]['id'] == int(ticket_id), \
    #        'raw_query search returned incorrect ticket'
    #
    #    assert len(response_query['results']) == len(response_raw['results']), \
    #        'raw_query search contained different number of results' 
    #
    #    assert response_query['results'][0]['id'] == response_raw['results'][0]['id'], \
    #        'raw_query search returned different tickets' 

    # Delete
    result = zd.ticket_delete(ticket_id, retval='code')

    assert isstatuscode(result), \
        'Delete ticket raw_query_test response is not a status code string'

