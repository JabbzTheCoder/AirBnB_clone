# AirBnB Clone - The Console

## Description
This project is part of a group project to create an AirBnB clone. The main objective is to build a command-line interface (CLI) to manage AirBnB objects such as users, states, cities, places, etc.

## Command Interpreter
The command interpreter allows users to interact with the AirBnB objects through a command-line interface. Here's how to get started and use it:

### How to Start
To start the command interpreter, execute the `console.py` script.

```bash
$ ./console.py
```

### How to Use
Once the command interpreter is running, you can use various commands to manage AirBnB objects. Here are some examples of supported commands:

- `create`: Create a new object.
- `show`: Show details of a specific object.
- `destroy`: Delete an object.
- `all`: Show all objects or objects of a specific type.
- `update`: Update attributes of an object.

### Examples
```bash
$ ./console.py
(hbnb) create User
b0c5eb59-fb5d-4e7a-8f9d-aa4b5d25e15f
(hbnb) show User b0c5eb59-fb5d-4e7a-8f9d-aa4b5d25e15f
[User] (b0c5eb59-fb5d-4e7a-8f9d-aa4b5d25e15f) {'id': 'b0c5eb59-fb5d-4e7a-8f9d-aa4b5d25e15f', 'created_at': '2024-02-08T12:00:00', 'updated_at': '2024-02-08T12:00:00'}
(hbnb) quit
$
```
