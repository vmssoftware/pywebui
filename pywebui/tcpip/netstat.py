from typing import List

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Connection(ResponseObject):
    """Connection object.

    Attributes:
        foreignAddress (str): the foreign address of connection.
        localAddress (str): the local address of connection.
        protocol (str): the protocol of connection.
        recieve (int): the received packets.
        send (int): the sent packets.
        state (str): the state of connection.
    """

class NetstatMethods:
    """Encapsulates methods for manage netstat."""
    def get_netstat(self) -> List[Connection]:
        """Returns the list of net statistics for active internet connections."""
        connections = []
        r = self.get(urls.API_GET_NETSTAT)
        if r.status_code == 200:
            for attrs in r.json():
                connections.append(Connection(attrs))
        else:
            message = r.json()
            raise ConnectorException(message['details'])

        return connections
