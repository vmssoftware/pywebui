def test_get_devices(connector):
    assert connector.get_devices()


def test_get_device(connector):
    devices = connector.get_devices()
    assert connector.get_device(devices[0].deviceSocket)
