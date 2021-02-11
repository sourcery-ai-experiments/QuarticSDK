
import pandas as pd
import quartic_sdk.utilities.constants as Constants


class TagDataIterator:
    """
    The given class is the iterator class, which will be used to iterate
    for getting the tag data values at the given intervals
    """

    def __init__(self, tags, start_time, stop_time, count, api_helper, offset=0, granularity=0, return_type="json"):
        """
        We initialize the iterator with the given parameters
        :param tags: (BaseEntityList) Refers to the instance of BaseEntityList with
                each containing tags as the individual items
        :param start_time: (epoch) Start time of the query
        :param stop_time: (epoch) Stop time of the query
        :param count: Count of time ranges in this interval with each interval
                containing 2L points
        :param api_helper: (APIHelper) APIHelper class object
        :param offset: Current offset
        :param granularity: The granularity at which the tag data is queried
        """
        self.count = count
        self._offset = offset
        self.tags = tags
        self.start_time = start_time
        self.stop_time = stop_time
        self.api_helper = api_helper
        self.granularity = granularity
        self.return_type = return_type

    def create_post_data(self):
        """
        We create the required post data which will be used for making the POST call
        """
        return {
            "tags": [tag.id for tag in self.tags],
            "start_time": self.start_time,
            "stop_time": self.stop_time,
            "granularity": self.granularity
        }

    def __next__(self):
        """
        Get the next object in the iteration
        """
        if self._offset >= self.count:
            raise StopIteration
        body_json = self.create_post_data()
        tag_data_return = self.api_helper.call_api(
            Constants.POST_TAG_DATA, Constants.API_POST, query_params={"offset": self._offset}, body=body_json).json()
        self._offset += 1

        del tag_data_return['count']
        del tag_data_return['offset']

        if self.return_type != "json":
            tag_data_return_str = json.dumps(tag_data_return)

            tag_data_return = pd.read_json(tag_data_return_str,
                orient="split")

        return tag_data_return

    def __getitem__(self, key):
        """
        We override this method to get the object at the given key
        """
        if key >= self.count:
            raise IndexError
        body_json = self.create_post_data()
        tag_data_return = self.api_helper.call_api(
            Constants.POST_TAG_DATA, Constants.API_POST, query_params={"offset": key}, body=body_json).json()

        del tag_data_return['count']
        del tag_data_return['offset']

        if self.return_type != "json":
            tag_data_return_str = json.dumps(tag_data_return)

            tag_data_return = pd.read_json(tag_data_return_str,
                orient="split")

        return tag_data_return
