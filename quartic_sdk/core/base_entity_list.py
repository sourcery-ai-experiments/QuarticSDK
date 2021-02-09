

class BaseEntityList:
    def __init__(self, class_type, entities_list=[]):
        """
        """
        self.class_type = class_type
        self.entities = []
        for entity_obj in entities_list:
            if self._validate_type(class_type, entity_obj):
                self.entities.append(entity_obj)

    def _validate_type(self, object):
        pass

    def get(self, name, value):
        return [entity for entity in self.entities_list if entity.name == value][0]

    def filter(self, condition):
        pass

    def add(self, instance):
        if self._validate_type(instance):
            self.entities.append(instance)

