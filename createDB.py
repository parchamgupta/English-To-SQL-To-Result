import sqlite3
import pandas as pd

connection = sqlite3.connect("student.db")

cur = connection.cursor()

table1_info = """
CREATE TABLE student(name VARCHAR(40), id INTEGER(5), department_id VARCHAR(2), total_marks FLOAT(3));
"""

table2_info = """
CREATE TABLE department(department_id VARCHAR(2) ,name VARCHAR(50), department_head VARCHAR(50));
"""

cur.execute(table1_info)
cur.execute("INSERT INTO student VALUES('Naruto', '00001', 'DS', 88);")
cur.execute("INSERT INTO student VALUES('Sasuke', '00002', 'ML', 97);")
cur.execute("INSERT INTO student VALUES('Sakura', '00003', 'ML', 92);")
cur.execute("INSERT INTO student VALUES('Kakashi', '00004', 'ML', 100);")
cur.execute("INSERT INTO student VALUES('Hinata', '00005', 'DS', 85);")
cur.execute("INSERT INTO student VALUES('Shino', '00006', 'CP', 72);")
cur.execute("INSERT INTO student VALUES('Shikamaru', '00007', 'DS', 93);")
cur.execute("INSERT INTO student VALUES('Choji', '00008', 'CP', 55);")

cur.execute(table2_info)
cur.execute("INSERT INTO department VALUES('DS', 'Data Science', 'Hashirama');")
cur.execute("INSERT INTO department VALUES('ML', 'Machine Learning', 'Madara');")
cur.execute("INSERT INTO department VALUES('CP', 'Competitive Programming', 'Minato');")

print("Table student data: ")
dataStudent = cur.execute("SELECT * FROM student;")
for row in cur:
    print(row)

print("Table department data: ")
dataStudent = cur.execute("SELECT * FROM department;")
for row in cur:
    print(row)

connection.commit()
connection.close()