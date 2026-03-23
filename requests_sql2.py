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

students_data = [
    ("Иван", "Петров"),
    ("Мария", "Сидорова"),
    ("Алексей", "Смирнов"),
    ("Екатерина", "Кузнецова"),
    ("Дмитрий", "Волков")]

courses_data = [
    ("Математика", 5),
    ("Физика", 4),
    ("Программирование", 6),
    ("Базы данных", 5),
    ("Английский язык", 3)]

enrollments_data = [
    (1, 3), (1, 5),
    (2, 1), (2, 4),
    (3, 2), (3, 5),
    (4, 1), (4, 3),
    (5, 2), (5, 4)
]
#cursor.executemany("INSERT INTO students (FirstName, LastName) VALUES (?, ?)", students_data)

#cursor.executemany("INSERT INTO courses (CourseName, Credits) VALUES (?, ?)", courses_data)

#cursor.executemany("INSERT INTO enrollments (StudentID, CourseID) VALUES (?, ?)", enrollments_data)
cursor.execute("SELECT * FROM enrollments")
result1 = cursor.fetchall()


cursor.execute("""SELECT students.FirstName,students.LastName,courses.CourseName
                  FROM enrollments
                  JOIN students ON enrollments.StudentID = students.StudentID
                  JOIN courses ON enrollments.CourseID = courses.CourseID
                  ORDER BY FirstName,LastName""")
result2 = cursor.fetchall()

cursor.execute("""SELECT students.FirstName,students.LastName 
                  FROM enrollments
                  JOIN students ON enrollments.StudentID = students.StudentID
                  JOIN courses ON enrollments.CourseID = courses.CourseID
                  WHERE courses.CourseID = 1
                  """)
result3 = cursor.fetchall()

cursor.execute("""SELECT students.FirstName,students.LastName,courses.CourseName
                  FROM enrollments
                  JOIN students ON enrollments.StudentID = students.StudentID
                  JOIN courses ON enrollments.CourseID = courses.CourseID
                  WHERE students.FirstName = 'Мария' OR students.LastName = 'Кузнецова'
                  ORDER BY LastName""")
result4 = cursor.fetchall()



#connect.commit()
connect.close()