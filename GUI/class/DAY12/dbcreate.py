import sqlite3

def database():
    global conn,cursor
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BOOK_DATA(
                   SL_N0 INTEGER PRIMARY KEY AUTOINCREMENT,
                   BOOK_ID TEXT UNIQUE NOT NULL,
                   BOOK_NAME TEXT NOT NULL,
                   AUTHOR TEXT NOT NULL,
                   PRICE REAL NOT NULL);''')
    conn.commit()

database()

"""bookid=input("enter the book id: ")
bookname=input("enter the book name: ")
author=input("enter the author name: ")
price=input("enter price : ")
cursor.execute('''INSERT INTO BOOK_DATA(BOOK_ID,BOOK_NAME,AUTHOR,PRICE) VALUES(?,?,?,?)''',(bookid,bookname,author,price))
conn.commit()
"""
#cursor.execute("SELECT * FROM BOOK_DATA")

#used to fetch only one data
#data=cursor.fetchone()
#print(data)

#used to fetch many data
'''data=cursor.fetchmany(2)# the value given in the parameter is the total number of count
for x in data:
    print(x)'''

#fetch all the data in the db
'''data=cursor.fetchall()
for x in data:
    print(x)'''


#using where clause
'''cursor.execute('SELECT * FROM BOOK_DATA WHERE SL_N0 in(1,2)')
data=cursor.fetchall()
for x in data:
    print(x)'''

'''cursor.execute('SELECT * FROM BOOK_DATA WHERE PRICE<=100 ')
data=cursor.fetchall()
for x in data:
    print(x)'''

'''cursor.execute('SELECT BOOK_NAME,AUTHOR,PRICE FROM BOOK_DATA WHERE AUTHOR = "tharun" AND PRICE<=150')
data=cursor.fetchall()
for x in data:
    print(x)'''

'''cursor.execute('SELECT * FROM BOOK_DATA WHERE SL_N0 NOT IN(1,2)')
data=cursor.fetchall()
for x in data:
    print(x)'''


'''cursor.execute('SELECT BOOK_ID,BOOK_NAME,AUTHOR,PRICE FROM BOOK_DATA ORDER BY BOOK_ID DESC')
data=cursor.fetchall()
for x in data:
    print(x)'''

'''cursor.execute('SELECT BOOK_ID,BOOK_NAME,AUTHOR,PRICE FROM BOOK_DATA ORDER BY PRICE DESC LIMIT 1')
data=cursor.fetchall()
for x in data:
    print(x)'''

#cursor.execute('ALTER TABLE BOOK_DATA ADD COLUMN PUBLISH DATE')

'''cursor.execute('SELECT BOOK_ID,BOOK_NAME,AUTHOR,PRICE FROM BOOK_DATA WHERE PRICE BETWEEN 100 AND 200 ')
data=cursor.fetchall()
for x in data:
    print(x)
'''

# cursor.execute('UPDATE BOOK_DATA SET BOOK_NAME = "MAHABARATH" WHERE BOOK_NAME="RAMAYANAM" ')
# conn.commit()

#cursor.execute('DELETE FROM BOOK_DATA WHERE PRICE>=100')

#cursor.execute('UPDATE BOOK_DATA SET PUBLISH = ? WHERE BOOK_ID= ? ',('12-12-2024','B01'))

cursor.execute("SELECT BOOK_NAME FROM BOOK_DATA")
data=cursor.fetchmany(1)
print(data)
conn.close()