#!/usr/bin/python3
""" File to handle db storage
"""

from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
# SQL Alchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
# OS getenv to return environment variables
from os import getenv


class DBStorage:
    """class DB Storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        mysql_user = getenv('HBNB_MYSQL_USER')
        mysql_password = getenv('HBNB_MYSQL_PWD')
        mysql_host = getenv('HBNB_MYSQL_HOST')
        mysql_database = getenv('HBNB_MYSQL_DB')
        # FIX: Create the engine  (self.__engine)
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(mysql_user, mysql_password,
                                              mysql_host, mysql_database),
                                      pool_pre_ping=True)
        # FIX: If test drop all tables
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    # FIX: Get the data
    def all(self, cls=None):
        """Get all data"""
        _dict = {}
        # FIX: if cls=None, query all types of objects
        # (User, State, City, Amenity, Place and Review)
        if cls is None:
            objs = []
            # FIX: classes imported then
            classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
            for names in classes:
                results = self.__session.query(eval(names))
                for res in results:
                    objs.append(res)
        else:
            objs = self.__session.query(cls).all()
        for obj in objs:
            # FIX: this method must return a dictionary: (like FileStorage)
            key = type(obj).__name__ + "." + str(obj.id)
            _dict[key] = obj
        return _dict

    # FIX: new(self, obj): add the object to the current
    # database session (self.__session)
    def new(self, obj):
        """Ad object to the database"""
        if obj:
            self.__session.add(obj)

    # FIX: save(self): commit all changes of the current
    # database session (self.__session)
    def save(self):
        """Commit changes to the database"""
        self.__session.commit()

    # FIX: delete(self, obj=None): delete from the current
    # database session obj if not None
    def delete(self, obj=None):
        """Delete from the database"""
        if obj:
            self.__session.delete(obj)

    # FIX: reload(self)
    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = session()
