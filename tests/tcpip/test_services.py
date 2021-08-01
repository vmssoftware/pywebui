def test_get_services(connector):
    assert connector.get_services()


def test_get_service(connector):
    services = connector.get_services()
    assert connector.get_service(services[0].name)


def test_add_service(connector):
    assert connector.add_service(
        'testwebui',
        'testprocess',
        8888,
        'testuser',
        'testfile'
    )
    assert connector.delete_service('testwebui')


def test_edit_service(connector):
    assert connector.add_service(
        'testwebui',
        'testprocess',
        8888,
        'testuser',
        'testfile'
    )
    assert connector.edit_service('testwebui', port=8887)
    assert connector.delete_service('testwebui')