-- 1. Start by getting a feel for the stream table and the chat table. Select the first 20 rows from each of the two tables. What are the column names?
SELECT *
FROM STREAM
LIMIT 20;

SELECT *
FROM CHAT
LIMIT 20;

-- 2. What are the unique games in the stream table?
SELECT DISTINCT(game)
FROM stream;

-- 3. What are the unique channels in the stream table?
SELECT DISTINCT(channel)
FROM stream;

-- 4. What are the most popular games in the stream table?  Create a list of games and their number of viewers using GROUP BY.
SELECT game, count(*)
FROM stream
GROUP BY game
ORDER BY 2 DESC;

-- 5. These are some big numbers from the game League of Legends (also known as LoL).  Where are these LoL stream viewers located? Create a list of countries and their number of LoL viewers using WHERE and GROUP BY.
SELECT  country, count(*)
FROM stream
WHERE game = 'League of Legends'
GROUP BY country;

-- 6. The player column contains the source the user is using to view the stream (site, iphone, android, etc). Create a list of players and their number of streamers.
SELECT  player, count(*)
FROM stream
GROUP BY player
ORDER BY 2 DESC;

/* 7. Create a new column named genre for each of the games.

Group the games into their genres: Multiplayer Online Battle Arena (MOBA), First Person Shooter (FPS), Survival, and Other.

Using CASE, your logic should be:

If League of Legends → MOBA
If Dota 2 → MOBA
If Heroes of the Storm → MOBA
If Counter-Strike: Global Offensive → FPS
If DayZ → Survival
If ARK: Survival Evolved → Survival
Else → Other
Use GROUP BY and ORDER BY to showcase only the unique game titles.*/

SELECT game,
 CASE
  WHEN game = 'League of Legends'
      THEN 'MOBA'
  WHEN game = 'DOTA 2'
      THEN 'MOBA'
  WHEN game = 'HEROES OF THE STORM'
      THEN 'MOBA'
  WHEN game = 'Counter-Strike: Global Offensive'
      THEN 'FPS'
  WHEN game = 'DayZ'
      THEN 'Survival'
  WHEN game = 'ARK: Survival Evolved'
      THEN 'Survival'
  ELSE 'MOBA'
  END AS 'genre',
  COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC;

-- 8. Before we get started, let’s run this query and take a look at the time column from the stream table:
SELECT time
FROM stream
LIMIT 10;

-- 9. SQLite comes with a strftime() function - a very powerful function that allows you to return a formatted date. It takes two arguments: strftime(format, column). Let’s test this function out:
SELECT time,
   strftime('%S', time)
FROM stream
GROUP BY 1
LIMIT 20;

-- 10. Okay, now we understand how strftime() works. Let’s write a query that returns two columns: The hours of the time column. The view count for each hour. Lastly, filter the result with only the users in your country using a WHERE clause.
SELECT
   strftime('%H', time),
   count(*)
FROM stream
WHERE country = 'GB'
GROUP BY 1;

-- 11. The stream table and the chat table share a column: device_id.  Let’s join the two tables on that column.
SELECT *
FROM stream
JOIN chat
ON stream.device_id = chat.device_id;
