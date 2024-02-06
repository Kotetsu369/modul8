import sqlite3

connection = sqlite3.connect('courses_students.db')
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

cursor.execute('''CREATE TABLE IF NOT EXISTS Student_courses (
courses_id INT REFERENCES Students(id),
student_id INT REFERENCES Courses(id))
''')
connection.commit()

#Student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]
#cursor.executemany("INSERT INTO Student_courses(student_id,courses_id) VALUES(?, ?)", Student_courses)
#connection.commit()

#Вссе студенты,кто старше 30
students_30 = cursor.execute("SELECT name, age FROM Students WHERE age > 30").fetchall()
print(students_30)

#Всех студентов, которые проходят курс по python.

students_python = cursor.execute('''SELECT Students.name, Courses.name
    FROM Students
    JOIN  Student_courses
    ON (Student_courses.student_id = Students.id)
    JOIN Courses
    ON (Courses.id = Student_courses.courses_id) AND
    (Student_courses.courses_id=1)''').fetchall()
print(students_python)

# Всех студентов, которые проходят курс по python и из Spb

python_SPB = cursor.execute('''SELECT Students.name, Courses.name, Students.city
    FROM Students, Courses, Student_courses
    WHERE (Student_courses.student_id = Students.id) AND (Students.city='Spb')
    AND (Courses.id = Student_courses.courses_id) AND
    (Student_courses.courses_id=1)''').fetchall()
print(python_SPB)

connection.close()