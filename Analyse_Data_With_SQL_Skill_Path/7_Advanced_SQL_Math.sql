-- MULTIPLICATION
SELECT
(price * quantity) as total_cost
FROM bakery;

-- ABSOLUTE VALUES
SELECT first_name, ABS(guess - 804)
FROM guesses;

SELECT ABS(AVG(guess) - 804)
FROM guesses;

-- CAST
SELECT 3 / 2; -- 1
SELECT 1.0 * 3 / 2; -- 1.5
SELECT CAST(3 AS REAL) / 2; -- 1.5
SELECT CAST('3.14 is pi' AS REAL); -- 3.14 - "is pi" ignored

-- DATE AND TIME
-- The DATETIME() function will return the entire time string which includes the date and time portions.
SELECT DATETIME('2020-09-01 17:38:22');

--To obtain the current date and time, you can provide the string 'now' to the function, which returns the date and time in UTC.
SELECT DATETIME('now');

--To obtain the date and time converted to your local timezone, you can provide a modifier localtime.
SELECT DATETIME('now', 'localtime');

-- The DATE() function allows us to extract just the date portion of a time string, which consists of the year, month and day.
SELECT DATE('2020-09-01 17:38:22'); -- 2020-09-01

--The TIME() function allows us to extract just the time portion of a time string, which consists of the hour, minute and second.
SELECT TIME('2020-09-01 17:38:22'); -- 17:38:22

-- First, it will apply the modifier 'start of month' which will shift to the beginning of the month, '2020-02-01 00:00:00'. It will include the time portion because we are using the DATETIME() function.
-- Then, it will apply the modifier '-1 day' which will offset the day by -1, resulting in '2020-01-31 00:00:00'.
-- Finally, it will apply the modifier '+7 hours', which will add 7 hours to the time, giving the final result of '2020-01-31 07:00:00'.
SELECT DATETIME('2020-02-10', 'start of month', '-1 day', '+7 hours');

-- Use STRFTIME() with the COUNT() function to find out how many orders were made on each day. Show the results in descending order based on the daily number of orders.Use STRFTIME() with the COUNT() function to find out how many orders were made on each day. Show the results in descending order based on the daily number of orders.
SELECT STRFTIME('%d', order_date) as day, count(*)
FROM bakery
GROUP BY 1
ORDER BY 2 DESC;
