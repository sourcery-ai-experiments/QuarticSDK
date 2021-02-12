
from quartic_sdk.core.entities.type_mapping import ENTITY_DICTIONARY
from quartic_sdk.core.iterators.entity_list_iterator import EntityListIterator


class EntityList:
    """
    The given class refers to the list of specific `class_type` of entity
    """

    def __init__(self, class_type, entities_list=[]):
        """
        We initialize the `BaseEntityList` based upon the class_type and the
        entities_list as passed by the user
        """
        self._class_type = class_type
        self._entities = []
        for entity_obj in entities_list:
            if self._validate_type(entity_obj):
                self._entities.append(entity_obj)

    def __repr__(self):
        """
        Return the representation of the entitylist
        """
        str_repr = "<EntityList: ["
        for entity_obj in self._entities:
            str_repr = str_repr + str(entity_obj) + ", "
        str_repr += "]>"
        return str_repr

    def __str__(self):
        """
        Return the stringified representation of the entitylist
        """
        return self.__repr__()

    def _validate_type(self, object):
        """
        We validate that the type of the object is the same as defined for the
        class definition
        """
        return isinstance(object, ENTITY_DICTIONARY[self._class_type])

    def get(self, name, value):
        """
        We return the entity with the given value for the name of the attribute
        """
        return [entity for entity in self._entities if getattr(entity, name) == value][0]

    def all(self):
        """
        We return the list of all entities for the given object
        """
        return self._entities

    def first(self):
        """
        Return the first element of the list
        """
        return self._entities[0]

    def last(self):
        """
        Return the last element of the list
        """
        return self._entities[-1]

    def count(self):
        """
        Returns the length of all entities
        """
        return len(self._entities)

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
            self._entities.append(instance)
        else:
            raise AssertionError(f"Can not add object, since it is not of {self._class_type} type")

    def exclude(self, name, value):
        """
        We return the EntityList after removing the entity with the attribute
        name having the value as above
        """
        updated_entities = [entity_obj for entity_obj in self._entities if getattr(entity_obj, name) != value]
        return EntityList(self._class_type, updated_entities)

    def __iter__(self):
        """
        We override the iterator to allow the user to iterate on the class
        """
        return EntityListIterator(self)

    def __getitem__(self, key):
        """
        Override the method to get the entity list value at the given index
        """
        return self._entities[key]

    def __eq__(self, other):
        """
        Check equality of two entity list objects
        """
        assert isinstance(other, BaseEntityList)
        return self.count() == other.count() and all(self[index] in other.all() for index in self.count())

    def __bool__(self):
        """
        Override to get the bool value of the class if required
        """
        return self.count() > 0
