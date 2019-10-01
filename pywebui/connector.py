import requests
from urllib.parse import urljoin

from . import urls

class User:
    def __init__(self, attrs):
        for attr, value in attrs.items():
            setattr(self, attr, value)

    def __repr__(self):
        return self.username

class ConnectorException(Exception): pass

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

    def get_user(self, username):
        url = urljoin(self.host, urls.API_GET_USER_DETAIL.format(username=username))
        r = self.session.get(url, cookies={'jwt': self.token})
        if r.status_code == 200:
            return User(r.json())

    def create_user(self, username, owner, password,uic, defprives, device, directory, pwd_expired, prives, account=None, flags=None):
        url = urljoin(self.host, urls.API_ADD_USER)

        data = {
            "account": account,
            "defprives": defprives,
            "device": device,
            "directory": directory,
            "flags": flags,
            "owner": owner,
            "password": password,
            "pwd_expired": pwd_expired,
            "prives": prives,
            "username": username,
            "uic": uic
        }

        if account:
            data['account'] = account

        if flags:
            data['flags'] = flags

        r = self.session.post(url, json=data, cookies={'jwt': self.token})

        if r.status_code == 200:
            return True # TODO: request and return created User
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message)

    def edit_user(self, username, **fields):
        url = urljoin(self.host, urls.API_EDIT_USER.format(username=username))

        r = self.session.put(url, json=fields, cookies={'jwt': self.token})

        if r.status_code == 200:
            return True # TODO: request and return created User
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message)

    def delete_user(self, username):
        url = urljoin(self.host, urls.API_DELETE_USER.format(username=username))

        r = self.session.delete(url, cookies={'jwt': self.token})

        if r.status_code == 200:
            return True
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message)

    def duplicate_user(self, username, new_username):
        url = urljoin(self.host, urls.API_DUPLICATE_USER.format(username=username))

        r = self.session.post(url, json={'new_user': new_username}, cookies={'jwt': self.token})

        if r.status_code == 200:
            return True # TODO: request and return created User
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message)

    def disable_user(self, username):
        url = urljoin(self.host, urls.API_DISABLE_USER.format(username=username))

        r = self.session.put(url, cookies={'jwt': self.token})

        if r.status_code == 200:
            return True
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message)

    def enable_user(self, username):
        url = urljoin(self.host, urls.API_ENABLE_USER.format(username=username))

        r = self.session.put(url, cookies={'jwt': self.token})

        if r.status_code == 200:
            return True
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message)