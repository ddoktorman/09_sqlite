import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
peeps = csv.DictReader(open('peeps.csv'))
courses = csv.DictReader(open('courses.csv'))

c.execute('CREATE TABLE peeps(name Text, age INTEGER, id INTEGER)')
c.execute('CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)')

for row in peeps:
    c.execute('INSERT INTO peeps VALUES(?,?,?)', [row['name'], row['age'], row['id']])
for row in courses:
    c.execute('INSERT INTO courses VALUES(?,?,?)', [row['code'], row['mark'], row['id']])
#==========================================================
db.commit() #save changes
db.close()  #close database
