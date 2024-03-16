# Define a Student class representing students with ID, name, date of birth, and marks.
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}  # Dictionary to store marks for each course.

    # Method to add a mark for a course.
    def add_mark(self, course, mark):
        self.marks[course] = mark 

# Define a Course class representing courses with ID and name.
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Define a School class managing students and courses.
class School:
    def __init__(self):
        self.students = []  # List to store student objects.
        self.courses = []   # List to store course objects.

    # Method to input student details.
    def input_students(self):
        total_student = int(input("Enter the number of students: "))
        for _ in range(total_student):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (DD/MM/YYYY): ")
            self.students.append(Student(id, name, dob))

    # Method to input course details.
    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses.append(Course(id, name))

    # Method to input marks for students in a course.
    def input_marks(self):
        course_id = input("Enter the course ID to input marks for: ")
        for course in self.courses:
            if course.id == course_id:
                for student in self.students:
                    mark = input(f"Enter mark for student {student.name}: ")
                    student.add_mark(course.name, mark)

    # Method to display student details.
    def show_students(self):
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}, DOB: {student.dob}")

    # Method to display student marks.
    def show_student_marks(self):
        for student in self.students:
            print(f"Student: {student.name}")
            for course, mark in student.marks.items():
                print(f"Course: {course}, Mark: {mark}")

    # Method to display course details.
    def show_courses(self):
        for course in self.courses:
            print(f"ID: {course.id}, Name: {course.name}")

# Main function to interact with the school system.
def main():
    school = School()  # Create a School object.
    school.input_students()  # Input student details.
    school.input_courses()   # Input course details.
    
    # Display options and execute chosen functionality until user exits.
    while True:
        print('''
        Welcome to the Student Management System:
            0. Exit
            1. Input marks for students in a course
            2. Show list of students
            3. Show list of courses
            4. Show student marks
            ''')
        
        option = int(input("Enter your choice: "))

        if option == 0:
            break
        elif option == 1:
            school.input_marks()
        elif option == 2:
            school.show_students()
        elif option == 3:
            school.show_courses()
        elif option == 4:
            school.show_student_marks()
        else:
            print("Invalid choice. Please enter a number between 0 and 4.")

# Call the main function if the script is executed.
if __name__ == "__main__":
    main()
