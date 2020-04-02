#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


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

    # relationships
    reviews = relationship("Review",
                           backref="place",
                           cascade="all, delete-orphan")

    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def amenities(self):
            """Get and return a list of Amenity instances"""
            res = []
            for obj in amenity_ids:
                if obj.id == self.id:
                    res.append(obj)
            return res

        @amenities.setter
        def amenities(self, obj):
            """Add amenities to the amenity_ids obj"""
            if type(obj).__name__ == 'Amenity':
                self.amenity_ids.append(obj)

    elif getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def reviews(self):
            res = []
            for review in self.reviews:
                if review.place_id == self.id:
                    res.append(review)
            return(res)

        amenities = relationship("Amenity",
                                 secondary=place_amenity)
