
from quartic_sdk.utilities.constants import (
    GET_TAGS,
    GET_BATCHES,
    GET_CONTEXT_FRAME_OCCURRENCES)


class BaseEntity:
    """
    The base class which is used for creating all the required instances
    of specific types
    """

    def __init__(self, body_json, api_helper):
        """
        Initialize the given entity. As a part of the initialization, we set the keys
        of `body_json` as the attributes of the class
        :param body_json: Dict containing the body of the entity
        :param api_helper: APIHelper class instance containing configuration details
        """
        for key in body_json:
            setattr(self, key, body_json[key])
        self.api_helper = api_helper

    def get(self, name):
        """
        Return the value of the given `name` attribute
        :param name: (string) The attribute name to be returned
        :return: The returned attribute value
        """
        return getattr(self, name)

    def __eq__(self, other):
        """
        Override equals to check equality of all attributes
        :param other: The other object, to which we are comparing
        :return: (bool) Whether they are equal
        """
        assert isinstance(self, type(other))
        assert len(self.__dict__) == len(other.__dict__)
        return all(self.__dict__[key] == other.__dict__[key] for key in self.__dict__)


class AssetEntity(BaseEntity):
    """
    The given class refers to the asset entity which is created based upon the
    asset object returned from the API
    """

    def __str__(self):
        """
        Override the method to return the asset name with id
        """
        return f"Asset: {self.name}_{self.id}"

    def get_tags(self):
        """
        The given method returns the list of tags for the given asset
        """
        from quartic_sdk.core.entity_factory import EntityFactory
        tags_response = self.api_helper.call_api(
            GET_TAGS, "GET", [self.id]).json()
        return EntityFactory("Tag", tags_response, self.api_helper)

    def event_frames(self):
        """
        The given method returns the list of event frames for the given asset
        """
        raise NotImplementedError

    def batches(self):
        """
        The given method returns the list of batches for the given asset
        """
        from quartic_sdk.core.entity_factory import EntityFactory
        batches_response = self.api_helper.call_api(
            GET_BATCHES, "GET", self.id).json()
        return EntityFactory("Batch", batches_response, self.api_helper)

    def data(self, start_time, stop_time, granularity=0):
        """
        Get the data of all tags in th easset between the given start_time and
        stop_time for the given granularity
        :param start_time: (epoch) Start_time for getting data
        :param stop_time: (epoch) Stop_time for getting data
        :param granularity: Granularity of the data
        :return: (DataIterator) DataIterator object which can be iterated to get the data
            between the given duration
        """
        tags = self.tags()
        body_json = {
            "tags": [tag.id for tag in tags],
            "start_time": start_time,
            "stop_time": stop_time,
            "granularity": granularity
        }
        tag_data_response = self.api_helper.call_api(
            POST_TAG_DATA, "POST", body=body_json)
        return TagDataIterator(tags, start_time, stop_time, tag_data_response["count"], self.api_helper)


class TagEntity(BaseEntity):
    """
    The given class refers to the tag entity which is created based upon the
    tag object returned from the API
    """

    def __str__(self):
        """
        Override the method to return the asset name with id
        """
        return f"Tag: {self.name}_{self.id}"

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
            POST_TAG_DATA, "POST", body=body_json)
        return TagDataIterator(BaseEntityList("Tag", [self]),
            start_time, stop_time, tag_data_response["count"], self.api_helper)


class ContextFrameEntity(BaseEntity):
    """
    The given class refers to the context frame entity which is created based
    upon the context frame object returned from the API
    """

    def __str__(self):
        """
        Override the method to return the asset name with id
        """
        return f"ContextFrame: {self.id}"

    def occurrences(self):
        """
        Return the list of occurrences for the given context frame
        """
        from quartic_sdk.core.entity_factory import EntityFactory
        occurrences_response = self.api_helper.call_api(
            GET_CONTEXT_FRAME_OCCURRENCES, "GET", self.id).json()
        return EntityFactory("ContextFrameOccurrence", occurrences_response, self.api_helper)


class ContextFrameOccurrenceEntity(BaseEntity):
    """
    The given class refers to the context frame occurrence entity which is created
    based upon the context frame occurrence object returned from the API
    """
    def __str__(self):
        """
        Override the method to return the asset name with id
        """
        return f"ContextFrameOccurrence: {self.id}"


class BatchEntity(BaseEntity):
    """
    The given class refers to the batch entity which is created based upon the batch
    object returned from the API
    """

    def __str__(self):
        """
        Override the method to return the asset name with id
        """
        return f"Batch: {self.name}_{self.id}"


ENTITY_DICTIONARY = {
    "Asset": AssetEntity,
    "Tag": TagEntity,
    "ContextFrame": ContextFrameEntity,
    "ContextFrameOccurrence": ContextFrameOccurrenceEntity,
    "Batch": BatchEntity
}
