-- RRUNNING TOTAL
SELECT
   month,
   change_in_followers,
   SUM(change_in_followers) OVER (
      ORDER BY month
   ) AS 'running_total',
   AVG(change_in_followers) OVER (
      ORDER BY month
   ) AS 'running_avg',
   COUNT(change_in_followers) OVER (
      ORDER BY month
   ) AS 'running_count'
FROM
   social_media
WHERE
   username = 'instagram';


-- PARTITION BY - running total by username
SELECT
    username,
    month,
    change_in_followers,
    SUM(change_in_followers) OVER (
      PARTITION BY username
      ORDER BY month
    ) 'running_total_followers_change',
    posts,
    AVG(change_in_followers) OVER (
      PARTITION BY username
      ORDER BY month
    ) 'running_avg_followers_change'
FROM
    social_media;

-- First value
SELECT username,
   posts,
   FIRST_VALUE (posts) OVER (
      PARTITION BY username
      ORDER BY posts
   ) AS 'fewest_posts'
FROM social_media;

-- LAST VALUE
-- Last value is more complicated because each row in our results set is the last row at the time it is outputted. In order to get LAST_VALUE to show us the most posts for a user, we need to specify a frame for our window function.
SELECT
   username,
   posts,
   LAST_VALUE (posts) OVER (
      PARTITION BY username
      ORDER BY posts
      RANGE BETWEEN UNBOUNDED PRECEDING AND
      UNBOUNDED FOLLOWING
    ) most_posts
FROM
    social_media;

-- LAG
SELECT
   artist,
   week,
   streams_millions,
   streams_millions - LAG(streams_millions, 1, streams_millions) OVER (
      PARTITION BY artist
      ORDER BY week
   ) AS 'streams_millions_change',
   chart_position,
   LAG(chart_position, 1, chart_position) OVER (
      PARTITION BY artist
      ORDER BY week
) - chart_position AS 'chart_position_change'
FROM
   streams
WHERE
   artist = 'Lady Gaga';

-- LEAD
SELECT
   artist,
   week,
   streams_millions,
   LEAD(streams_millions, 1) OVER (
      PARTITION BY artist
      ORDER BY week
   ) - streams_millions AS 'streams_millions_change',
   chart_position,
   chart_position - LEAD(chart_position, 1) OVER (
      PARTITION BY artist
      ORDER BY week
   ) AS 'chart_position_change'
FROM
   streams;

   -- ROW NUMBER
   SELECT
   ROW_NUMBER() OVER (
      ORDER BY streams_millions DESC
   ) AS 'row_num',
   artist,
   week,
   streams_millions
FROM
   streams;

   -- RANK

   SELECT
   RANK() OVER (
      PARTITION BY week
      ORDER BY streams_millions DESC
   ) AS 'rank',
   artist,
   week,
   streams_millions
FROM
   streams;

   -- NTile - breaks results up into number of groups (eg, quartiles)

   SELECT
   NTILE(4) OVER (
      ORDER BY streams_millions DESC
   ) AS 'weekly_streams_group',
   artist,
   week,
   streams_millions
FROM
   streams;
