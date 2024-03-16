from domains.student import Student
from domains.course import Course

students = []
courses = []

def input_students():
    num_students = int(input("Please enter the number of students: "))
    for _ in range(num_students):
        student_id = input("Please enter the student ID: ")
        student_name = input("Please enter the student name: ")
        student_dob = input("Please enter the student date of birth (DoB): ")
        students.append(Student(student_id, student_name, student_dob))

def input_courses():
    num_courses = int(input("Please enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Please enter the course ID: ")
        course_name = input("Please enter the course name: ")
        course_credit = int(input("Please enter the course credit: "))
        courses.append(Course(course_id, course_name, course_credit))

def input_marks():
    course_id_input = input("Please enter the course ID to input marks: ")
    for course in courses:
        if course.id == course_id_input:
            for student in students:
                mark = float(input(f"Please enter the mark for student {student.name}: "))
                student.input_mark(course, mark, course.credit)
