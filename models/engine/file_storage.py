#!/usr/bin/python3
"""class that serializes instances to JSON file
   and deserializes JSON file to instances
"""
import json
import os.path
import datetime


class FileStorage():
    """serialize instance to JSON file and
       deserialize to instances from file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary containing dictionary
           representation of instances
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in dictionary a object
           wih key

           Args:
               obj (class instance): to store inside dictionary
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes dictionary containing instance dictionary
           representations to JSOn file"""
        obj_cpy = FileStorage.__objects
        obj_dict = {obj_id: obj_cpy[obj_id].to_dict() for obj_id in obj_cpy.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """deserializes the JSON file to dictionary containing
           instance dictionary representations
        """
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as json_file:
                obj_dict = json.load(json_file)
                for d in obj_dict.values():
                    class_name = d["__class__"]
                    del d["__class__"]
                    self.new(eval(class_name)(**d))
        except FileNotFoundError:
            return
