from typing import List
from urllib.parse import urljoin

from pywebui import urls
from pywebui.response import ResponseObject


class Node(ResponseObject):
    """Cluster node object.

    Attributes:
        boottime (int): the time when the node was booted (Unix Epoch format).
        csid (int): the CSID of the node.
        hardware (str): the model name string of the node.
        ip (str): the IP address of the node.
        nodename (str): the name of the node.
        online (str): the state of WebUI server (true - WebUI server started on this node, false - WebUI server isn't started on this node or isn’t installed, unknown - state of WebUI server unknown).
        os (str): the software version number of the OpenVMS operating system running on the node.
        status (str): the status of the node in cluster.
    """
    def __repr__(self):
        return self.nodename


class ClusterMethods:
    """Encapsulates methods for manage nodes."""

    def get_nodes(self) -> List[Node]:
        """Returns list of nodes."""
        nodes = []
        r = self.get(urls.API_GET_NODES)
        if r.status_code == 200:
            for attrs in r.json():
                nodes.append(Node(attrs))

        return nodes
