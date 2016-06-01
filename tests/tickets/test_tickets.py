from __future__ import print_function

from zdesk import get_id_from_url

class TestTickets(object):
    def setup(self):
        print("setup TestTickets")

    def teardown(self):
        print("teardown TestTickets")

    def test_ticket_ops(self, zd):
        new_ticket = {
            'ticket': {
                'requester_name': 'Howard Schultz',
                'requester_email': 'howard@starbucks.com',
                'subject':'My Starbucks coffee is cold!',
                'description': 'please reheat my coffee',
                'set_tags': 'coffee drinks',
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
        result = zd.ticket_create(data=new_ticket)

        ticket_id = get_id_from_url(result)

        # Show
        zd.ticket_show(id=ticket_id)

        tickets = zd.tickets_list(get_all_pages=True)

        # Delete
        zd.ticket_delete(id=ticket_id)

        assert(True)

