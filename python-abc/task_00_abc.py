#!/usr/bin/python3
"""
Module defining an abstract Animal base class and its concrete subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to return the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Subclass representing a dog.
    """

    def sound(self):
        """
        Returns the sound made by a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass representing a cat.
    """

    def sound(self):
        """
        Returns the sound made by a cat.
        """
        return "Meow"
