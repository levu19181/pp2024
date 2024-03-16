class MarkManagement:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def show_list(self):
        for student in self.student_list:
            student.show_full_info()

    def show_student_info(self):
        print("{:<15} {:<15} {:<15}".format("Student ID", "Student Name", "Date of Birth"))
        for student in self.student_list:
            print("{:<15} {:<15} {:<15}".format(student.get_id(), student.get_name(), student.get_dob()))

    def show_course_info(self):
        print("{:<15} {:<15} {:<15}".format("Course ID", "Course Name", "Credits"))
        for student in self.student_list:
            for course_data in student.get_courses():
                course = course_data["Course"]
                print("{:<15} {:<15} {:<15}".format(course.get_id(), course.get_name(), course.get_credit()))

    def show_student_marks(self):
        student_id = input("Enter Student ID: ")
        found = False
        for student in self.student_list:
            if student.get_id() == student_id:
                course_id = input("Enter Course ID: ")
                for course_data in student.get_courses():
                    course = course_data["Course"]
                    mark = course_data["Mark"]
                    if course.get_id() == course_id:
                        found = True
                        print("\nMark for {} in {}: {}".format(student.get_name(), course.get_name(), mark))
        if not found:
            print("Student or Course not found.")

    def show_gpa(self):
        sorted_students = sorted(self.student_list, key=lambda x: x.calculate_gpa(), reverse=True)
        print("{:<15} {:<15} {:<15}".format("Student ID", "Student Name", "GPA"))
        for s in sorted_students:
            print("{:<15} {:<15} {:<15}".format(s.get_id(), s.get_name(), s.calculate_gpa()))
