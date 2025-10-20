-- Script creates table 'unique_id' on MySQL server
-- 'id' column defaults at 1 and each id is unique
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256) NOT NULL
);

