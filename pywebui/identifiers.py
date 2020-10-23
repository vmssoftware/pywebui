from typing import List
from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Identifier(ResponseObject):
    """
    Identifier object.

    Attributes:
        GIDValue (str): The decimal value of group identifier (GID).
        name (str): The name of identifier.
        value (str): The hex value of identifier.
    """
    IDENTIFIER_TYPE = 'IDENTIFIER'
    GID_TYPE = 'GID'

    TYPES = [IDENTIFIER_TYPE, GID_TYPE]

    ATTRIBUTES = [
        'RESOURCE',
        'DYNAMIC',
        'NOACCESS',
        'SUBSYSTEM',
        'HOLDER_HIDDEN',
        'NAME_HIDDEN'
    ]

    def __repr__(self):
        return f'{self.name}={self.value}'


class Holder(ResponseObject):
    """
    Holder object.

    Attributes:
        attributes (list(str)): array of holder's attributes.
        holder (str): name of user (holder) who hold selected identifier
    """
    def __repr__(self):
        return f'{self.holder}'


class IdentifiersMethods:
    """Encapsulates methods for manage identifiers."""

    def get_identifiers(self) -> List[Identifier]:
        """Returns the list of rights identifiers without user UIC's."""
        identifiers = []
        r = self.get(urls.API_GET_IDENTIFIERS)
        if r.status_code == 200:
            for attrs in r.json():
                identifiers.append(Identifier(attrs))

        return identifiers

    def get_all_identifiers(self) -> List[Identifier]:
        """Returns the list of all rights identifiers."""
        identifiers = []
        r = self.get(urls.API_GET_ALL_IDENTIFIERS)
        if r.status_code == 200:
            for attrs in r.json():
                identifiers.append(Identifier(attrs))

        return identifiers

    def get_identifier(self, identifier: str) -> Identifier:
        """Returns identifier by name."""
        identifiers = self.get_all_identifiers()
        identifiers = list(filter(lambda i: i.name == identifier, identifiers))
        if identifiers:
            return identifiers[0]

    def get_identifier_holders(self, identifier: str) ->  List[Holder]:
        """Returns the list of users (holders) who hold selected identifier."""
        holders = []
        r = self.get(urls.API_GET_IDENTIFIER_HOLDERS, identifier=identifier)
        if r.status_code == 200:
            for attrs in r.json():
                holders.append(Holder(attrs))

        return holders

    def get_holder_identifiers(self, holder: str) -> List[Identifier]:
        """Returns the list of identifiers that are held by selected user (holder).

        User can hold one or more identifiers, or no identifiers.
        """
        identifiers = []
        r = self.get(urls.API_GET_HOLDER_IDENTIFIERS, holder=holder)
        if r.status_code == 200:
            data = r.json()
            if 'details' in data:
                return []
            for attrs in data:
                identifiers.append(Identifier(attrs))

        return identifiers

    def create_identifier(self, name: str, value: str, identifier_type: str = Identifier.IDENTIFIER_TYPE, attributes: List[str] = []) -> bool:
        """Creates the new identifier."""
        data = {
            "identName": name,
            "identValue":
                {
                    "value": value,
                    "type": identifier_type
                },
            "identAttrs": attributes
        }
        r = self.post(urls.API_CREATE_IDENTIFIER, json=data)
        if r.status_code == 200:
            return True
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_identifier(self, identifier) -> bool:
        """Deletes selected identifier."""
        r = self.delete(urls.API_DELETE_IDENTIFIER, identifier=identifier)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def grant_identifiers(self, username: str, identifiers: List[str]) -> bool:
        """Grants identifiers to user."""
        data = [{
            "username": username,
            "identifiers": identifiers
        }]
        r = self.put(urls.API_GRANT_IDENTIFIERS, json=data)
        if r.status_code == 200:
            return True
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message['details'])

    def rovoke_identifiers(self, username: str, identifiers: List[str]) -> bool:
        """Revokes identifiers from user."""
        data = [{
            "username": username,
            "identifiers": identifiers
        }]
        r = self.put(urls.API_REVOKE_IDENTIFIERS, json=data)
        if r.status_code == 200:
            return True
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message['details'])
