#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    # Fix
    # Create table 'users'
    # email = ""
    # password = ""
    # first_name = ""
    # last_name = ""

    __tablename__ = 'users'

    email = Column(String(128),
                   nullable=False)
    password = Column(String(128),
                      nullable=False)
    first_name = Column(String(128),
                        nullable=True)
    last_name = Column(String(128),
                       nullable=True)

    # FIX: relationship representation with class Place
    places = relationship("Place",
                          backref="user",
                          cascade="all, delete-orphan")
