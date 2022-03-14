SELECT *
FROM state_climate
LIMIT 1;

-- 2. Write a query that returns the state, year, tempf or tempc, and running_avg_temp (in either Celsius or Fahrenheit) for each state.
SELECT
  state,
  year,
  tempc,
  AVG(tempc) OVER (
    ORDER BY year
  ) AS running_avg_temp
FROM state_climate;

-- 3. Write a query that returns state, year, tempf or tempc, and the lowest temperature (lowest_temp) for each state.
SELECT
  state,
  year,
  tempc,
  FIRST_VALUE (tempc) OVER (
      PARTITION BY state
      ORDER BY tempc
   ) AS 'lowest_temp'
FROM state_climate;

-- 4. Like before, write a query that returns state, year, tempf or tempc, except now we will also return the highest temperature (highest_temp) for each state.
SELECT
  state,
  year,
  tempc,
  LAST_VALUE (tempc) OVER (
      PARTITION BY state
      ORDER BY tempc
      RANGE BETWEEN UNBOUNDED PRECEDING AND
      UNBOUNDED FOLLOWING
   ) AS 'highest_temp'
FROM state_climate;

-- 5. Write a query to select the same columns but now you should write a window function that returns the change_in_temp from the previous year (no null values should be returned).
SELECT
  state, year, tempc,
  tempc - LAG(tempc, 1, 0) OVER (
    PARTITION BY state
    ORDER BY year
    ) AS change_in_temp
FROM state_climate
ORDER BY change_in_temp DESC;

-- 6. Write a query to return a rank of the coldest temperatures on record (coldest_rank) along with year, state, and tempf or tempc. Are the coldest ranked years recent or historic? The coldest years should be from any state or year.
SELECT
  RANK() OVER (
    PARTITION BY state
    ORDER BY tempc ASC
  ) as coldest_rank,
  state, year, tempc
FROM state_climate;

-- 7. Modify your coldest_rank query to now instead return the warmest_rank for each state, meaning your query should return the warmest temp/year for each state. Again, are the warmest temperatures more recent or historic for each state?
SELECT
  RANK() OVER (
    PARTITION BY state
    ORDER BY tempc DESC
  ) as warmest_rank,
  state, year, tempc
FROM state_climate;

-- 8. Let’s now write a query that will return the average yearly temperatures in quartiles instead of in rankings for each state.
SELECT
   NTILE(4) OVER (
      PARTITION BY state
      ORDER BY tempc 
   ) AS quartile,
   state, year, tempc
FROM
   state_climate;

-- 9. Lastly, we will write a query that will return the average yearly temperatures in quintiles (5).
SELECT
   NTILE(5) OVER (
      ORDER BY tempc
   ) AS quartile,
   state, year, tempc
FROM
   state_climate;
