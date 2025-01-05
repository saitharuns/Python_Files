import sqlite3

def database():
    global conn,cursor
    conn=sqlite3.connect('student.db')
    cursor=conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS STUDENT(
                   STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   NAME TEXT UNIQUE NOT NULL,
                   AGE INTEGER NOT NULL,
                   SALARY REAL CHECK(SALARY>0))""")

database()

# name=input("enter the name: ")
# age=int(input("enter the age : "))
# salary=float(input('enter the salary : '))

# cursor.execute("INSERT INTO STUDENT(NAME,AGE,SALARY) VALUES(?,?,?)",(name,age,salary))
# print("data inserted successfully...")

cursor.execute('SELECT NAME,COUNT(NAME),SUM(SALARY) FROM STUDENT GROUP BY NAME ORDER BY COUNT(NAME) DESC')
data=cursor.fetchall()
for x in data:
    print(x)
#print(data)

conn.commit()
conn.close()