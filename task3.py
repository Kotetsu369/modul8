import datetime
from peewee import *

conn = SqliteDatabase('db1.sqlite')

class Student(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')

    class Meta:
        database = conn
        db1_table = 'Students'

class Course(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField(column_name='name')
    time_start = DateTimeField(column_name='time_start')
    time_end = DateTimeField(column_name='time_finish')
    class Meta:
        database = conn
        db1_table = 'Courses'

class Student_course(Model):
    Student_id = ForeignKeyField(Student)
    Courses_id = ForeignKeyField(Course)

    class Meta:
        database = conn
        db1_table = 'Student_courses'

#Student.create_table()
#Course.create_table()
#Student_course.create_table()


#Первый, самый распространенный способ добавления
#student = Student(name="Max", surname="Brooks", age=24, city="Spb")
#student.save()
#student = Student(name="John", surname="Stones", age=15, city="Spb")
#student.save()
#student = Student(name="Andy", surname="Wings", age=45, city="Manchester")
#student.save()
#student = Student(name="Kate", surname="Brooks", age=34, city="Spb")
#student.save()

#Второй способ добавления
#courses = [
#        {'name':'python','time_start':datetime.date(2021,7,21), 'time_end':datetime.date(2021,8,21)},
#        {'name':'java', 'time_start':datetime.date(2021,7,13),'time_end':datetime.date(2021,8,21)}
#    ]
#Course.insert_many(courses).execute()

#student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]
#Student_course.insert_many(student_courses).execute()


