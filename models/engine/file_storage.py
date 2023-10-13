"""
This module contains a class for managing objects,
and persisting them to a JSON file.
The FileStorage class provides methods;
for adding, saving, and reloading objects.

Usage:
    To use this module,
    you can create an instance of the FileStorage class
    and use its methods to manage and persist objects to a JSON file.

Example:
    storage = FileStorage()
    obj = SomeObject()
    storage.new(obj)
    storage.save()
    storage.reload()

"""
import json


class FileStorage:
    """
    A class for managing objects and persisting them to a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): A dictionary to hold objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all stored objects.

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the storage.

        Args:
            obj: The object to be added.

        Returns:
            None
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        dictionary = self.all()
        dictionary[key] = obj.to_dict()

    def save(self):
        """
        Save the objects to the JSON file.

        Returns:
            None
        """
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Reload objects from the JSON file.

        If the file does not exist, it does nothing.

        Returns:
            None
        """
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
