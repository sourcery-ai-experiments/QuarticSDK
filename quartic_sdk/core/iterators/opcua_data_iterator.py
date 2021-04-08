
import json
import pandas as pd
import quartic_sdk.utilities.constants as Constants
from quartic_sdk.core.iterators.tag_data_iterator import TagDataIterator


class OPCUADataIterator:
    """
    Thee given class is the iterator class for OPCUA data connector
    """

    def __init__(self,
        tags,
        start_time,
        stop_time,
        batch_size,
        api_helper,
        max_records=None,
        return_type=Constants.RETURN_JSON,
        transformations=[]):
        """
        We initialize the opcua iterator with the given parameters
        :param tags: (BaseEntityList) Refers to the instance of BaseEntityList with
                each containing tags as the individual items
        :param start_time: (epoch) Start time of the query
        :param stop_time: (epoch) Stop time of the query
        :param batch_size: Expected size of each batch
        :param api_helper: (APIHelper) APIHelper class object
        :param return_type: The param decides whether the data after querying will be
            json(when value is "json") or pandas dataframe(when value is "pd"). By default,
            it takes the value as "json"
        :param transformations: Refers to the list of transformations. It supports either
            interpolation or aggregation, depending upon which, we pass the value of this
            dictionary. An example value here is:
            [{
                "transformation_type": "interpolation",
                "column": "3",
                "method": "linear"
            }, {
                "transformation_type": "aggregation",
                "aggregation_column": "4",
                "aggregation_dict": {"3": "max"}
            }]
        """
        TagDataIterator.raise_exception_for_transformation_schema(
            transformations, tags)
        self.tags = tags
        self.start_time = start_time
        self.stop_time = stop_time
        self.batch_size = batch_size
        self.api_helper = api_helper
        self.granularity = granularity
        self.return_type = return_type

        self._transformations = transformations
        self._cursor = None
        self._data_call_state = 0

    def create_post_data(self):
        """
        The method creates the post data for the tag data call
        """
        return {
            "tags": [tag.name for tag in self.tags.all()],
            "start_time": self.start_time,
            "end_time": self.stop_time,
            "batch_size": self.batch_size,
            "transformations"
        }

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def
