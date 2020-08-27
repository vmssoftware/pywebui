from urllib.parse import urljoin

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class User(ResponseObject):
    def __repr__(self):
        return self.username


class UserMethods:
    def get_users(self):
        users = []
        r = self.get(urls.API_GET_USER_LIST)
        if r.status_code == 200:
            for attrs in r.json():
                users.append(User(attrs))

        return users

    def get_user(self, username):
        r = self.get(urls.API_GET_USER_DETAIL, username=username)
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

    def duplicate_user(self, username, new_username, uic):
        r = self.post(
            urls.API_DUPLICATE_USER,
            json={'new_user': new_username, "uic": uic},
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
