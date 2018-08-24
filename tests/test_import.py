def test_import_module():
    try:
        import zdesk
    except:
        assert False

    assert True

def test_import_class():
    try:
        from zdesk import Zendesk
    except:
        assert False

    assert True

def test_import_get_id():
    try:
        from zdesk import get_id_from_url
    except:
        assert False

    assert True

