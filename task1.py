import sqlite3

connection = sqlite3.connect('students.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
surname TEXT NOT NULL,
age INT,
city TEXT NOT NULL)
''')
connection.commit()
#students = [('Max', 'Brooks', 24, 'Spb'), ('John', 'Stones', 15, 'Spb'), ('Andy', 'Wings', 45, 'Manhester'), ('Kate', 'Brooks', 34, 'Spb')]
#cursor.executemany("INSERT INTO Students(name, surname, age, city) VALUES(?, ?, ?, ?)", students)

#connection.commit()
connection.close()

connection = sqlite3.connect('courses.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
time_start DATE,
time_end DATE)
''')

connection.commit()
#courses = [(1, 'python', '21.07.21', '21.08.21'),
#           (2, 'java', '13.07.21', '16.08.21')]
#cursor.executemany("INSERT INTO courses VALUES(?, ?, ?, ?)", courses)
#connection.commit()
connection.close()

connection = sqlite3.connect('Student_courses.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Student_courses (
courses_id INT REFERENCES Students(id),
student_id INT REFERENCES Courses(id))
''')

#connection.commit()
#Student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]
#cursor.executemany("INSERT INTO Student_courses(student_id,courses_id) VALUES(?, ?)", Student_courses)

connection.commit()
connection.close()

#Вссе студенты,кто старше 30
connection = sqlite3.connect('students.db')
cursor = connection.cursor()
students_30 = cursor.execute("SELECT name, age FROM Students WHERE age > 30").fetchall()
print(students_30)

#connection.close()

#Всех студентов, которые проходят курс по python.

connection = sqlite3.connect('Student_courses.db')
cursor = connection.cursor()
students_python = cursor.execute('''SELECT Students_name
    FROM Student_Courses
    WHERE (Courses_id = 1) AND
    (Student_id=Student_Courses.student_id)''').fetchall()
print(students_python)