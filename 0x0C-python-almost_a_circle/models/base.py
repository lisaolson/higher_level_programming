#!/usr/bin/python3
"""Module to define Base Class
"""

import json


class Base:
    """Defines Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation with id
        Args:
            id (int): id value as integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries
        Args:
            size (int): size as integer value
        """
        if list_dictionaries is None:
            return "[]"
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to file
        Args:
            list_objs: list of instances who inherits Base
        """
        filename = cls.__name__ + ".json"
        json_list_objs = Base.to_json_string\
                       ([obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as f:
            f.write(json_list_objs)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of the JSON string representation json_string
        Args:
            json_string: string representing a list of dictionaries
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            **dictionary: double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns list of instances
        """
        new_list = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.read(from_json_string(f))
            new_list.append(instance_list)
        return new_list
