-- Script creates user 'user_0d_2' and database 'hbtn_0d_2' on SQL server running on localhost
-- Script assigns SELECT privileges to the new user.
-- Script will not fail if user already exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
DROP USER IF EXISTS 'user_0d_2'@'localhost';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;

