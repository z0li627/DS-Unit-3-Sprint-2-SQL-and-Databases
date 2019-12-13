"""
northwind.py
"""

import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

def run_queries():
    """Run queries:
       - What are the ten most expensive items (per unit price) in the database?
       - What is the average age of an employee at the time of their hiring? (Hint: a
         lot of arithmetic works with dates.)
       - (*Stretch*) How does the average age of employee at hire vary by city?"""
    c = conn.cursor()
    print(c.execute('SELECT (UnitPrice) FROM Product ORDER BY UnitPrice desc limit 10;').fetchall())
    print(c.execute('SELECT AVG(HireDate - BirthDate) FROM Employee;').fetchall())


if __name__ == "__main__":
    run_queries()