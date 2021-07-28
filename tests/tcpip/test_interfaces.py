def test_get_interfaces(connector):
    assert connector.get_interfaces()


def test_get_interface(connector):
    interface = connector.get_interfaces()[0]
    assert connector.get_interface(interface.intf)
