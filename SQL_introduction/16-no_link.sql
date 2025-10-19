-- Script lists all records of the 'second_table'
-- Conditions:
--      Rows are not listed where 'name' has no value
--      Results are displayed in score and name column order
--      Records are listed in descending order - by score
SELECT score, name FROM second_table WHERE name is NOT NULL ORDER BY score DESC;

