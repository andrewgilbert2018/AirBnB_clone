#!/bin/usr/python3
"""BaseModel File that defines attributes and methods"""

from models import storage
import uuid
from datetime import datetime


class BaseModel:

    """Class Base Model"""

    def __init__(self, *args, **kwargs):
        """initialization of items 
	in the BaseModel Class"""

        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Defining a class string method"""

        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):

        """An update class instance attribute
	 that update to the current time"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):

        """
	creates a dictionary of BaseModel 
	that returns its keys and key
	"""

        new_dictionary = dict(self.__dict__)
        new_dictionary['__class__'] = self.__class__.__name__
        new_dictionary['created_at'] = datetime.isoformat(self.created_at)
        new_dictionary['updated_at'] = datetime.isoformat(self.updated_at)
        return new_dictionary
