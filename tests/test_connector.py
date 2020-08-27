import pywebui


def test_constructor(hostname):
    c = pywebui.Connector(hostname)


def test_auth(connector):
    assert connector.token


def test_get_version(connector):
    assert connector.get_version()