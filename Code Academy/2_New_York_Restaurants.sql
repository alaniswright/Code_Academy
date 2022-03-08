SELECT *
FROM nomnom;

SELECT DISTINCT neighborhood
FROM nomnom;

SELECT DISTINCT cuisine
FROM nomnom;

SELECT *
FROM nomnom
WHERE cuisine = 'Chinese';

SELECT *
FROM nomnom
WHERE review >= 4;

SELECT *
FROM nomnom
WHERE cuisine = 'Italian' AND price = '$$$';

-- Find restaurants which have the word 'meatball' in the title
SELECT *
FROM nomnom
WHERE name like '%meatball%';

SELECT *
FROM nomnom
WHERE neighborhood = 'Midtown' OR 'Downtown' OR 'Chinatown';

SELECT *
FROM nomnom
WHERE health IS null;

SELECT *
FROM nomnom
ORDER BY review DESC
LIMIT 10;

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
