#!/usr/bin/python3
"""
Module defining mixin classes for swimming and flying, and a Dragon class.
"""


class SwimMixin:
    """
    Mixin class providing swimming capability.
    """

    def swim(self):
        """
        Prints swimming capability message.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class providing flying capability.
    """

    def fly(self):
        """
        Prints flying capability message.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class inheriting swimming and flying capabilities from mixins.
    """

    def roar(self):
        """
        Prints roaring behavior of a dragon.
        """
        print("The dragon roars!")
