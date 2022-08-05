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
        with open(self.__file_path, 'w', encoding='utf-8') as temp_file:
            json.dump(temp_dict, temp_file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as temp_file:
                temp_dict = json.load(temp_file)

            from models.base_model import BaseModel
            from models.user import User
            for key in temp_dict:
                if temp_dict[key]["__class__"] == "BaseModel":
                    self.__objects[key] = BaseModel(**temp_dict[key])
                if temp_dict[key]["__class__"] == "User":
                    self.__objects[key] = User(**temp_dict[key])
