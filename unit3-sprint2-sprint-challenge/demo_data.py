"""
Unit 3 Sprint 2 Sprint Challenge
demo_data.py
"""

import sqlite3

conn = sqlite3.connect('demo.sqlite3')


def make_db():
    """Creating table"""
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS demo
                 (s, x, y)""")
    c.close()
    conn.commit()


def addentries():
    """Adding entries to the table"""
    c = conn.cursor()
    c.execute("""INSERT INTO demo (s, x, y)
                 VALUES
                 ('g', 3, 9),
                 ('v', 5, 7),
                 ('f', 8, 7);""")
    c.close()
    conn.commit()


def run_queries():
    """check the data"""
    c = conn.cursor()
    print(c.execute('SELECT * from demo;').fetchall())

def more_queries():
    """- Count how many rows you have - it should be 3!
       - How many rows are there where both `x` and `y` are at least 5?
       - How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
         `DISTINCT`)?"""
    c = conn.cursor()
    print(c.execute("""SELECT COUNT(*) FROM demo""").fetchall())
    print(c.execute("""SELECT * FROM demo WHERE x > 5 AND y > 5""").fetchall())
    print(c.execute("""SELECT COUNT(DISTINCT y) FROM demo""").fetchall())

if __name__ == "__main__":
    make_db()
    addentries()
    run_queries()
    more_queries()