#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from os import path
from models.base_model import BaseModel

class FileStorage():
    '''
    serializes instances to a JSON file and deserializes JSON file to instances
    Attributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
    Methods:
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file (path: __file_path)
    reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised) 
    '''
    __file_path =  "file.json"
    __objects = {}

    def all(self):
        '''
        returns the dictionary __objects
        '''
        return FileStorage.__objects
    
    def new(self, obj):
        '''
        Sets in __objects the obj with key <obj class name>.id
        '''
        FileStorage.__objects[obj.id] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(FileStorage.__file_path, "w") as file:
            obj_dict = {key: obj.to_dict() for key, obj in FileStorage.items()}
            json.dump(obj_dict, file)
    
    def reload(self):
        '''
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised) 
        '''
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    module = __import__("models." + class_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    obj_instance = class_(**value)
                    self.new(obj_instance)