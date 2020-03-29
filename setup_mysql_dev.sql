-- script that prepares a MySQL server for the project --

-- Create database --

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create User --

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
       IDENTIFIED BY 'hbnb_dev_pwd';

-- Setting privileges of User --

GRANT ALL PRIVILEGES ON hbnb_dev_db.*
      to 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.*
      to 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
