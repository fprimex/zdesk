from zdesk import get_id_from_url

from zdesk_common import islocation, isstatuscode

def test_ticket_ops(zd):
    new_ticket = {
        'ticket': {
            'subject': 'zdesk test ticket',
            'description': 'test ticket description',
        }
    }

    # create
    result = zd.ticket_create(data=new_ticket)

    assert(islocation(result),
        'Create ticket response is not a location string')

    # get id from url
    ticket_id = get_id_from_url(result)

    assert(ticket_id.isdigit(),
        'Returned created ticket ID is not a string of decimal digits')

    # show
    result = zd.ticket_show(id=ticket_id)

    assert(isinstance(result, dict),
        'Show ticket response is not a dict')

    # list
    result = zd.tickets_list(get_all_pages=True)

    assert(isinstance(result, dict),
        'List tickets response is not a dict')

    assert(int(ticket_id) in [t['id'] for t in result['tickets']],
        'Created ticket not present in ticket list')

    # Delete
    result = zd.ticket_delete(id=ticket_id)

    assert(isstatuscode(result),
        'Delete ticket response is not a status code string')

