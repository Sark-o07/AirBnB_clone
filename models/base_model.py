#!/usr/bin/python3
"""Defines the BaseModel class."""
from datetime import datetime
import models
from uuid import uuid4


class BaseModel():
    """The BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel.
        Args:
            *args(tup): unused.
            **kwargs(dict): key/value pairs of attributes.
        """
        t_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, t_form)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Return the str representation of the BaseModel instance."""
        clsname = self.__class__.__name__
        return f"[{clsname}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates 'updated_at' with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dict of all keys/values of the BaseModel instance."""

        r_dict = self.__dict__.copy()
        r_dict["__class__"] = self.__class__.__name__
        r_dict["created_at"] = self.created_at.isoformat()
        r_dict["updated_at"] = self.updated_at.isoformat()
        return r_dict
