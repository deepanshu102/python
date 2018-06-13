'''functions
->connect():create tables and rows and commit and close
->insert():insert the row 1 by one
->search():search the data
'''
import sqlite3 as sq
cursor=None
conn=None
def connect(db):
	conn=sq.connect(db);
	cursor=conn.cursor();
	cursor.execute("""CREATE table IF NOT EXISTS courses(number INTEGER PRIMARY KEY,name text,etcs real);""");
	conn.commit()
	conn.close()
def insert():
	cursor.execute("INSERT INTO courses value(?,?,?);",(a,b,c));
	conn.commit();
	conn.close();
def search():
	a=int("Enter the number of the user");
	cursor.execute("SELECT * from courses where number=?",a)
	conn.close();
	return (cursor.fetchall());
db=input("Enter the name of the database file name");
connect(db);
a=int(input("enter the Number from the database "))
b=input("Enter the name of the user");
c=float(input("Enter the value "))
insert()
print(search())
