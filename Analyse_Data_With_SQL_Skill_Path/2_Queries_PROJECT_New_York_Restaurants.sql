-- 1
SELECT *
FROM nomnom;

-- 2
SELECT DISTINCT neighborhood
FROM nomnom;

-- 3
SELECT DISTINCT cuisine
FROM nomnom;

-- 4
SELECT *
FROM nomnom
WHERE cuisine = 'Chinese';

-- 5
SELECT *
FROM nomnom
WHERE review >= 4;

-- 6
SELECT *
FROM nomnom
WHERE cuisine = 'Italian' AND price = '$$$';

-- 7
-- Find restaurants which have the word 'meatball' in the title
SELECT *
FROM nomnom
WHERE name like '%meatball%';

-- 8
SELECT *
FROM nomnom
WHERE neighborhood = 'Midtown' OR 'Downtown' OR 'Chinatown';

-- 9
SELECT *
FROM nomnom
WHERE health IS null;

-- 10
SELECT *
FROM nomnom
ORDER BY review DESC
LIMIT 10;

-- 11
-- Use a CASE statement to change the rating system to words, and print list of new ratings alongside restaurant names
SELECT name,
  CASE
    WHEN review > 4.5 THEN 'Extraordinary'
    WHEN review > 4 THEN 'Excellent'
    WHEN review > 3 THEN 'Good'
    WHEN review > 2 THEN 'Fair'
    ELSE 'Poor'
  END AS 'Review'
FROM nomnom;
