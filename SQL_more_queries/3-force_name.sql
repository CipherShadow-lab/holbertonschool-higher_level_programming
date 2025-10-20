-- Script creates a table 'force_name' on MySQL server
-- Table columns include 'id' and 'name'
-- If table 'force_name' already exists, script will not fail
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

