#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            k = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[k] = obj

    def save(self):
        m_dict = {}
        for k, v in self.__objects.items():
            m_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, mode='w+') as f:
            json.dump(m_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, mode='r') as f:
                something = json.load(f)
            for k, v in something.items():
                new = eval(v['__class__'])(**v)
                self.__objects[k] = new
        except FileNotFoundError:
            pass
