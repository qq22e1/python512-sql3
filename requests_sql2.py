import sqlite3

connect = sqlite3.connect('University')
cursor = connect.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""CREATE TABLE IF NOT EXISTS students(
                  StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
                  FirstName TEXT,
                  LastName TEXT
                  )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS courses(
                  CourseID INTEGER PRIMARY KEY AUTOINCREMENT,
                  CourseName TEXT,
                  Credits INTEGER
                  )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS enrollments(
                  EnrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
                  StudentID INTEGER REFERENCES students(StudentID),
                  CourseID INTEGER REFERENCES courses(CourseID)
                  )""")


connect.commit()
connect.close()