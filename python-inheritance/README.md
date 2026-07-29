# Python - Inheritance

This repository contains tasks and exercises for learning Object-Oriented Programming (OOP) concepts in Python, specifically focused on **Inheritance**, Method Overriding, built-in functions (`isinstance`, `issubclass`, `type`, `super`), and custom object inspection.

## Files & Tasks

| File / Task Name | Description |
| ---------------- | ----------- |
| `0-lookup.py` | Returns the list of available attributes and methods of an object using `dir()`. |
| `1-my_list.py` | Custom class `MyList` inheriting from `list` with a method `print_sorted()` to print sorted elements. |
| `tests/1-my_list.txt` | Doctest suite covering `1-my_list.py`. |
| `2-is_same_class.py` | Function that returns `True` if an object is exactly an instance of the specified class. |
| `3-is_kind_of_class.py` | Function that returns `True` if an object is an instance of, or inherited from, the specified class. |
| `4-inherits_from.py` | Function that returns `True` if an object is an instance of a subclass of the specified class. |
| `5-base_geometry.py` | Defines an empty class `BaseGeometry`. |
| `6-base_geometry.py` | Expands `BaseGeometry` with a public instance method `area()` that raises an `Exception`. |
| `7-base_geometry.py` | Expands `BaseGeometry` with an `integer_validator(name, value)` method. |
| `tests/7-base_geometry.txt` | Doctest suite covering `7-base_geometry.py`. |
| `8-rectangle.py` | Class `Rectangle` inheriting from `BaseGeometry` with validated private `width` and `height`. |
| `9-rectangle.py` | Expands `Rectangle` with `area()` implementation and `__str__` representation. |
| `10-square.py` | Class `Square` inheriting from `Rectangle` with validated private `size`. |

## Requirements
* All files interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
* All Python scripts start with `#!/usr/bin/python3`.
* Code style complies with `pycodestyle` (version 2.7.*).
* Mandatory module, class, and function docstring documentation.

## Author
Luis Gonzalez - Holberton School San Juan, Puerto Rico
