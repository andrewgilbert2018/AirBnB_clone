#!/usr/bin/python3
"""File Storage for the project"""
import json
from os.path import exists


class FileStorage:
    """Class for object FileStorage"""

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """dictionary __objects return"""
        return self.__objects

    def new(self, obj):
        """sets obj in __objects with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """__objects to JSON file serialize"""
        deb = dict()
        for keys in self.__objects.keys():
            deb[keys] = self.__objects[keys].to_dict()
        with open(self.__file_path, mode='w') as jsonfile:
            json.dump(deb, jsonfile)

    def reload(self):
        """the JSON file to __objects deserializes"""
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review

        if exists(self.__file_path):
            with open(self.__file_path) as jsonfile:
                ret = json.load(jsonfile)
            for keys in ret.keys():
                if ret[keys]['__class__'] == "BaseModel":
                    self.__objects[keys] = BaseModel(**ret[keys])
                elif ret[keys]['__class__'] == "User":
                    self.__objects[keys] = User(**ret[keys])
                elif ret[keys]['__class__'] == "State":
                    self.__objects[keys] = State(**ret[keys])
                elif ret[keys]['__class__'] == "City":
                    self.__objects[keys] = City(**ret[keys])
                elif ret[keys]['__class__'] == "Amenity":
                    self.__objects[keys] = Amenity(**ret[keys])
                elif ret[keys]['__class__'] == "Place":
                    self.__objects[keys] = Place(**ret[keys])
                elif ret[keys]['__class__'] == "Review":
                    self.__objects[keys] = Review(**ret[keys])
