-- Script creates database 'hbtn_0d_usa' and table 'cities' on MySQL server
-- 'cities' table has unique 'id' which is set to the 'primary key'
-- 'state_id' column can't be NULL and is a FOREIGN KEY - referencing id of 'states' table
-- If database or table exist, script will not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL
	FOREIGN KEY (state_id) REFERENCES state(id)
);

