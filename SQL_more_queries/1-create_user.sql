-- Script creates user 'user_0d_1' on SQL server running on localhost
-- Script will not fail if user already exists.
DROP USER IF EXISTS 'user_01_1'@'localhost';
CREATE USER 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
FLUSH PRIVILEGES

