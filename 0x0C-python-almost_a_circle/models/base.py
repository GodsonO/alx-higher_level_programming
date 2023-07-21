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
    def from_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts."""
        if list_dictionaries is None or list_dictionaries == 0:
            return []
        return json.dumps(list_dictionaries)
