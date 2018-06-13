'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
conn.commit()
conn.close()'''

'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE course(number INTEGER PRIMARY KEY, name text, etcs real);")
cursor.execute("""INSERT INTO courses VALUES("02820", "Python programming", 5);""")
conn.commit()
conn.close()'''

'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS courses(number INTEGER PRIMARY KEY, name text, etcs real);")
cursor.execute("""INSERT INTO courses VALUES("02820", "Python programming", 5);""")
conn.commit()
conn.close()'''

'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE courses(number INTEGER PRIMARY KEY, name text, etcs real);")
cursor.execute("""INSERT INTO courses VALUES("02820", "Python programming", 5);""")
conn.commit()
conn.close()'''

'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS courses(number INTEGER PRIMARY KEY, name text, ects real);")
courses=("02457", "Nonlinear Signal Processing", 10)
cursor.execute("INSERT INTO courses VALUES(?, ?, ?);",courses)
conn.commit()
conn.close()'''

'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE courses(number INTEGER PRIMARY KEY, name text, etcs real);")
courses=[("02454", "Introduction to Cognitive Science", 5), ("02451", "Digital Signal Processing", 10)]
cursor.executemany("INSERT INTO courses VALUES (?,?,?);", courses)
conn.commit()
conn.close()'''

'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS courses(number INTEGER PRIMARY KEY, name text, etcs real);")
cursor.fetchone()
cursor.execute("SELECT * FROM courses;")
for row in cursor:
    print(row)
conn.commit()
conn.close()'''

'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS courses(number INTEGER PRIMARY KEY, name text, etcs real);")
cursor.fetchall()
cursor.execute("SELECT * FROM courses;")
for row in cursor:
    print(row)
conn.commit()
conn.close()'''

'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("SELECT * FROM courses ORDER BY number LIMIT 2;")
c=cursor.fetchall()
print(c)
conn.commit()
conn.close()'''

'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("SELECT * FROM courses WHERE number=? OR name=? OR etcs=?",("2454", "2451", " "))
rows=cursor.fetchall()
print(rows)
conn.commit()
conn.close()'''

'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("SELECT * FROM courses WHERE number=? OR name=? OR etcs=?",("324", "", ""))
rows=cursor.fetchall()
print(rows)
conn.commit()
conn.close()'''

'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
param={'etcs':10.0}
cursor.execute("SELECT number FROM courses WHERE etcs=?",(param['etcs'],))
rows=cursor.fetchall()
print(rows)'''

'''import sqlite3 as sq
conn=sq.connect("course.db")
cursor=conn.cursor()
def connect():
    conn=sq1.connect("courses.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE course(number INTEGER PRIMARY KEY, name text, etcs real);")
def insert(self):
    cursor.execute("INSERT INTO course VALUES (?, ?, ?);" a, b, c)
def search(self):
    search=input("Enter the number of user = ")
    cursor.execute("SELECT * FROM course WHERE number = ? OR name=? OR ects=?", ("value1", "value2", "value3"))
    rows=cursor.fetchall()
conn.commit()
conn.close()'''

'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("UPDATE courses SET name=?, etcs=? WHERE number=?", ('', '', '5432'))
rows=cursor.fetchall()
print(rows)
conn.commit()
conn.close()'''

'''import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("DELETE FROM courses WHERE number=?", (2454,))
conn.commit()
conn.close()'''
