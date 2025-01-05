import sqlite3

def database():
    global conn,cursor
    conn=sqlite3.connect('product.db')
    cursor=conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS PRODUCT(
                   P_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   NAME TEXT UNIQUE NOT NULL,
                   PRICE REAL NOT NULL CHECK(PRICE>0),
                   QUANTITIY INTEGER NOT NULL DEFAULT 0 )""")


database()

try:

    cursor.execute('INSERT INTO PRODUCT(NAME,PRICE,QUANTITIY) VALUES("RICE",20,1),("RAGI",21,1),("WHEAT",20,1),("JOWAR",20,1)')
    conn.commit()
except Exception as e:
    print(e)
