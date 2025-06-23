-- contacts.sql
CREATE DATABASE contactDB;
USE contactDB;

CREATE TABLE contacts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  phone VARCHAR(15),
  email VARCHAR(100)
);
