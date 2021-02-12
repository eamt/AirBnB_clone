#!/usr/bin/python3
""" Define the Basemodel class """

import uuid
from datetime import datetime 


class BaseModel:
    """ Base class """
    def __init__(self, *args, **kwargs):
        """ Initialize public instance attributes """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                else:
                    setattr(self, key, value)

    def __str__(self):
        """ """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ save method """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ dictionaty method"""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
