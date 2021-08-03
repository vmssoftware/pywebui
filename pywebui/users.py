from typing import List
from urllib.parse import urljoin

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class User(ResponseObject):
    """User object.

    Available fields described in Get User API documentation.
    """
    def __repr__(self):
        return self.username


class UserMethods:
    """Encapsulates methods for manage users."""

    def get_users(self) -> List[User]:
        """Returns list of users."""
        users = []
        r = self.get(urls.API_GET_USER_LIST)
        if r.status_code == 200:
            for attrs in r.json():
                users.append(User(attrs))

        return users

    def get_user(self, username) -> User:
        """Returns user details.

        Args:
            username (str): Username of requested user
        """
        r = self.get(urls.API_GET_USER_DETAIL, username=username)
        if r.status_code == 200:
            return User(r.json())
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def create_user(self, username: str, owner: str, password: str,
                    uic: List[str], def_priv: List[str], device: str,
                    directory: str, pwd_expired: bool, priv: List[str],
                    account: str=None, flags: List[str]=None) -> User:
        """Creates user.

        Args:
            def_priv: default privileges for the user.
            device: the name of the user's default device at login (30 alphanumeric characters maximum).
            directory: the default directory name (39 alphanumeric characters maximum).
            owner: the name of the owner of the account (31 characters maximum).
            password: passwords for login (8 alphanumeric characters minimum, length to 32 alphanumeric characters. The dollar sign ( $ ) and underscore ( _ ) are also permitted).
            priv: privileges the user is authorized to hold.
            uic: the user identification code (UIC) (it’s in octal, don't use digits 8 and 9 for UIC).
            username: the user name (12 symbols maximum - alphanumeric characters. The dollar sign ( $ ) and underscore ( _ ) are also permitted).
            account: the account name of the user (8 symbols maximum - alphanumeric characters and underscores).

        Keyword Args:
            flags: login flags for the user.
            pwd_expired: primary password is pre-expired (false is not pre-expired or true is pre-expired).

        Example:
            ::

                connector.create_user(
                    username="testuser",
                    owner="testowner",
                    password="asd123asd123",
                    uic=("312", "77"),
                    def_priv=["NETMBX","TMPMBX"],
                    device="SYS$SYSDEVICE",
                    directory="[testuser1]",
                    pwd_expired=False,
                    priv=["NETMBX","TMPMBX"],
                    flags=["DISUSER"],
                    # account = "testusr1",
                )
        """

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

    def edit_user(self, username: str, **fields) -> bool:
        """Change user attributes.

        User attributes available for changing listed in `create_user()` method.
        Pass corresponding attribute as keyword argument.

        Args:
            username (str): Username of requested user

        Example:
            >>> c = pywebui.Connector('http://11.12.132.21:8082')
            >>> c.login('testuser', 'testuser')
            >>> c.edit_user('user1', owner = "owner1")
        """
        r = self.put(urls.API_EDIT_USER, json=fields, username=username)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_user(self, username) -> bool:
        """Deletes user."""
        r = self.delete(urls.API_DELETE_USER, username=username)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def duplicate_user(self, username, new_username, uic) -> bool:
        """Duplicates user `username` to user with name `new_username`."""
        r = self.post(
            urls.API_DUPLICATE_USER,
            json={'new_user': new_username, "uic": uic},
            username=username)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def disable_user(self, username) -> bool:
        """Disables user."""
        r = self.put(urls.API_DISABLE_USER, username=username)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def enable_user(self, username) -> bool:
        """Enabled user."""
        r = self.put(urls.API_ENABLE_USER, username=username)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])
