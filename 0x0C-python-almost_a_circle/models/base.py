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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Turns the dictionary representation of an instance into JSON
        Args:
            list_dictionaries (list): list of representations of an instances
        """
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(d) == dict for d in list_dictionaries)):
            raise TypeError("list_dictionaries must be in the dictionaries")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to file"""

        filename = "{}.json".format(cls.__name__)
        D_list = []

        if list_objs is not None:
            for i in list_objs:
                D_list.append(i.to_dictionary())

        json_list = cls.to_json_string(D_list)

        with open(filename, "w+", encoding="UTF-8") as f:
            f.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the Python version of a JSON string
        Args:
            json_string (str): string to turn into Python object
        """

        if json_string is None or len(json_string) == 0:
            json_string = "[]"

        return json.loads(json_string)
