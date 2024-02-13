#!/usr/bin/python3
'''User class that inherits from BaseModel'''
from .base_model import BaseModel

class User(BaseModel):
    '''
    User model that store hbnb users
    Attributes:
        -email: string - empty string
        -password: string - empty string
        -first_name: string - empty string
        -last_name: string - empty string

    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""