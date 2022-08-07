#!/usr/bin/python3
""" A module which defines FileStorage class.

"""
import json
import os


class FileStorage:
    """ Serializes and deserializes JSON file.

    Serializes instances to JSON file and deserializes JSON file
    to instances using the json module.

    Attributes:
        __file_path (str): Path to the JSON file
        __objects (dict): Store all objects by <classname.id>
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dict __objects """
        return self.__objects

    def new(self, obj):
        """ Adds obj to __objects dict.

        Args:
            obj (...): Object passed
        """
        key = type(obj).__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to JSON file """
        temp_dict = {}
        for key in self.__objects:
            temp_dict[key] = self.__objects[key].to_dict()
        json_string = json.dumps(temp_dict)
        with open(self.__file_path, 'w', encoding='utf-8') as temp_file:
            temp_file.write(json_string)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as temp_file:
                json_string = temp_file.read()
            temp_dict = json.loads(json_string)
            from models.base_model import BaseModel
            from models.user import User
            from models.place import Place
            from models.city import City
            from models.state import State
            from models.amenity import Amenity
            from models.review import Review
            for key, value in temp_dict.items():
                if value["__class__"] == "BaseModel":
                    self.__objects[key] = BaseModel(**value)
                elif value["__class__"] == "User":
                    self.__objects[key] = User(**value)
                elif value["__class__"] == "Place":
                    self.__objects[key] = Place(**value)
                elif value["__class__"] == "City":
                    self.__objects[key] = City(**value)
                elif value["__class__"] == "State":
                    self.__objects[key] = State(**value)
                elif value["__class__"] == "Amenity":
                    self.__objects[key] = Amenity(**value)
                elif value["__class__"] == "Review":
                    self.__objects[key] = Review(**value)
