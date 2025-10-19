-- Script lists number of records with same score in table 'second_table'
-- Results display the 'score', the number of records in column 'label'
-- and is sorted in descending order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;

