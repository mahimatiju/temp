import sqlite3

conn = sqlite3.connect('sample.db')

cursor = conn.cursor()

sql = '''SELECT StudentID, StudentName, AdvisorName
FROM Student
INNER JOIN Advisor
ON Student.AdvisorID = Advisor.AdvisorID;'''

# Executing the query
cursor.execute(sql)

# Fetching rows from the result table
result = cursor.fetchall()
for row in result:
    print(row)

# Closing the connection
conn.close()
