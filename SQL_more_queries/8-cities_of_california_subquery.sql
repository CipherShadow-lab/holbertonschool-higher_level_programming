-- Script lists all cities of California found in database 'hbtn_0d_usa'.
-- 'states' table contains one record where 'name' = 'California' (but id is different)
-- Results are sorted in ascending order by 'cities.id'
SELECT id, name
FROM cities
WHERE state_id = (
        SELECT id
        FROM states
        WHERE name = 'California'
    );
