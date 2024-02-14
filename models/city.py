#!/usr/bin/python3
'''City class that inherits from that inherit from BaseModel'''
from .base_model import BaseModel

class City(BaseModel):
    '''
    City representation
    Attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    '''
    state_id = ""
    name = ""