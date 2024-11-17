from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}

    def add(self, obj):
        self._storage[obj.id] = obj

    def get(self, obj_id):
        return self._storage.get(obj_id)

    def get_all(self):
        return list(self._storage.values())

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            obj.update(data)

    def delete(self, obj_id):
        if obj_id in self._storage:
            del self._storage[obj_id]
            
            
    def get_by_attribute(self, attr_name, attr_value):
        print(self)
        # Debugging: Print all objects in the repository
        print(self._storage)
        for obj in self._storage.values():
            print(attr_name)
            if hasattr(obj, attr_name):
                attr = getattr(obj, attr_name)
                # Compare values as needed
                if attr is not None:
                    if isinstance(attr, str):
                        if attr.lower() == attr_value.lower():  # Normalize the case
                            return obj
                    elif attr == attr_value:  # Direct comparison for other types
                        return obj
        return None