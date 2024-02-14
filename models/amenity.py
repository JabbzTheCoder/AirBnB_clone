#!/usr/bin/python3
'''Amenity class that inherits from that inherit from BaseModel'''
from .base_model import BaseModel

class Amenity(BaseModel):
    '''Represents a Amenity
    Attributes:
        -name: name of amenity
    '''
    name = ""