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

---

## 2. SELECT Statement

The `SELECT` statement is the most commonly used SQL command, allowing users to retrieve data from tables.

**Syntax**:  
```sql
SELECT column1, column2 FROM table_name;
To retrieve all columns:

sql
Copy
Edit
SELECT * FROM table_name;
Examples:
Example 1:

sql
Copy
Edit
SELECT name, age FROM students;
Example 2:

sql
Copy
Edit
SELECT * FROM employees;
Example 3:

sql
Copy
Edit
SELECT name, salary * 1.10 AS new_salary FROM employees;
Using Aliases (AS): Helps rename columns in the result set.

3. WHERE Clause
The WHERE clause filters rows based on a specified condition.

Syntax:

sql
Copy
Edit
SELECT columns FROM table WHERE condition;
Common Comparison Operators:
= (equals)

<> (not equals)

> (greater than)

< (less than)

>= (greater than or equal to)

<= (less than or equal to)

Logical Operators:
AND

OR

NOT

Other Operators:
BETWEEN: Range filtering

LIKE: Pattern matching ('%a' ends with 'a', 'a%' starts with 'a')

IN: Matches any value in a list

Examples:
Example 1:

sql
Copy
Edit
SELECT * FROM employees WHERE salary > 50000;
Example 2:

sql
Copy
Edit
SELECT * FROM customers WHERE name LIKE 'A%';
Example 3:

sql
Copy
Edit
SELECT * FROM orders WHERE status IN ('pending', 'processing');
4. JOINs
JOINs combine records from two or more tables based on a related column between them.

Types of JOINs:
INNER JOIN: Returns only matching rows.

LEFT JOIN: Returns all rows from the left table, and matched rows from the right.

RIGHT JOIN: Opposite of LEFT JOIN (not supported in all DBs).

FULL JOIN: Returns all rows from both tables with matches where possible.

Example INNER JOIN:
sql
Copy
Edit
SELECT orders.id, customers.name 
FROM orders
JOIN customers ON orders.customer_id = customers.id;
Example LEFT JOIN:
sql
Copy
Edit
SELECT customers.name, orders.id 
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id;
JOINs are essential for normalized databases where data is split across multiple tables.

5. GROUP BY Clause
GROUP BY groups rows that have the same values into summary rows. It is often used with aggregate functions: COUNT(), SUM(), AVG(), MAX(), MIN().

Syntax:

sql
Copy
Edit
SELECT column, AGG_FUNCTION(column) FROM table GROUP BY column;
Examples:
Example 1:

sql
Copy
Edit
SELECT department, COUNT(*) FROM employees GROUP BY department;
Example 2:

sql
Copy
Edit
SELECT status, SUM(total) FROM orders GROUP BY status;
GROUP BY can be combined with WHERE and HAVING:

Example 3:

sql
Copy
Edit
SELECT department, AVG(salary) FROM employees
WHERE salary > 30000 GROUP BY department HAVING AVG(salary) > 50000;
