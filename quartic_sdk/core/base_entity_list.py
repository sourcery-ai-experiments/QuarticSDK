
from quartic_sdk.core.base_entity import ENTITY_DICTIONARY


class BaseEntityListIterator:
    """
    The given class is the entity list iterator which will be used to iterate
    for the given list of entities
    """

    def __init__(self, base_entity_list):
        """
        Initialize the iterator. We set the current index as 0
        """
        self._base_entity_list = base_entity_list
        self._index = 0

    def __next__(self):
        """
        Return the subsequent iteration results starting from 0 as index
        """
        if len(base_entity_list.all()) > self._index:
            self._index +=1
            return base_entity_list[self._index]
        raise StopIteration


class BaseEntityList:
    """
    The given class refers to the list of specific `class_type` of entity
    """

    def __init__(self, class_type, entities_list=[]):
        """
        We initialize the `BaseEntityList` based upon the class_type and the
        entities_list as passed by the user
        """
        self.class_type = class_type
        self.entities = []
        for entity_obj in entities_list:
            if self._validate_type(class_type, entity_obj):
                self.entities.append(entity_obj)

    def _validate_type(self, object):
        """
        We validate that the type of the object is the same as defined for the
        class definition
        """
        return isinstance(object, ENTITY_DICTIONARY[self.class_type])

    def get(self, name, value):
        """
        We return the entity with the given value for the name of the attribute
        """
        return [entity for entity in self.entities_list if entity.name == value][0]

    def all(self):
        """
        We return the list of all entities for the given object
        """
        return self.entities

    def count(self):
        """
        Returns the length of all entities
        """
        return len(self.entities)

    def filter(self, condition):
        """
        We filter the entities based upon the given condition
        """
        raise NotImplementedError

    def add(self, instance):
        """
        We add the given object instance to the entities list of the class
        """
        if self._validate_type(instance):
            self.entities.append(instance)

    def __iter__(self):
        """
        We override the iterator to allow the user to iterate on the class
        """
        return BaseEntityListIterator(self)

    def __getitem__(self, key):
        """
        Override the method to get the entity list value at the given index
        """
        return self.entities[key]

    def __eq__(self, other):
        """
        Check equality of two entity list objects
        """
        assert isinstance(other, BaseEntityList)
        assert self.count() == other.count()
        return all(self[index] in other.all() for index in self.count())
