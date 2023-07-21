#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle

class Base:
    """Represent the base model."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

   @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list of objects): list of instances who inherits of Base
        """

        filename = "{}.json".format(cls.__name__)
        my_list = []

        if list_objs is not None:
            for each in list_objs:
                my_list.append(each.to_dictionary())

        json_list = cls.to_json_string(my_list)

        with open(filename, "w+", encoding="UTF-8") as f:
            f.write(json_list)
