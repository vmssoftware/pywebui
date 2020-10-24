from typing import List

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Package(ResponseObject):
    """Package object.

    Attributes:
        architecture (str): The base system name identifies both a hardware platform and an operating system.
        name (str): The product name.
        producer (str): The name of the company that owns the product.
        state (str): The state of the product.
        type (str): The type of product kit (full LP, operating system, mandatory update, partial, patch, platform, or transition).
        version (str): The version of product.
    """
    def __repr__(self):
        return f'{self.name}.{self.version}'


class PackageHistory(Package):
    """PackageHistory object.

    Attributes:
        architecture (str): The base system name identifies both a hardware platform and an operating system.
        date (int): The date of the operation (Unix Epoch format).
        dateStr (str): The date of the operation in string format.
        error (int): The number of error during the operation.
        name (str): The product name.
        operation (str): The operation name with product kit.
        producer (str): The name of the company that owns the product.
        type (str): The type of product kit (full LP, operating system, mandatory update, partial, patch, platform, or transition).
        validStatus	(dict): The validation code status object.
        username (str): The name of user who performed operation.
        version (str): The version of product.
    """


class InstalledPackagesMethods:
    """Encapsulates methods for manage packages."""

    def get_installed_packages(self) -> List[Package]:
        """Returns the list of installed packages on current node."""
        packages = []
        r = self.get(urls.API_GET_INSTALLED_PACKAGES)
        if r.status_code == 200:
            for attrs in r.json():
                packages.append(Package(attrs))

        return packages

    def get_package_history(self, product: str) -> List[PackageHistory]:
        """Returns the history of selected package on current node."""
        history = []
        r = self.get(urls.API_GET_INSTALLED_PACKAGE_HISTORY, product=product)
        if r.status_code == 200:
            for attrs in r.json():
                history.append(PackageHistory(attrs))
        elif r.status_code == 404:
            pass

        return history

    def export_package_history(self, product: str) -> str:
        """Exports the history of selected package on current node to text."""
        r = self.get(urls.API_EXPORT_INSTALLED_PACKAGE_HISTORY, product=product)

        if r.status_code == 200:
            return r.text
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_package(self, product: str) -> bool:
        """Deletes the selected package on current node."""
        pass
