import requests
from urllib.parse import urljoin

from . import urls

class User:
    def __init__(self, attrs):
        for attr, value in attrs.items():
            setattr(self, attr, value)

    def __repr__(self):
        return self.username

class Process:
    def __init__(self, attrs):
        for attr, value in attrs.items():
            setattr(self, attr, value)

    def __repr__(self):
        return self.pid

class ConnectorException(Exception): pass

class UserMethods:
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

    def create_user(self, username, owner, password, uic, def_priv, device, directory, pwd_expired, priv, account=None, flags=None):
        url = urljoin(self.host, urls.API_ADD_USER)

        data = {
            "def_priv": def_priv,
            "device": device,
            "directory": directory,
            "owner": owner,
            "password": password,
            "pwd_expired": pwd_expired,
            "priv": priv,
            "username": username,
            "uic": uic
        }

        if account:
            data['account'] = account

        if flags:
            data['flags'] = flags

        r = self.post(urls.API_ADD_USER, json=data)

        if r.status_code == 200:
            return User(r.json())
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

class SystemMethods:
    def get_sysinfo(self):
        r = self.get(urls.API_GET_SYSTEM_INFO)

        if r.status_code == 200:
            return r.json()
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def get_resinfo(self):
        r = self.get(urls.API_GET_SYSTEM_RESOURCES)

        if r.status_code == 200:
            return r.json()
        else:
            message = r.json()
            raise ConnectorException(message['details'])

class ProcessMethods:
    def get_processes(self):
        processes = []
        r = self.get(urls.API_GET_PROCESS_LIST)
        if r.status_code == 200:
            for attrs in r.json():
                processes.append(Process(attrs))

        return processes

    def get_process(self, pid):
        r = self.get(urls.API_GET_PROCESS_DETAIL, pid=pid)
        if r.status_code == 200:
            return Process(r.json())
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def end_process(self, pid):
        r = self.post(urls.API_KILL_PROCESS, pid=pid)
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

class LicenseMethods:
    pass

class Connector(UserMethods, SystemMethods, ProcessMethods):
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