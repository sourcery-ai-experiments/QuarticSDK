
from pprint import pprint
from quartic_sdk.core.base_entity import ENTITY_DICTIONARY
from quartic_sdk.core.base_entity_list import BaseEntityList


class EntityFactory:

    def __new__(cls, class_type, body, api_helper):
        """
        The method initializes a copy of the required entity based upon the
        passed parameters
        """
        if type(body) == list:
            return cls.follow_list_strategy(class_type, body, api_helper)
        return cls.follow_single_strategy(class_type, body, api_helper)

    @classmethod
    def follow_single_strategy(cls, class_type, body, api_helper):
        """
        The given method creates a new instance of the object as required
        based upon the class_type
        """
        return ENTITY_DICTIONARY[class_type](body, api_helper)

    @classmethod
    def follow_list_strategy(cls, class_type, body, api_helper):
        """
        The given method creates a new instance of BaseEntityList with
        the objects as required based upon the class_type
        """
        entities_list = BaseEntityList(class_type=class_type)
        for each_element in body:
            entities_list.add(ENTITY_DICTIONARY[class_type](each_element, api_helper))
        return entities_list
