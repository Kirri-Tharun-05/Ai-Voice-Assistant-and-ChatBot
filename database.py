import sqlite3
import os
from adodbapi import Cursor

con=sqlite3.connect("voiceAssistant.db")

cursor=con.cursor()
# #
# query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100),path VARCHAR(1000))"
# cursor.execute(query)

# query="INSERT INTO sys_command VALUES(null,'one note','C:\\Program Files\\Microsoft Office\\root\\Office16')"
# query="UPDATE sys_command SET name = 'one note', path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe' WHERE id = 2;"
# query="INSERT INTO sys_command VALUES(null,'ms word','C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')"
# query="DELETE FROM sys_command WHERE id=3"
# query="INSERT INTO sys_command VALUES(null,'calculator','C:\\Windows\\System32\\calc.exe')"
# cursor.execute(query)
# con.commit()

# query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100),path VARCHAR(1000))"
# cursor.execute(query)
# query="INSERT INTO web_command VALUES(null,'git hub','https://github.com//')"
# cursor.execute(query)
# con.commit()


# Testing Code
# app_name="chat gpt"
# cursor.execute("SELECT path FROM web_command WHERE name IN(?)",(app_name,))
# result=cursor.fetchall()
# print(len(result))
# print(result[0][0])
# app_name="vs code"
# cursor.execute("SELECT path FROM sys_command WHERE name IN(?)",(app_name,))
# result=cursor.fetchall()
# print(len(result))
# print(result[0][0])
#
# os.startfile()

# query="UPDATE sys_command SET path='C:\\Users\\tharu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'"
# cursor.execute(query)
# con.commit()

# app_name='vs code'
# cursor.execute(
#                  "SELECT path FROM sys_command WHERE name IN(?)",(app_name,)
#              )
# result=cursor.fetchall()
# print(result)
# print(len(result))

# inserting contact to contact database
# cursor.execute("CREATE TABLE IF NOT EXISTS contact (id int primary key, name VARCHAR(50), mobile_no VARCHAR(50))")
# cursor.execute("INSERT INTO contact (id,'name','mobile_no')VALUES(null,'Amma','+91 88698 31979')")
# cursor.execute("INSERT INTO contact (id,'name','mobile_no')VALUES(null,'Aarchi','+91 85338 43455')")
# cursor.execute("INSERT INTO contact (id,'name','mobile_no')VALUES(null,'Praji','+91 6300 590 511')")
# con.commit()
# con.close()


# searching contact from database
# query ="praji"
# query= query.strip().lower()

# cursor.execute('SELECT mobile_no FROM contact WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?',("%"+query+"%",query+"%"))
# result=cursor.fetchall()
# print(result[0][0])