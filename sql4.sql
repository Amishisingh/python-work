-- Salesman Table
-- ===============================

CREATE TABLE IF NOT EXISTS Salesman (

Salesman_id VERCHAR(50) PRIMARY KEY,

name VERCHAR(100),
city VERCHAR(100),
Comission VERCHAR(100)
);

INSERT INTO Salesman (Salesman_id, name, city, Comission) VALUES

('5001', 'James Hoog', 'New York', '0.15'),
('5002', 'Nail Knite', 'Paris', '0.13'),
('5005', 'Pit Alex', 'London', '0.11'),
('5006', 'Mc Lyon', 'Paris', '0.14'),
('5007', 'Paul Adam', 'Rome', '0.13'),
('5003', 'Lauson Hen', 'San Jose', '0.12');

-- ===============================
-- Customer Table
-- ===============================

CREATE TABLE IF NOT EXISTS Customer (

customer_id VERCHAR(100),
cust_name VERCHAR(100) PRIMARY KEY,
city VERCHAR(100),
grade VERCHAR(100),
Salesman_id VERCHAR(100)
);

INSERT INTO Customer (customer_id, cust_name, city, grade, Salesman_id) VALUES

('3002', 'nick rimando', 'new york', '100', '5001'),
('3007', 'brad davis', 'new york', '200', '5001'),
('3005', 'graham zusi', 'california', '200', '5002'),
('3008', 'julian green', 'london', '300', '5002'),
('3004', 'fabian johnson', 'paris', '300', '5006'),
('3009', 'geoff cameron', 'berlin', '100', '5003'),
('3003', 'jozy altidore', 'moscow', '200', '5007'),
('3001', 'brad guzan', 'london', NULL, '5005');

-- ===============================
-- Orders Table
-- ===============================

CREATE TABLE IF NOT EXISTS Orders (

ord_no VERCHAR(100) PRIMARY KEY,

purch_amt VERCHAR(100),
ord_date VERCHAR(100),
customer_id VERCHAR(100),
Salesman_id VERCHAR(100)
);

INSERT INTO Orders (ord_no, purch_amt, ord_date, customer_id, Salesman_id) VALUES

('70001', '150.5', '2012-10-05', '3005', '5002'),
('70009', '270.65', '2012-09-10', '3001', '5001'),
('70002', '65.26', '2012-10-05', '3002', '5003'),
('70004', '110.5', '2012-08-17', '3009', '5007'),
('70007', '948.5', '2012-09-10', '3005', '5005'),
('70005', '2400.6', '2012-07-27', '3007', '5006');

SELECT customer.cust_name,salesman.name,salesman.city
FROM customer
JOIN salesman ON customer.city * salesman.city;

SELECT customer.cust_name,salesman.name
FROM customer
JOIN salesman ON customer.salesman_id=salesman.salesman_id;

SELECT orders.ord_no,customer.cust_name,Orders.customer_id,Orders.salesman_id
FROM orders
JOIN customer ON Orders.customer_id = customer.customer_id
JOIN salesman ON Orders.salesman_id = salesman.salesman_id
WHERE customer.city <> salesman.city;

SELECT orders.ord_no,customer.cust_name
From Orders
JOIN customer ON Orders.salesman_id = salesman.salesman_id;

SELECT customer.cust_name AS "Customer" , customer.grade AS "Grade"
FROM Orders
JOIN salesman ON Orders.salesman_id = salesman.salesman_id
JOIN customer ON Orders.customer_id = customer.customer_id

SELECT *
FROM Customer
JOIN Orders ON Customer.customer_id=Orders.customer_id
WHERE Orders.ord_date = "2012-10-05";