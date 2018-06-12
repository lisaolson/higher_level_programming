#!/usr/bin/python3
'''FileStorage class module'''

import json
from models.base_model import BaseModel


class FileStorage():
    '''FileStorage class'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets class.id key with obj value'''
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        '''serializes __objects to the JSON file'''
        '''turning __objects into dict'''
        mydict = {}
        for k, v  in __objects.items():
            mydict[k] = v.to_dict()
        with open(__file_path, mode='w+', encoding='utf-8') as f:
            json.dump(mydict, f)

    def reload(self):
        '''deserializes the JSON file to __objects if file exists'''
        try:
            with open(FileStorage.__file_path, mode='r') as f:
                jsond = json.load(f)
                for k, v in jsond.items():
                    newobj = eval(v['__class__'])(**v)
                    FileStorage.__objects[k] = newobj
        except FileNotFoundError:
            pass
