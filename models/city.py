#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """City class that will be used to represent a city"""

    state_id = ""  # it will be the state.id
    name = ""
