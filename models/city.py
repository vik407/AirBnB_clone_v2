#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    # state_id = ""
    # name = ""
    # Fix: Table name cities

    __tablename__ = 'cities'

    name = Column(String(128),
                  nullable=False)

    state_id = Column(String(60),
                      ForeignKey('states.id'),
                      nullable=False)

    # FIX: relationship representation with class Place
    places = relationship("Place",
                          backref="cities",
                          cascade="all, delete-orphan")
