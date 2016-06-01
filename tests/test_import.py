from __future__ import print_function


class TestImport(object):
    def setup(self):
        print("setup TestTickets")

    def teardown(self):
        print("teardown TestTickets")

    def test_import_module(self):
        try:
            import zdesk
        except (ImportError, SyntaxError):
            assert False

        assert True

    def test_import_class(self):
        try:
            from zdesk import Zendesk
        except (ImportError, SyntaxError):
            assert False

        assert True

    def test_import_get_id(self):
        try:
            from zdesk import get_id_from_url
        except (ImportError, SyntaxError):
            assert False

        assert True

