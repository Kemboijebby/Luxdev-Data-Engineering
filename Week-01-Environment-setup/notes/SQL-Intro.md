# Core SQL Concepts

## 1. Introduction to SQL

SQL (Structured Query Language) is the standard language used for managing and manipulating relational databases.  
Relational databases store data in tables, where each table consists of rows and columns.

SQL is used to perform tasks such as:
- **Retrieving data** (queries using `SELECT`)
- **Inserting new records** (`INSERT INTO`)
- **Updating existing records** (`UPDATE`)
- **Deleting records** (`DELETE`)
- **Creating and modifying schema objects** (`CREATE`, `ALTER`, `DROP`)

### Popular SQL-based Database Systems:
- **MySQL**: Open-source and widely used.
- **PostgreSQL**: Open-source with advanced features.
- **SQLite**: Lightweight and file-based, great for local apps.
- **Microsoft SQL Server**: Enterprise-grade database system by Microsoft.
- **Oracle Database**: Commercial DBMS used in large systems.

--
# SQL Basics

This guide covers fundamental SQL concepts like selecting data, filtering with conditions, using JOINs, and grouping data for summaries.

## 1. Selecting Data

### Select Specific Columns:
```sql
SELECT column1, column2 FROM table_name

To retrieve all columns:

SELECT * 
FROM table_name;

🔹 Examples

-- Example 1: Select specific columns
SELECT name, age 
FROM students;

-- Example 2: Select all columns
SELECT * 
FROM employees;

-- Example 3: Use of alias
SELECT name, salary * 1.10 AS new_salary 
FROM employees;

3. WHERE Clause

Filters rows based on a specified condition.
🔹 Syntax

SELECT column1, column2 
FROM table_name 
WHERE condition;

🔹 Operators

Comparison:

    =, <>, >, <, >=, <=

Logical:

    AND, OR, NOT

Others:

    BETWEEN, LIKE, IN

🔹 Examples

-- Employees with salary greater than 50,000
SELECT * 
FROM employees 
WHERE salary > 50000;

-- Customers with names starting with 'A'
SELECT * 
FROM customers 
WHERE name LIKE 'A%';

-- Orders with certain statuses
SELECT * 
FROM orders 
WHERE status IN ('pending', 'processing');

4. JOINs

JOINs combine rows from two or more tables based on related columns.
🔹 Types of JOINs

    INNER JOIN: Only matching rows.

    LEFT JOIN: All from left + matched from right.

    RIGHT JOIN: All from right + matched from left.

    FULL JOIN: All from both sides (if supported).

🔹 Example: INNER JOIN

SELECT orders.id, customers.name 
FROM orders
INNER JOIN customers 
ON orders.customer_id = customers.id;

🔹 Example: LEFT JOIN

SELECT customers.name, orders.id 
FROM customers
LEFT JOIN orders 
ON customers.id = orders.customer_id;

5. GROUP BY Clause

Groups rows based on column values and is used with aggregate functions.
🔹 Syntax

SELECT column, AGG_FUNCTION(column)
FROM table_name
GROUP BY column;

🔹 Examples

-- Count employees in each department
SELECT department, COUNT(*) 
FROM employees 
GROUP BY department;

-- Sum of orders by status
SELECT status, SUM(total) 
FROM orders 
GROUP BY status;

🔹 With WHERE and HAVING

SELECT department, AVG(salary)
FROM employees
WHERE salary > 30000
GROUP BY department
HAVING AVG(salary) > 50000;
