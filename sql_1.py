'''
#######################################
cursor.execute("UPDATE courses set name=?,etcs=? where number=?,('name','acts','number'))

#######################################
'''
import sqlite3 as sq
conn=sq.connect("courses.db");
cursor=conn.cursor();
cursor.execute("Select * from  courses");
f=cursor.fetchall();
print(f);
cursor.execute("UPDATE courses set name=?,etcs=? where number=?",("Deepanshu","23",2341));
cursor.execute("Select * from  courses");
f=cursor.fetchall();
print("\n",f);
cursor.execute("Delete From courses where number=?",(2345,))
cursor.execute("Select * from courses");
print(cursor.fetchall())
#conn.commit();
conn.close();