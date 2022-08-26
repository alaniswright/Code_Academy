-- 1
SELECT *
FROM startups;

-- 2
SELECT COUNT(*)
FROM startups;

-- 3
SELECT SUM(valuation)
FROM startups;

-- 4 & 5
SELECT MAX(raised)
FROM startups
WHERE stage = 'Seed';

-- 6
SELECT MIN(founded)
FROM startups;

-- 7
SELECT AVG(valuation)
FROM startups;

-- 8 & 9
SELECT category, ROUND(AVG(valuation), 2)
FROM startups
GROUP BY category
ORDER BY 2 DESC;

-- 10
SELECT category, COUNT(*)
FROM startups
GROUP BY category
HAVING COUNT(*) > 3;

-- 11
SELECT category, COUNT(*)
FROM startups
GROUP BY category;

-- 12
SELECT category, COUNT(*)
FROM startups
GROUP BY category
HAVING COUNT(*) > 3
ORDER BY 2 DESC;

-- 13
SELECT location, AVG(employees)
FROM startups
GROUP BY location;

-- 14
SELECT location, AVG(employees)
FROM startups
GROUP BY location
HAVING AVG(employees) > 500;
