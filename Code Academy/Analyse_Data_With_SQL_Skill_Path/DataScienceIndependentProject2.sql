-- Data Science Indepent Project 2
-- https://discuss.codecademy.com/t/data-science-independent-project-2-explore-a-sample-database/419945

-- 1. "Which tracks appeared in the most playlists? how many playlist did they appear in?"
-- Top 50 tracks ordered by how many playlists they appear in

SELECT
	tracks.name as 'Track name',
	COUNT(*) as 'Number of playlists'
FROM playlist_track
JOIN tracks
ON playlist_track.TrackId=tracks.TrackId
GROUP BY playlist_track.TrackId
ORDER BY 2 DESC
LIMIT 50;

-- 2. "Which track generated the most revenue? which album? which genre?"

-- Top 50 tracks by revenue

SELECT
	tracks.name as 'Track name',
	SUM(invoice_items.UnitPrice) AS 'Revenue'
FROM tracks
JOIN invoice_items	
	ON tracks.TrackId=invoice_items.TrackId
GROUP BY tracks.TrackId
ORDER BY 2 DESC
LIMIT 50;

-- Top 50 albums by revenue

SELECT
	albums.title as 'Album name',
	SUM(invoice_items.UnitPrice) AS 'Revenue'
FROM invoice_items
JOIN tracks
	ON tracks.TrackID=invoice_items.TrackId
JOIN albums
	ON albums.AlbumId=tracks.AlbumId
GROUP BY albums.AlbumId
ORDER BY 2 DESC
LIMIT 50;

-- Top 10 genres by revenue	

SELECT
	genres.name as 'Genre',
	ROUND(SUM(invoice_items.UnitPrice), 2) AS 'Revenue'
FROM invoice_items
JOIN tracks
	ON tracks.TrackID=invoice_items.TrackId
JOIN genres
	ON genres.GenreID=tracks.GenreId
GROUP BY genres.GenreId
ORDER BY 2 DESC
LIMIT 10;

-- 3. "Which countries have the highest sales revenue? What percent of total revenue does each country make up?"

-- 50 countries with the highest sales revenue

SELECT 
	invoices.BillingCountry as 'Country',
	round(sum(invoices.Total)) AS 'Revenue'
FROM invoices
GROUP BY 1
ORDER BY 2 DESC
LIMIT 50;

-- % of total sales revenue for each Country

SELECT
	invoices.BillingCountry AS 'Country',
	ROUND(SUM(invoices.total)	* 100 / (SELECT SUM(invoices.total) FROM invoices), 1) AS '% of revenue'
FROM invoices
GROUP BY invoices.BillingCountry
ORDER BY 2 DESC
LIMIT 50;

-- 4. "How many customers did each employee support, what is the average revenue for each sale, and what is their total sale?"

SELECT
	employees.FirstName || ' ' || employees.LastName AS 'Employee name',
	COUNT(customers.SupportRepId) as '# customers supported',
	ROUND(SUM(invoices.Total) / COUNT(invoices.total), 3) as 'Average sale value',
	ROUND(SUM(invoices.Total)) as 'Total Sale' 
FROM customers
JOIN employees
	ON customers.SupportRepId = employees.EmployeeId
JOIN invoices
	ON customers.CustomerId = invoices.CustomerId
GROUP BY customers.SupportRepId
ORDER BY 2 DESC
LIMIT 50;


