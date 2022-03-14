-- 1
SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

-- 2
SELECT SUM(score)
FROM hacker_news;

-- 3
SELECT user, SUM(score)
FROM hacker_news
GROUP BY user
HAVING SUM(SCORE) > 200;

-- 4
SELECT (309 + 304 + 282 + 517) / 6366.0;

-- 5
SELECT user,
   COUNT(*)
FROM hacker_news
WHERE url LIKE '%watch?v=dQw4w9WgXcQ%'
GROUP BY user
ORDER BY COUNT(*) DESC;

-- 6 & 7
SELECT CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
  END AS 'Source',
  COUNT(*)
FROM hacker_news
GROUP BY 1;

-- 8
SELECT timestamp
FROM hacker_news
LIMIT 10;

-- 9
SELECT timestamp,
   strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;

--10 & 11
-- This returns the hour, HH, of the timestamp column! Read more about function at https://www.sqlite.org/lang_datefunc.html
SELECT strftime('%H', timestamp) AS 'Hour',
   ROUND(AVG(score), 1) AS 'Average Score',
   COUNT(*) AS 'Number of Stories'
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 1;
