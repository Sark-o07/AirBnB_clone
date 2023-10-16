#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review


class FileStorage():
    """This is the abstracted storage engine.
    Attributes:
        __file_path: string_path to the JSON file (ex. file.json)
        __objects: a dict that stores all objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dict containing all objs."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets obj with class-id key in __objects (dict)."""
        obj_clsname = obj.__class__.__name__
        FileStorage.__objects[f"{obj_clsname}.{obj.id}"] = obj

    def save(self):
        """serializes the __objects (dict) to the JSON file."""
        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (dict)."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for o_dict in obj_dict.values():
                    clsname = o_dict["__class__"]
                    del o_dict["__class__"]
                    self.new(eval(clsname)(**o_dict))
        except FileNotFoundError:
            return
