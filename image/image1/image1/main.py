import sqlite3
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

cursor.execute(''' CREATE TABLE Advisor(
AdvisorID int,
AdvisorName text) ''')

cursor.execute(''' CREATE TABLE Student(
StudentID int,
StudentName text,
AdvisorID int) ''')

advisor = [ (1,"John Paul"),
(2,"Anthony Roy"),
(3,"Raj Shetty"),
(4,"Sam Reeds"),
(5,"Arthur Clintwood") ]

cursor.executemany(''' INSERT INTO Advisor VALUES (?,?)
 ''', advisor)


student = [ (501,"Ram",1),
(502,"Lakshman",1),
(503,"Ganapathy",3),
(504,"Maruthi",2),
(505,"Ravi",4),
(506,"Krishna",5),
(507,"Seetha",2),
(508,"Ganga",3),
(509,"Saraswathy",5),
(510,"Ramya",4) ]

cursor.executemany('''
INSERT INTO Student VALUES (?,?,?)
''', student)
print('Table created & values added sucessfully !')

conn.commit()
conn.close()