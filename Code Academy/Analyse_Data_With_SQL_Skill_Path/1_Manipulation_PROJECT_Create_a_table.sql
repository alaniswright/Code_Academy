-- 1
CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE,
);

-- 2
INSERT INTO friends
VALUES (1, "Ororo Munroe", '1940-05-30');

-- 3
SELECT *
FROM friends;

-- 4
INSERT INTO friends
VALUES (2, "Alan Wright", '1985-11-08');
VALUES (3, "Lorraine Lisk", '1987-08-13');

-- 5
UPDATE friends
SET name = 'Storm'
WHERE id = 1;

-- 6
ALTER TABLE friends
ADD COLUMN email TEXT;

-- 7
UPDATE friends
SET email = 'storm:@codeacademy.com' WHERE ID = 1;
SET email = 'alan@alaniswright.com' WHERE ID = 2;
SET email = 'lorrainelisk@outlook.com' WHERE ID = 3;

-- 8
DELETE FROM friends
WHERE id = 1;

-- 9
SELECT *
FROM friends;
