#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), primary_key=True, nullable=False),
    Column('amenity_id', String(60), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    # FIX: Place to DBStorage
    """city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []"""

    # class attribute __tablename__
    __tablename__ = 'places'

    # class attribute city_id
    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)

    # class attribute user_id
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)

    # class attribute name
    name = Column(String(128),
                  nullable=False)

    # class attribute description
    description = Column(String(1024),
                         nullable=True)

    # class attribute number_rooms
    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)

    # class attribute number_bathrooms
    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)

    # class attribute max_guest
    max_guest = Column(Integer,
                       nullable=False,
                       default=0)

    # class attribute price_by_night
    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)

    # class attribute latitude
    latitude = Column(Float,
                      nullable=True)

    # class attribute longitude
    longitude = Column(Float,
                       nullable=True)

    # Relationship with review
    reviews = relationship("models.review.Review",
                            backref="place",
                            cascade="all, delete")
    
    # Getter of reviews
    @property
    def reviews(self):
        pass
        revs = []
        for review in self.reviews:
            if review.place_id == self.id:
                revs.append(review)
        return (_reviews)
