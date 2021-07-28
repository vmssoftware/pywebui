from enum import Enum
from typing import List

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Alert(ResponseObject):
    """Alert object.

    Attributes:
        bookmark (bool): the message added to bookmarks or not (boolean value)
        id (int): the ID of message
        message (str): the text of message
        node (str): the node name where alert occurred
        timestamp (int): the time when alert occurred
    """

    def __repr__(self):
        return f"[{self.id}] {self.message}"


class Bookmark(Alert):
    """Bookmark object.

    Attributes:
        id (int): the ID of message
        message (str): the text of message
        node (str): the node name where alert occurred
        timestamp (int): the time when alert occurred
        type (str): the type of message.
        username (str): the username who added message to bookmarks
    """


class AlertType(Enum):
    """Available alert types."""

    OPCOM = "opcom"
    INTRUSIONS = "intrusions"
    DEVICES = "devices"


class AlertsMethods:
    """Encapsulates methods for manage alerts."""

    def get_alerts(self, alert_type: AlertType, limit: int = 30, after_id: int = -1, before_id: int = -1) -> List[Alert]:
        """Returns list of messages from operator console, list of intrusions and list of errors for disks."""
        alerts = []
        r = self.get(urls.API_GET_ALERTS,
                     type=alert_type.value,
                     limit=limit,
                     afterID=after_id,
                     beforeID=before_id)
        if r.status_code == 200:
            for attrs in r.json():
                alerts.append(Alert(attrs))

        return alerts

    def get_bookmarks(self) -> List[Bookmark]:
        """Returns messages which saved as bookmarks."""
        bookmarks = []
        r = self.get(urls.API_GET_BOOKMARKS)
        if r.status_code == 200:
            for attrs in r.json():
                bookmarks.append(Bookmark(attrs))

        return bookmarks

    def add_bookmark(self, alert_id: int, alert_type: AlertType) -> bool:
        """Adds message to bookmarks."""
        data = {
            'id': alert_id,
            'type': alert_type.value}

        r = self.post(urls.API_ADD_BOOKMARK, json=data)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_bookmark(self, alert_id: int, alert_type: AlertType) -> bool:
        """Deletes message which saved as bookmark."""
        data = [{'id': alert_id, 'type': alert_type.value}]

        r = self.delete(urls.API_DELETE_BOOKMARK, json=data)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])
