def test_netstat(connector):
    assert connector.get_netstat()