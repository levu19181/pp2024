# Define functions for inputting student and course information, selecting courses, entering marks, and displaying options and lists.

def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_information():
    print("")
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return student_id, student_name, student_dob

# Define other input functions for courses, selecting a course, inputting marks, and displaying lists.
# Main functionality is wrapped in a while loop to allow for multiple interactions.
# Display options and take user input to execute desired actions.

students = []
courses = []

while True:
    display_options()
    choice = int(input("Enter your choice: "))

    # Execute different actions based on user's choice.
    if choice == 1:
        num_students = input_number_of_students()
        for _ in range(num_students):
            student = input_student_information()
            students.append(student)
        print("")
        print("Student information entered successfully!")
        print("")

    elif choice == 2:
        num_courses = input_number_of_courses()
        for _ in range(num_courses):
            course = input_course_information()
            courses.append(course)
        print("")
        print("Course information entered successfully!")
        print("")

    elif choice == 3:
        course_selected = select_course(courses)
        marks = input_student_marks(students, course_selected)
        print("")
        print("Student marks entered successfully!")
        print("")

    elif choice == 4:
        list_students(students)

    elif choice == 5:
        list_courses(courses)

    elif choice == 6:
        course_selected = select_course(courses)
        show_student_marks(course_selected, marks)

    elif choice == 7:
        break

    else:
        print("Invalid choice. Please try again!")
