#!/usr/bin/python3
"""test for user"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
import pep8
import MySQLdb


class TestUser(unittest.TestCase):
    """this will test the User class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kevin"
        cls.user.last_name = "Yook"
        cls.user.email = "yook00627@gmamil.com"
        cls.user.password = "secret"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_User(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_User(self):
        """checking for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes_User(self):
        """chekcing if User have attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_is_subclass_User(self):
        """test if User is subclass of Basemodel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types_User(self):
        """test attribute type for User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "DB")
    def test_save_User(self):
        """test if the save works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "DB")
    def test_to_dict_User(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.user), True)

    # MySQL tests
    # Start connection
    def connection(self):
        """ Connect to db """
        # Getting environment variables
        mysql_user = os.getenv('HBNB_MYSQL_USER')
        mysql_password = os.getenv('HBNB_MYSQL_PWD')
        mysql_host = os.getenv('HBNB_MYSQL_HOST')
        mysql_database = os.getenv('HBNB_MYSQL_DB')
        # Connection
        conn = MySQLdb.connect(host=mysql_host,
                               port=3306,
                               user=mysql_user,
                               passwd=mysql_password,
                               db=mysql_database,
                               charset="utf8")
        return conn

    def test_to_user_attributes(self):
        """ Test user attributes on db """
        conn = self.connection()
        cur = conn.cursor()
        current = cur.execute("SELECT * FROM users")
        new = User()
        cur.close()
        cur = conn.cursor()
        after = cur.execute("SELECT * FROM users")
        self.assertEqual(current, after)
        cur.close()
        conn.close()

if __name__ == "__main__":
    unittest.main()
