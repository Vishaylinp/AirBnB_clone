#!/usr/bin/python3
"""class that serializes instances to JSON file
   and deserializes JSON file to instances
"""
import json
import os.path

class FileStorage():
    """serialize instance to JSON file and
       deserialize to instances from file
    """
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}
        return classes

    def all(self):
        """return dictionary containing dictionary
           representation of instances
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in dictionary a object representation of instance
           wih key

           Args:
               obj (class instance): to store inside dictionary
        """
        id_key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[id_key] = obj

    def save(self):
        """serializes dictionary containing instance dictionary
           representations to JSOn file"""
        obj_copies = FileStorage.__objects.copy()

        for key, val in obj_copies.items():
            obj_copies[key] = val.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            json.dump(obj_copies, json_file)

    def reload(self):
        """deserializes the JSON file to dictionary containing
           instance dictionary representations
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as j_file:
                objs_dict = json.load(j_file)
                objs_dict = {id_key: self.classes()[inst["__class__"]](**inst)
                             for id_key, inst in objs_dict.items()}
                FileStorage.__objects = objs_dict
        else:
            return
