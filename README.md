# AirBnB Clone Command Interpreter

Welcome to the AirBnB clone project! This project aims to build a simplified version of the Airbnb website, focusing on creating a command-line interface to manage AirBnB objects.

## Project Description

The project is divided into multiple tasks, with the first task being the creation of a command interpreter. The command interpreter allows you to perform various operations on AirBnB objects, including creating, retrieving, updating, and deleting objects.

## Getting Started

To start the command interpreter, follow these steps:

1. Clone the repository:

2. Run the command interpreter:
## Using the Command Interpreter

Once you're in the command interpreter, you can use the following commands:

- `help`: Display a list of available commands and their descriptions.
- `quit`: Exit the command interpreter.

You can also perform various operations on AirBnB objects:

- `create <classname>`: Create a new instance of the specified class.
- `show <classname> <object_id>`: Display information about a specific object.
- `all [classname]`: Display information about all objects or objects of a specific class.
- `update <classname> <object_id> <attribute_name> "<attribute_value>"`: Update the specified attribute of an object.
## Examples

Here are some examples of how to use the command interpreter:

- To create a new User instance:
(hbnb) create User


- To display information about a User instance with the ID "user123":
(hbnb) show User user123


- To display information about all City instances:
(hbnb) all City


## Contributors

This project is the result of the collaborative efforts of the following contributors:

- @billwk254

Feel free to contribute and add your name to the list!

## Testing

To run unit tests, execute the following command:
python3 -m unittest discover tests