
from quartic_sdk.utilities.constants import POST_TAG_DATA


class TagDataIterator:

    def __init__(self, tags, start_time, stop_time, count, api_helper, offset=0, granularity=0):
        """
        """
        self.count = count
        self._offset = offset
        self.tags = tags
        self.start_time = start_time
        self.stop_time = stop_time
        self.api_helper = api_helper
        self.granularity = granularity

    def create_post_data(self):
        """
        """
        return {
            "tags": [tag.id for tag in self.tags],
            "start_time": self.start_time,
            "stop_time": self.stop_time,
            "granularity": self.granularity
        }

    def __next__(self):
        """
        """
        if self._offset >= self.count:
            raise StopIteration
        body_json = self.create_post_data()
        tag_data_return = self.api_helper.call_api(
            POST_TAG_DATA, "POST", query_params={"offset": self._offset}, body=body_json).json()
        self._offset += 1

        del tag_data_return['count']
        del tag_data_return['offset']

        return tag_data_return

    def __getitem__(self, key):
        """
        """
        if key >= self.count:
            raise IndexError
        body_json = self.create_post_data()
        tag_data_return = self.api_helper.call_api(
            POST_TAG_DATA, "POST", query_params={"offset": key}, body=body_json).json()

        del tag_data_return['count']
        del tag_data_return['offset']

        return tag_data_return
