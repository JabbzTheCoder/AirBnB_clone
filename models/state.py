#!/usr/bin/python3
'''State class that inherits from that inherit from BaseModel'''
from .base_model import BaseModel

class State(BaseModel):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """
    name = ""