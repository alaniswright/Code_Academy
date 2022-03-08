CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE,
);

INSERT INTO friends
VALUES (1, "Ororo Munroe", '1940-05-30');

SELECT *
FROM friends;

INSERT INTO friends
VALUES (2, "Alan Wright", '1985-11-08');
VALUES (3, "Lorraine Lisk", '1987-08-13');

UPDATE friends
SET name = 'Storm'
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = 'storm:@codeacademy.com' WHERE ID = 1;
SET email = 'alan@alaniswright.com' WHERE ID = 2;
SET email = 'lorrainelisk@outlook.com' WHERE ID = 3;

DELETE FROM friends
WHERE id = 1;

SELECT *
FROM friends;
