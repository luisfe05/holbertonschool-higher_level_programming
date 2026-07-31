#!/usr/bin/python3
"""
Contains State class and Base instance to link to the MySQL table states.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class mapped to the 'states' table in MySQL database.

    Attributes:
        id (int): Auto-generated unique integer primary key.
        name (str): State name string with max 128 chars, non-nullable.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
