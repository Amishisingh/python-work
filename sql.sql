CREATE TABLE Students (

Id INT,

Name VARCHAR(20),

Age INT

);

INSERT INTO Students (Id, Name, Age) VALUES

(1, 'Alice', 21),

(2, 'Bob', 22),

(3, 'Charlie', 23);

select * from Students;

Drop Students

CREATE TABLE IF NOT EXISTS STUDENT (

ROLL_NO TEXT PRIMARY KEY,

NAME TEXT NOT NULL,

ADDRESS TEXT,

PHONE TEXT,

AGE INTEGER

);


INSERT INTO STUDENT (ROLL_NO, NAME, ADDRESS, PHONE, AGE) VALUES

('1', 'RAM', 'DELHI', '*****', 18),

('2', 'RAMESH', 'GURGAON', '*****', 18),

('3', 'SUJIT', 'ROHTAK', '*****', 20),

('4', 'SURESH', 'DELHI', '*****', 18),

('5', 'AMAN', 'ROHTAK', '*****', 20),

('6', 'HARSH', 'GURGAON', '*****', 18);


SELECT * FROM STUDENT

WHERE AGE = 18 AND ADDRESS = 'DELHI';