import pytest
from zdesk import Zendesk


@pytest.fixture(scope='session')
def zd(request):
    try:
        # If a zdtestcfg exists, then prefer it because it has been
        # manually created just for test running.

        from zdtestcfg import testconfig
        config = testconfig
    except ImportError:
        try:
            import zdeskcfg

            # Create an object using the [zdesk] and [sandbox] sections of
            # ~/.zdeskcfg and the zdeskcfg module
            config = zdeskcfg.get_ini_config(section='sandbox')

            # It's possible that zdeskcfg is installed, but if the config
            # file does not exist or have a valid configuration, we should
            # not try to use it.
            if True not in map(bool, config.values()):
                config = {}

        except ImportError:
            config = {}

    if config:
        return Zendesk(**config)
    else:
        assert 0, 'No Zendesk configuration found.\n' \
                  'Create tests/zdtestcfg.py or install and configure zdeskcfg.'

