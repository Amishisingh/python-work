CREATE TABLE IF NOT EXISTS nomnom (
NAME VARCHAR(100),
NEIGHBOURHOOD VARCHAR(50),
CUISINE VARCHAR(100),
REVIEW REAL,
PRICE VARCHAR(100),
HEALTH VARCHAR(100)
);

INSERT INTO nomnom (NAME,NEIGHBOURHOOD,CUISINE,REVIEW,PRICE,HEALTH) VALUES
('Peter', 'Brooklyn', 'Steak', 4.4,'$$$$','A'),
('Jongro', 'Queens', 'Korean', 3.4,'$$','A'),
('Pocha', 'Midtown', 'Pizza', 4,'$','B'),
('Lighthouse', 'Chinatown', 'Chinese', 3.0,'$$$$','A'),
('Minca', 'Downtown', 'American', 3.6,'$$$$',''),
('Dirty Candy', 'Downtown', 'Italian', 3.5,'$$$$',''),
('Minca', 'Downtown', 'American', 3.6,'$$$$',''),
('Minca', 'Downtown', 'American', 3.6,'$$$$',''),
('Marea', 'Uptown', 'Italian', 4.9,'$$$','B');

SELECT * FROM nomnom;
DROP TABLE nimnom;
SELECT DISTINCT NEIGHBOURHOOD FROM nomnom;

-- Select distinct cuisines from the nomnom table

SELECT DISTINCT CUISINE FROM nomnom;

-- Select all records with Chinese cuisine

SELECT * FROM nomnom WHERE CUISINE = 'Chinese';

-- Select all records with a review rating of 4 or higher

SELECT * FROM nomnom WHERE REVIEW >= 4;

-- Select all records with Italian cuisine and $$$ price

SELECT * FROM nomnom WHERE CUISINE = 'Italian' AND PRICE = '$$$';

-- Select all records where the name contains 'Candy'

SELECT * FROM nomnom WHERE NAME LIKE '%Candy%';

-- Select all records where the neighborhood is Midtown, Downtown, or Chinatown

SELECT * FROM nomnom

WHERE NEIGHBOURHOOD IN ('Midtown', 'Downtown', 'Chinatown');

-- Select the top 4 records ordered by review rating in descending order

SELECT * FROM nomnom ORDER BY REVIEW DESC LIMIT 4;
