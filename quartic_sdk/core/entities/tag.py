
from quartic_sdk.core.entities.base_entity import Base
from quartic_sdk.utilities.constants import * as Constants
from quartic_sdk.core.tag_data import TagDataIterator
from quartic_sdk.core.base_entity_list import BaseEntityList


class Tag(Base):
    """
    The given class refers to the tag entity which is created based upon the
    tag object returned from the API
    """

    def __str__(self):
        """
        Override the method to return the asset name with id
        """
        return f"{Constants.TAG_ENTITY}: {self.name}_{self.id}"

    def data(self, start_time, stop_time, granularity=0):
        """
        Get the data for the given tag between the start_time and the stop_time
        for the given granularity
        :param start_time: (epoch) Start_time for getting data
        :param stop_time: (epoch) Stop_time for getting data
        :param granularity: Granularity of the data
        :return: (DataIterator) DataIterator object which can be iterated to get the data
            between the given duration
        """
        body_json = {
            "tags": [self.id],
            "start_time": start_time,
            "stop_time": stop_time,
            "granularity": granularity
        }
        tag_data_response = self.api_helper.call_api(
            Constants.POST_TAG_DATA, Constants.API_POST, body=body_json)
        return TagDataIterator(BaseEntityList(Constants.TAG_ENTITY, [self]),
            start_time, stop_time, tag_data_response["count"], self.api_helper)

