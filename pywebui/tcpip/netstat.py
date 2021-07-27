from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Netstat(ResponseObject):
    """Netstat object.

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
    def get_interface(self, name) -> Netstat:
        """Returns the list of net statistics for active internet connections."""
        r = self.get(urls.API_GET_NETSTAT)
        if r.status_code == 200:
            return Netstat(r.json())
        else:
            message = r.json()
            raise ConnectorException(message['details'])
