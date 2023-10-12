#!/usr/bin/python3
"""This module contains the definition of the class BaseModel"""

from datetime import datetime
import json
import uuid


class BaseModel:
    """The base model for other classes in this project"""

    def __init__(self):
        """Initializes a newly instantiated BaseModel object
        Attributes:
            id (str): A unique id of the new instance
            created_at (datetime.datetime): the datetime the object was created
            updated_at (datetime.datetime): the datetime the object was updated
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a formatted string representation of the calling
        BaseModel instance
        """

        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute `updated_at`
        to the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a modified dict containing the attributes of the
        calling BaseModel instance
        """

        revised_dict = self.__dict__.copy()
        revised_dict.update({"__class__": type(self).__name__})
        revised_dict["created_at"] = self.created_at.isoformat()
        revised_dict["updated_at"] = self.updated_at.isoformat()

        return revised_dict
