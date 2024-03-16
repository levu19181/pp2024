import domain
from input import input_student_info, input_course_info, input_mark, input_choice, input_num_students, input_num_courses
import zipfile

def main():
    management_system = domain.management.MarkManagement()

    num_of_students = input_num_students()

    for _ in range(num_of_students):
        student_info = input_student_info()
        num_of_courses = input_num_courses()

        student = domain.student.Student(student_info.get_idS(), student_info.get_nameS(), student_info.get_dob())

        for _ in range(num_of_courses):
            course_info = input_course_info()
            mark = input_mark(student_info.get_idS(), course_info.get_idC())

            course = domain.course.Course(course_info.get_idC(), course_info.get_nameC(), course_info.get_credit())
            student.add_course(course, mark)

        management_system.add_student(student)

    with zipfile.ZipFile("student.dat", "w") as zfile:
        zfile.write("file_student")
        zfile.write("file_course")
        zfile.write("file_mark")

    while True:
        print("---------------------------------------------------------")
        print("1. Show the Student List information")
        print("2. Show the Course List")
        print("3. Show Student with mark of chosen Course")
        print("4. Show full")
        print("5. GPA")
        print("0. Exit")
        print("---------------------------------------------------------")
        choice = input_choice()
        if choice == 1:
            management_system.show_student_info()
        elif choice == 2:
            management_system.show_course_info()
        elif choice == 3:
            management_system.show_follow_choose()
        elif choice ==4:
            management_system.show_list()
        elif choice ==5:
            management_system.show_gpa()
        elif choice == 0:
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
