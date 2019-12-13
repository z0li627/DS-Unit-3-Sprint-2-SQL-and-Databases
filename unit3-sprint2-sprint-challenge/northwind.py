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


def run_queries2():
    """- What are the ten most expensive items (per unit price) in the database *and*
         their suppliers?
       - What is the largest category (by number of unique products in it)?
       - (*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
         (not name, region, or other fields) as the unique identifier for territories.
    """
    print(c.execute('SELECT (UnitPrice) FROM Product ORDER BY UnitPrice desc limit 10;').fetchall())
    print(c.execute("""SELECT UnitPrice
                       FROM Product
                       INNER JOIN Supplier
                       ON Supplier.Id = Product.SupplierId
                       ORDER BY UnitPrice desc limit 10;""").fetchall())
    print(c.execute("""SELECT COUNT(CategoryId) AS cnt FROM Product
                       INNER JOIN Category
                       ON Category.Id = Product.CategoryId
                       GROUP BY CategoryId
                       ORDER BY cnt DESC
                       LIMIT 1;""").fetchall())



if __name__ == "__main__":
    run_queries()