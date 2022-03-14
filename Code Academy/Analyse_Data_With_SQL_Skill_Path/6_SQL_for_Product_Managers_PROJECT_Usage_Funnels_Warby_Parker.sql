-- 1
SELECT *
FROM survey
LIMIT 10;

-- 2
SELECT
 question,
 count(DISTINCT user_id),
 count(DISTINCT user_id) / 5 AS '%'
FROM survey
GROUP BY question;

-- 3
SELECT *
FROM quiz
LIMIT 5;

-- 4
SELECT *
FROM home_try_on
LIMIT 5;

-- 5
SELECT *
FROM purchase
LIMIT 5;

-- 6
-- Create a new table that tracks how users move through the funnel
-- How many who took quiz use the Home Try On?  How many pairs are sent out for home try on? How many of those purchase?
SELECT
 quiz.user_id as 'user_id',
 home_try_on.user_id IS NOT NULL AS 'is_home_try_on',
 home_try_on.number_of_pairs as 'number_of_pairs',
 purchase.user_id IS NOT NULL AS 'is_purchase'
FROM quiz
LEFT JOIN home_try_on
 ON quiz.user_id = home_try_on.user_id
LEFT JOIN purchase
 ON home_try_on.user_id = purchase.user_id
LIMIT 10;
