import requests
from urllib.parse import urljoin

from . import urls

class User:
    def __init__(self, attrs):
        for attr, value in attrs.items():
            setattr(self, attr, value)

    def __repr__(self):
        return self.username

class Connector:
    token = None
    def __init__(self, host):
        self.host = host
        self.session = requests.Session()

    def login(self, username, password):
        url = urljoin
        r = self.session.get(urljoin(self.host, urls.API_LOGIN), auth=(username, password))
        if r.status_code == 200:
            if 'jwt' in r.cookies:
                self.token = r.cookies['jwt']

    def get_users(self):
        users = []
        r = self.session.get(urljoin(self.host, urls.API_GET_USER_LIST), cookies={'jwt': self.token})
        if r.status_code == 200:
            for attrs in r.json():
                users.append(User(attrs))
        return users