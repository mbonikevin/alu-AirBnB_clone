# ALU AirBnB Clone

This project is a simplified clone of the AirBnB console application. It is part of the ALU curriculum and aims to help students understand the basics of object-oriented programming, file serialization, and building a command-line interface in Python.

## 📜 Project Description

The ALU AirBnB clone is a command-line interpreter that allows users to:
- Create new data models (e.g., users, places, reviews)
- Save these objects to a JSON file
- Retrieve, update, and destroy stored objects using commands

It follows the object-oriented programming paradigm and uses custom classes for each data model.

## ⚙️ How to Start the Command Interpreter

You must have Python 3.8.5 installed. On your machine:

./console.py

Make sure the script has execution permissions:
```chmod +x console.py

## 💡 How to Use

Once launched, the command interpreter supports the following syntax:

```create <class_name>```
Creates a new instance of the class

```show <class_name> <id>```
Prints the string representation of an instance

```destroy <class_name> <id>```
Deletes an instance

```all [<class_name>]```
Prints all string representations

```update <class_name> <id> <attribute_name> "<attribute_value>"```
Updates an instance

## 🔍 Examples

(hbnb) create User
(hbnb) show User 1234-5678-9101
(hbnb) destroy User 1234-5678-9101
(hbnb) update User 1234-5678-9101 email "user@example.com"

## 🧪 Testing

Run unit tests with:
```python3 -m unittest discover tests```
