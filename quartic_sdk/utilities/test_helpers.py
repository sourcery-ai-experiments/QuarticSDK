
class APIHelperCallAPI:
    """
    The class is used to mock the call API which in turn calls the `requests`
    get, post, patch, put and delete methods
    """

    def __init__(self, body_json):
        """
        We initialize the class
        """
        self._json = body_json

    def json(self):
        """
        The method is called in the actual implementation to get the json
        form of the response object
        """
        return self._json
