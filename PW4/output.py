def list_courses():
    for course in courses:
        print(f"Course name: {course.name}")

def list_students():
    for student in students:
        print(f"Student name: {student.name}")

def show_marks():
    course_id_input = input("Please enter the course ID to show marks: ")
    for course in courses:
        if course.id == course_id_input:
            for student in students:
                if course in student.marks:
                    print(f"Student {student.name} scored {student.marks[course][0]} in course {course.name}")

def calculate_gpa():
    student_id_input = input("Please enter the student ID to calculate GPA: ")
    for student in students:
        if student.id == student_id_input:
            student.calculate_gpa()
            print(f"Student {student.name} has a GPA of {student.gpa}")

def sort_students():
    students.sort(key=lambda student: student.gpa, reverse=True)
    for student in students:
        print(f"Student {student.name} with GPA {student.gpa}")
