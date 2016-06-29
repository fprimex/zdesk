def test_import_module():
    try:
        import zdesk
    except (ImportError, SyntaxError):
        assert False

    assert True

def test_import_class():
    try:
        from zdesk import Zendesk
    except (ImportError, SyntaxError):
        assert False

    assert True

def test_import_get_id():
    try:
        from zdesk import get_id_from_url
    except (ImportError, SyntaxError):
        assert False

    assert True

