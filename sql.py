import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor to create table, insert records & retrieve data
cursor = connection.cursor()

# Create a table
table_info = """
CREATE TABLE STUDENTS(Name VARCHAR(30), Class VARCHAR(25), Section VARCHAR(25), Marks INT)
"""

cursor.execute(table_info)

# Insert some records in the table
cursor.execute('''INSERT INTO STUDENTS VALUES('Mayur', 'Software Development', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENTS VALUES('Raj', 'Data Science', 'C', 70)''')
cursor.execute('''INSERT INTO STUDENTS VALUES('Sohan', 'Software Development', 'A', 92)''')
cursor.execute('''INSERT INTO STUDENTS VALUES('Ritesh', 'Salesforce', 'D', 60)''')
cursor.execute('''INSERT INTO STUDENTS VALUES('Sonali', 'Software Development', 'B', 73)''')

# Display all records
print("The inserted records are")

data = cursor.execute('''SELECT * FROM STUDENTS''')

for row in data:
    print(row)
    
# Close the connection
connection.commit()
connection.close()





