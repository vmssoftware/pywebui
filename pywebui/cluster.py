from urllib.parse import urljoin

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Node(ResponseObject):
    def __repr__(self):
        return self.nodename


class ClusterMethods:
    def get_nodes(self):
        nodes = []
        r = self.get(urls.API_GET_NODES)
        if r.status_code == 200:
            for attrs in r.json():
                nodes.append(Node(attrs))

        return nodes
