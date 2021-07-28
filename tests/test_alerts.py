from pywebui.alerts import AlertType


def test_get_alerts(connector):
    assert connector.get_alerts(alert_type=AlertType.OPCOM)


def test_bookmarks(connector):
    alert = connector.get_alerts(alert_type=AlertType.OPCOM)[0]
    assert connector.add_bookmark(alert.id, AlertType.OPCOM)
    bookmarks = connector.get_bookmarks()
    assert bookmarks
    for bookmark in bookmarks:
        assert connector.delete_bookmark(bookmark.id, AlertType.OPCOM)
    assert len(connector.get_bookmarks()) == 0
