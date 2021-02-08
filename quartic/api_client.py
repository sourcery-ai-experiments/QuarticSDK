
from quartic.api.api_helpers import APIHelpers


class APIClient:

    def __init__(self, host, username=None, password=None, oauth_token=None, verify_ssl=None):
        """
        Create the API Client
        """
        self.api_helper = APIHelpers(host, username, password, oauth_token, verify_ssl)

    @staticmethod
    def version():
        """
        Return the SDK version
        """
        return VERSION

    def assets():
        """
        Get the assets method
        """
        pass

    def process_units():
        """
        Get the process units
        """
        pass

    def work_cells():
        """
        Get the work cells
        """
        pass

    def tags(self, asset_id):
        """
        Get the tags
        """
        pass
