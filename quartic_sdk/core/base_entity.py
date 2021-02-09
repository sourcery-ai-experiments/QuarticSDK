
from quartic_sdk.core.entity_factory import EntityFactory
from quartic_sdk.utilities.constants import (
    GET_TAGS,
    GET_BATCHES,
    GET_CONTEXT_FRAME_OCCURRENCES)


ENTITY_DICTIONARY = {
    "Asset": AssetEntity,
    "Tag": TagEntity,
    "ContextFrame": ContextFrameEntity,
    "ContextFrameOccurrence": ContextFrameOccurrenceEntity,
    "Batch": BatchEntity
}



class BaseEntity:
    """
    The base class which is used for creating all the required instances
    of specific types
    """

    def __init__(self, body_json, api_helper):
        """
        """
        for key in body_json:
            setattr(self, key, body_json[key])
        self.api_helper = api_helper

    def get(self, name):
        """
        """
        return getattr(self, name)


class AssetEntity(BaseEntity):

    def tags(self):
        tags_response = self.api_helper.call_api(
            GET_TAGS, "GET", self.id).json()
        return EntityFactory("Tag", tags_response, self.api_helper)

    def event_frames(self):
        raise NotImplementedError

    def batches(self):
        batches_response = self.api_helper.call_api(
            GET_BATCHES, "GET", self.id).json()
        return EntityFactory("Batch", batches_response, self.api_helper)

    def data(self):
        pass


class TagEntity(BaseEntity):

    def data(self):
        pass


class ContextFrameEntity(BaseEntity):

    def occurrences(self):
        occurrences_response = self.api_helper.call_api(
            GET_CONTEXT_FRAME_OCCURRENCES, "GET", self.id).json()
        return EntityFactory("ContextFrameOccurrence", occurrences_response, self.api_helper)


class ContextFrameOccurrenceEntity(BaseEntity):
    pass


class BatchEntity(BaseEntity):
    pass
