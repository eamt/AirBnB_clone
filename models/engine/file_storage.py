#!/usr/bin/python3
"""FileStorage class"""

from models.base_model import BaseModel
import json
import models
import os.path


class FileStorage:
    """File storage """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return dict __objects"""
        return self.__objects

    def new(self, obj):
        """Save new object in  __objects"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serialize the content of  __objects to the JSON file"""
        json_dict = {}
        """ fill dictionary from __objects"""
        for key, value in FileStorage.__objects.items():
            json_dict[key] = FileStorage.__objects[key].to_dict()
            with open(self.__file_path, 'w') as f:
                f.write(json.dumps(json_dict))

    def reload(self):
        """Reload method"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.loads(f.read())
                for key, value in json_dict.items():
                    FileStorage.__objects[key] = eval(value[
                        '__class__'])(**value)
