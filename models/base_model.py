#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime


class BaseModel:
    """Represents the base class for all other models."""

    def __init__(self):
        """Initialize a new BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__
        }

