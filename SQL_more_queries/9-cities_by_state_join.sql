-- Script lists all cities contained in database 'hbtn_0d__usa'
-- Each record displays 'cities.id' - 'cities.name' - 'states.name'
-- Results are displayed in ascending order by 'cities.id'
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

