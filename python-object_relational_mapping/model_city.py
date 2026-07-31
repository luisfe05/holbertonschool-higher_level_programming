#!/usr/bin/python3
"""
Defines the City class to link to the MySQL table cities using SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class mapped to the 'cities' table in MySQL database.

    Attributes:
        id (int): Auto-generated unique integer primary key.
        name (str): City name string with max 128 chars, non-nullable.
        state_id (int): Foreign key to states.id, non-nullable.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
