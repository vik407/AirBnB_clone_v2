#!/usr/bin/python3
"""test for databasse storage"""
import unittest
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
import MySQLdb
import pep8
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.engine.db_storage import DBStorage
from models import storage
import os
import MySQLdb


class TestDBStorage(unittest.TestCase):
    '''Class to test DB Storage'''

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "DB")
    def setUp(self):
        """Initialize the setup connection"""
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            self.db = MySQLdb.connect(os.getenv("HBNB_MYSQL_HOST"),
                                      os.getenv("HBNB_MYSQL_USER"),
                                      os.getenv("HBNB_MYSQL_PWD"),
                                      os.getenv("HBNB_MYSQL_DB"))
            self.cursor = self.db.cursor()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "DB")
    def tearDown(self):
        """Close db"""
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            self.db.close()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "DB")
    def test_attributes_DBStorage(self):
        """Check if has the attributes"""
        self.assertTrue(hasattr(DBStorage, '_DBStorage__engine'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__session'))
        self.assertTrue(hasattr(DBStorage, 'new'))
        self.assertTrue(hasattr(DBStorage, 'save'))
        self.assertTrue(hasattr(DBStorage, 'all'))
        self.assertTrue(hasattr(DBStorage, 'delete'))
        self.assertTrue(hasattr(DBStorage, 'reload'))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "DB")
    def test_pep8_DBStorage(self):
        """Check PEP8"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(pep.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
