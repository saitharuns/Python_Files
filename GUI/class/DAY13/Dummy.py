import sqlite3

def database():
    global conn,cursor
    conn=sqlite3.connect('dummy.db')
    cursor=conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS PRODUCT(
                   P_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   NAME TEXT UNIQUE NOT NULL,
                   PRICE REAL NOT NULL CHECK(PRICE>0),
                   QUANTITIY INTEGER NOT NULL DEFAULT 0 )""")


database()

try:

    cursor.execute('DROP TABLE CUSTOMER')
    print("table is dropped")
    
except sqlite3.Error as e:
    print(f"Error Dropping Table: {e}")

conn.commit()
conn.close()