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
        """Returns the list of the JSON string representation json_string"""

        if json_string is None or len(json_string) == 0:
            json_string = "[]"

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                brand_new = cls(1, 1)
            else:
                brand_new = cls(1)

        brand_new.update(**dictionary)

        return brand_new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """

        D_filename = "{}.json".format(cls.__name__)
        D_list = []

        try:
            with open(D_filename, mode="r+", encoding="UTF-8") as f:
                r_json = f.read()
            output_list = cls.from_json_string(r_json)
            for i in output_list:
                D_list.append(cls.create(**i))
        except FileNotFoundError:
            pass
        return D_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes csv """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w+", newline="", encoding="UTF-8") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attributes = ["id", "width", "height", "x", "y"]
                else:
                    attributes = ["id", "size", "x", "y"]
                new_csvwrite = csv.DictWriter(f, fieldnames=attributes)
                for i in list_objs:
                    new_csvwrite.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Load csv data """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r+", newline="", encoding="UTF-8") as f:
                if cls.__name__ == "Rectangle":
                    attributes = ["id", "width", "height", "x", "y"]
                else:
                    attributes = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(f, fieldnames=attributes)
                dict_list = [dict([key, int(value)] for key,
                                  value in f.items())
                             for f in dict_list]
                return [cls.create(**argument) for argument in dict_list]
        except IOError:
            return []
