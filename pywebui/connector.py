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

    def get(self, url, **query_params):
        url = urljoin(self.host, url.format(**query_params))
        response = self.session.get(url, cookies={'jwt': self.token})
        return response

    def post(self, url, json={}, **query_params):
        url = urljoin(self.host, url.format(**query_params))
        response = self.session.post(url, json=json, cookies={'jwt': self.token})
        return response

    def put(self, url, json={}, **query_params):
        url = urljoin(self.host, url.format(**query_params))
        response = self.session.put(url, json=json, cookies={'jwt': self.token})
        return response

    def delete(self, url, **query_params):
        url = urljoin(self.host, url.format(**query_params))
        response = self.session.delete(url, cookies={'jwt': self.token})
        return response

    def get_users(self):
        users = []
        r = self.get(urls.API_GET_USER_LIST)
        if r.status_code == 200:
            for attrs in r.json():
                users.append(User(attrs))

        return users

    def get_user(self, username):
        r = self.get(urls.API_GET_USER_DETAIL, username = username)
        if r.status_code == 200:
            return User(r.json())
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def create_user(self, username, owner, password, uic, defprives, device, directory, pwd_expired, prives, account=None, flags=None):
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

        r = self.post(urls.API_ADD_USER, json=data)

        if r.status_code == 200:
            return True # TODO: request and return created User
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def edit_user(self, username, **fields):
        r = self.put(urls.API_EDIT_USER, json=fields, username=username)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_user(self, username):
        r = self.delete(urls.API_DELETE_USER, username=username)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def duplicate_user(self, username, new_username):
        r = self.post(
            urls.API_DUPLICATE_USER,
            json={'new_user': new_username},
            username=username)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def disable_user(self, username):
        r = self.put(urls.API_DISABLE_USER, username=username)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def enable_user(self, username):
        r = self.put(urls.API_ENABLE_USER, username=username)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])