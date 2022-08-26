-- 1 & 2
SELECT * FROM trips;

SELECT * FROM riders;

SELECT * FROM cars;

-- 3
-- CROSS JOIN - combine each row from one table with each row from another in the result set. This JOIN is helpful for creating all possible combinations for the records (rows) in two tables.
SELECT *
FROM riders
CROSS JOIN cars;

-- 4
-- LEFT JOIN / OUTER JOIN - combine rows from different tables even if the join condition is not met
SELECT *
FROM trips
LEFT JOIN riders
  ON trips.rider_id = riders.id;

-- 5
-- INNER JOIN is the default JOIN and it will only return results matching the condition specified by ON.
SELECT *
FROM trips
JOIN cars
  ON trips.car_ID = cars.id;

-- 6
-- UNION - combine results that appear from multiple SELECT statements and filter duplicates (Stack two tables on top of each other)
SELECT *
FROM riders
UNION
SELECT *
FROM riders2;

-- 7
SELECT AVG(cost)
FROM trips;

-- 8
SELECT *
FROM riders
WHERE total_trips < 500
UNION
SELECT *
FROM riders2
WHERE total_trips < 500;

-- 9
SELECT *
FROM cars
WHERE status = 'active';

-- 10
SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;
