-- Creates a database and a table with unique id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT PRIMARY KEY DEFAULT 1 UNIQUE NOT NULL,
    name VARCHAR(256) NOT NULL);
