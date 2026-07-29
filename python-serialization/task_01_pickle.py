#!/usr/bin/python3
"""
Module for serializing and deserializing custom Python objects using pickle.
"""
import pickle


class CustomObject:
    """
    Represents a custom object with name, age, and student status attributes.
    """

    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initializes the CustomObject instance.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes in the required format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes current instance and saves to a file using pickle.

        Args:
            filename (str): Name of the file to save object to.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes instance of CustomObject from a pickle file.

        Args:
            filename (str): Name of the file containing pickled object.

        Returns:
            CustomObject or None: The deserialized instance or None.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
