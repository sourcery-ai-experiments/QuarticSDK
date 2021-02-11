
import requests
from quartic_sdk.utilities.configuration import Configuration
from quartic_sdk.utilities.constants import * as Constants


class APIHelpers:
    """
    The class is the helper class which will be used for making the API calls
    """

    def __init__(self, host, username=None, password=None, oauth_token=None, verify_ssl=None):
        """
        Create API Client
        """
        self.configuration = Configuration.get_configuration(
            host, username, password, oauth_token, verify_ssl)

    def call_api(self, url, method_type, path_params=[], query_params={}, body={}):
        """
        Call the API at the given url
        :param: url:
        :param: method_type:
        :param: path_params:
        :param: query_params:
        :param: body:
        """
        assert method_type in METHOD_TYPES

        http_method_function_mapping = {
            Constants.API_GET: self.__http_get_api,
            Constants.API_POST: self.__http_post_api,
            Constants.API_PATCH: self.__http_patch_api,
            Constants.API_PUT: self.__http_put_api,
            Constants.API_DELETE: self.__http_delete_api
        }

        return http_method_function_mapping[method_type](url, path_params, query_params, body)

    def __http_get_api(self, url, path_params=[], query_params={}, body={}):
        """
        The method makes a GET call via the requests module
        :param: url:
        :param: path_params:
        :param: query_params:
        :param: body:
        """
        request_url = self.configuration.host + url
        for path_param in path_params:
            request_url += str(path_param) + "/"

        if self.configuration.auth_type == Constants.BASIC:
            return requests.get(request_url, auth=(
                self.configuration.username, self.configuration.password))
        elif self.configuration.auth_type == Constants.OAUTH:
            # TODO: Add oauth call
            return None

    def __http_post_api(self, url, path_params=[], query_params={}, body={}):
        """
        The method makes a POST call via the requests module
        :param: url:
        :param: path_params:
        :param: query_params:
        :param: body:
        """
        request_url = self.configuration.host + url
        for path_param in path_params:
            request_url += str(path_param) + "/"

        if self.configuration.auth_type == Constants.BASIC:
            headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
            return requests.post(request_url, auth=(
                self.configuration.username, self.configuration.password),
                data=body)
        elif self.configuration.auth_type == Constants.OAUTH:
            # TODO: Add oauth call
            return None

    def __http_patch_api(self, url, path_params=[], query_params={}, body={}):
        """
        The method makes a PATCH call via the requests module
        :param: url:
        :param: path_params:
        :param: query_params:
        :param: body:
        """
        raise NotImplementedError

    def __http_put_api(self, url, path_params=[], query_params={}, body={}):
        """
        The method makes a PUT call via the requests module
        :param: url:
        :param: path_params:
        :param: query_params:
        :param: body:
        """
        raise NotImplementedError

    def __http_delete_api(self, url, path_params=[], query_params={}, body={}):
        """
        The method makes a DELETE call via the requests module
        :param: url:
        :param: path_params:
        :param: query_params:
        :param: body:
        """
        raise NotImplementedError
