def test_get_hosts(connector):
    assert connector.get_hosts()


HOST = ('testhost.vmssoftware.com', '127.0.0.2')
ALIASES = ('testhost1', 'testhost2')


def test_add_host(connector):
    assert connector.add_host(*HOST, ALIASES)
    assert connector.delete_host(*HOST)


def test_edit_host(connector):
    assert connector.add_host(*HOST, ALIASES)
    assert connector.edit_host_aliases(*HOST, ['testhost-1', 'testhost-2'])
    assert connector.delete_host(*HOST)
