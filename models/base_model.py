#!/usr/bin/python3
"""file contains the base class that defines all the common attributes
   and methods for other classes"""
import uuid
from datetime import datetime

class BaseModel():
    """the base class for all other classes"""
    def __init__(self):
        """instantiation of object"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """updates the public instance attribute
           updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all
           keys/values of __dict__ of the instance
        """
        self.__dict__["__class__"] = str(self.__class__.__name__)
        self.created_at = datetime.isoformat(self.created_at)
        self.updated_at = datetime.isoformat(self.updated_at)
        return self.__dict__

    def __str__(self):
        """print the class name, id and dictionary"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__)
