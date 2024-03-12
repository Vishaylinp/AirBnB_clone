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
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects.update({key: obj.to_dict()})

    def save(self):
        """serializes dictionary containing instance dictionary
           representations to JSOn file"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        """deserializes the JSON file to dictionary containing
           instance dictionary representations
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as jfile:
                FileStorage.__objects = json.load(jfile)
        else:
            return
