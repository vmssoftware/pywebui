from urllib.parse import urljoin

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class License(ResponseObject):
    """
    License object.

    Attributes:
        active (int): The license loaded to memory or not (1 - license loaded to memory, 0 - license didn’t load to memory).
        activity (int): The license type – activity licenses, for layered products such as compilers (1 - activity license type).
        authorization (str): The string that helps identify the license.
        command (str): The command, which modified the license.
        hardwareID (str): The identification number of the hardware on which the product is licensed.
        issuer (str): The name of the company that issued the PAK for the product.
        modifiedByUser (str): The user, which modified license.
        modifiedOn (str): The date, when modified license.
        options (str): The list of license options from a PAK.
        pcl (int): The license type – per core licenses (PCL), which replaces per processor licenses (PPL). This type implements the licensing model on OpenVMS Integrity server systems. The PCL model licenses a product based on the number of active processor cores on the system (1 - per core license type).
        producer (str): The name of the company that owns the product for which you have a license.
        productName (str): The name of product with a license.
        releaseDate (str): The product release date such that the license authorizes use of all product versions released on or before the date.
        revisionLevel (int): The order number of license modification.
        status (str): The license status.
        terminationDate (str): The date on which the product license terminates.
        token (str): The product token.
        units (int): The number of license units from a PAK.
        version (int): The version limits from a PAK of the product for which you have a license.
    """
    def __repr__(self):
        return f'{self.productName}.{self.authorization}'


class LicenseHistory(License):
    """License history object."""
    def __repr__(self):
        return f'{self.productName}.{self.authorization}'


class LicenseMethods:
    """Encapsulates methods for manage licenses.

    Contains the same attributes as License object."""

    def get_all_licenses(self):
        licenses = []
        r = self.get(urls.API_GET_ALL_LICENSES_LIST)
        if r.status_code == 200:
            for attrs in r.json():
                licenses.append(License(attrs))

        return licenses

    def get_active_licenses(self):
        licenses = []
        r = self.get(urls.API_GET_ACTIVE_LICENSES_LIST)
        if r.status_code == 200:
            for attrs in r.json():
                licenses.append(License(attrs))

        return licenses

    def get_license(self, product, authorization):
        r = self.get(urls.API_GET_LICENSE, product=product, authorization=authorization)
        if r.status_code == 200:
            return License(r.json())
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def get_license_history(self, product, authorization):
        history = []
        r = self.get(urls.API_GET_LICENSE_HISTORY, product=product, authorization=authorization)
        if r.status_code == 200:
            for attrs in r.json():
                history.append(LicenseHistory(attrs))
        elif r.status_code == 404:
            pass

        return history

    def register_license(self, product, data):
        r = self.post(urls.API_REGISTER_LICENSE, product=product, json=data)
        if r.status_code == 200:
            return License(r.json())
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_license(self, product, authorization):
        r = self.delete(urls.API_DELETE_LICENSE, product=product, authorization=authorization)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_license_history(self, product, authorization):
        r = self.delete(urls.API_DELETE_LICENSE_HISTORY, product=product, authorization=authorization)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def export_license_history(self, product, authorization):
        r = self.get(urls.API_EXPORT_LICENSE_HISTORY, product=product, authorization=authorization)

        if r.status_code == 200:
            return r.text
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def enable_license(self, product, authorization):
        r = self.put(urls.API_ENABLE_LICENSE, product=product, authorization=authorization)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def disable_license(self, product, authorization):
        r = self.put(urls.API_DISABLE_LICENSE, product=product, authorization=authorization)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def load_license(self, product, authorization):
        r = self.post(urls.API_LOAD_LICENSE, product=product, authorization=authorization)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def unload_license(self, product, authorization):
        r = self.post(urls.API_UNLOAD_LICENSE, product=product, authorization=authorization)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])