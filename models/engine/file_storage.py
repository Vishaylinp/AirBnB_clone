#!/usr/bin/python3
"""class that serializes instances to JSON file
   and deserializes JSON file to instances
"""
from models.base_model import BaseModel
import json
import os.path

class FileStorage(BaseModel):
    """serialize instance to JSON file and
       deserialize to instances from file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary containing dictionary
           representation of instances
        """
        return cls.__objects

    def new(self, obj):
        """sets in dictionary a object representation of instance
           wih key

           Args:
               obj (class instance): to store inside dictionary
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        cls.__objects.update({key: str(obj.to_dict())})

    def save(self):
        """serializes dictionary containing instance dictionary
           representations to JSOn file"""

        with open (__file_path, "w") as json_file:
            json.dump(cls.__objects, json_file)

    def reload(self):
        """deserializes the JSON file to dictionary containing
           instance dictionary representations
        """
        if os.path.exists(self.__file_path):
            with open(__file_path, 'r') as json_file:
                cls.__objects = json.load(json_file)
