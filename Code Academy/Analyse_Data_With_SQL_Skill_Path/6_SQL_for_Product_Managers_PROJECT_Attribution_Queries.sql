-- 1
SELECT
  COUNT(DISTINCT(utm_campaign))
FROM page_visits;

SELECT
  COUNT(DISTINCT(utm_source))
FROM page_visits;

SELECT
  DISTINCT utm_campaign, utm_source
FROM page_visits;

-- 2
SELECT
  DISTINCT(page_name)
FROM page_visits;

-- 3
-- FIRST TOUCHES
-- Count first touches
WITH first_touch AS (
    SELECT user_id,
        MIN(timestamp) as first_touch_at
    FROM page_visits
    GROUP BY user_id),

-- Map first touches against campaign & source data
ft_attr AS (
  SELECT ft.user_id,
      ft.first_touch_at,
      pv.utm_source,
          pv.utm_campaign
  FROM first_touch ft
  JOIN page_visits pv
      ON ft.user_id = pv.user_id
      AND ft.first_touch_at = pv.timestamp)

-- Count which campaign & source gives most first touches
SELECT
  utm_source,
  utm_campaign,
  COUNT(first_touch_at)
FROM ft_attr
GROUP BY 1, 2
ORDER BY 3 DESC;

-- 4
-- LAST TOUCHES
-- Count lat touches
WITH last_touch AS (
    SELECT user_id,
        MIN(timestamp) as last_touch_at
    FROM page_visits
    GROUP BY user_id),

-- Map last touches against campaign & source data
lt_attr AS (
  SELECT lt.user_id,
      lt.last_touch_at,
      pv.utm_source,
          pv.utm_campaign
  FROM last_touch lt
  JOIN page_visits pv
      ON lt.user_id = pv.user_id
      AND lt.last_touch_at = pv.timestamp)

-- Count which campaign & source gives most last touches
SELECT
  utm_source,
  utm_campaign,
  COUNT(last_touch_at)
FROM lt_attr
GROUP BY 1, 2
ORDER BY 3 DESC;
*/

-- 5
-- Count the distinct users who visited the page named 4 - purchase.
SELECT COUNT(DISTINCT(user_id))
FROM page_visits
WHERE page_name = '4 - purchase';

-- 6
-- How many last touches on the purchase page is each campaign responsible for?
-- Count lat touches
WITH last_touch AS (
    SELECT user_id,
        MIN(timestamp) as last_touch_at
    FROM page_visits
    WHERE page_name = '4 - purchase'
    GROUP BY user_id),
