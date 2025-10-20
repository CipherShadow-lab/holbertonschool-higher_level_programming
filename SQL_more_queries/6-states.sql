-- Script creates database 'hbtn_0d_usa' and table 'states' on MySQL server
-- 'id' column is unique, auto-generated, can't be null and is a primary key
-- 'name' column is VARCHAR(256) and can't be NULL
-- If database and table already exists, script will not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
DROP TABLE IF EXISTS usa;
CREATE TABLE usa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

