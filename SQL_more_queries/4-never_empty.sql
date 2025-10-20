-- Script creates table 'unique_id' on MySQL server
-- id has default value of 1 and is unique
-- if table already exists, script will not fail
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);

