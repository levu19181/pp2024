import math
import domain

file_student = "student.txt"
file_course = "course.txt"
file_mark = "mark.txt"

def input_student_info():
    id_student = input("Enter Student's ID: ")
    name_student = input("Enter Student's name: ")
    dob_student = input("Enter Student's date of birth (DoB): ")
    student_info = f"{id_student}, {name_student}, {dob_student}\n"
    with open(file_student, 'a') as f:
        f.write(student_info)
    return domain.student.Student(id_student, name_student, dob_student)

def input_course_info():
    id_course = input("Enter the Course's ID: ")
    name_course = input("Enter the Course's name: ")
    credit = int(input("Enter the number of credits for the course: "))
    course_info = f"{id_course}, {name_course}, {credit}\n"
    with open(file_course, 'a') as f:
        f.write(course_info)
    return domain.course.Course(id_course, name_course, credit)

def input_mark(student_id, course_id):
    mark = float(input("Enter the mark for this Course: "))
    mark_info = f"{student_id}, {course_id}, {mark}\n"
    with open(file_mark, 'a') as f:
        f.write(mark_info)
    return math.floor(mark * 10) / 10

def input_choice():
    choice = int(input("Enter your choice: "))
    return choice

def input_num_students():
    num_students = int(input("Enter the number of students: "))
    return num_students

def input_num_courses():
    num_courses = int(input("Enter the number of courses: "))
    return num_courses
