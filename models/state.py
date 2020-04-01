#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    # FIX: Add tablename, class attribute name
    __tablename__ = 'states'

    name = Column(String(128),
                  nullable=False)
    # FIX: for DBStorage: class attribute cities
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete-orphan")

    # FIX: for FileStorage with getter attribute
    if getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self):
            _list = []
            for _id, city in models.storage.all(City).items():
                if self.id == city.state_id:
                    _list.append(city)
            return _list
