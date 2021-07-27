from pywebui.alerts import AlertType


def test_get_alerts(connector):
    assert connector.get_alerts(alert_type=AlertType.OPCOM)


def test_get_bookmarks(connector):
    assert connector.get_bookmarks()


def test_add_bookmarks(connector):
    alert = connector.get_alerts(alert_type=AlertType.OPCOM)[0]
    assert connector.add_bookmark(alert.id, AlertType.OPCOM)
    assert connector.get_bookmarks()


def test_delete_bookmarks(connector):
    bookmark = connector.get_bookmarks()
    assert connector.delete_bookmark(bookmark.id, AlertType.OPCOM)
    bookmarks = connector.get_bookmarks()
    assert len(filter(lambda b: b.id == bookmark.id, bookmarks)) == 0
