import sqlite3

def database():
    global conn,cursor
    conn = sqlite3.connect("MULTI.db")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS STUDENT_DATA("NAME" VARCHAR(20),"MOBILE" LONGINT(10),"MAIL" VARCHAR(20))')
    conn.commit()
    

var=[('sai',543463456,'sai@gmial'),
     ('saitharun',543463456,'sai@gmial'),
     ('saivijay',543463456,'sai@gmial'),
     ('sai',543463456,'sai@gmial'),
     ('sai',543463456,'sai@gmial'),

     ]


def update_st():
    database()
    cursor.executemany("INSERT INTO `STUDENT_DATA` (name,mobile,mail) VALUES(?, ?, ?)",var)
    conn.commit()
    cursor.close()


ch=int(input('enter the number'))

if(ch==1):
    update_st()

