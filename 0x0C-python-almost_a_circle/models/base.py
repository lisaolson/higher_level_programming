#!/usr/bin/python3


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#    def integer_validator(self, name, value):
 #       """Validates integers

  #      Args:
   #         name (str): name of class
    #        value (int): value to validate
     #   """
      #  if type(value) is not int:
       #     raise TypeError("{} must be an integer".format(name))
       # if value <= 0:
        #    raise ValueError("{} must be greater than 0".format(name))
