#!/usr/bin/python3

import models
from datetime import datetime
import uuid

class BaseModel():

    def __init__(self, *args, **kwargs):
        if (kwargs):
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['__class__'] = self.__class__.__name__        
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
