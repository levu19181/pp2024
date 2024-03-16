import numpy as np

class Student:
    def __init__(self, student_id, student_name, dob):
        self.student_id = student_id
        self.student_name = student_name
        self.dob = dob
        self.courses = []

    def get_name(self):
        return self.student_name
    
    def get_id(self):
        return self.student_id

    def get_dob(self):
        return self.dob
    
    def add_course(self, course, mark):
        self.courses.append({"Course": course, "Mark": mark})

    def calculate_gpa(self):
        marks = np.array([course["Mark"] for course in self.courses])
        credits = np.array([course["Course"].get_credit() for course in self.courses])
        
        total_mark = np.sum(marks * credits)
        total_credit = np.sum(credits)

        average_gpa = np.round(total_mark / total_credit, 1)
        return average_gpa

    def show_full_info(self):
        print("\n{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Student ID", "Name", "Date of Birth", "Course ID", "Course Name", "Mark"))
        for data in self.courses:
            course = data["Course"]
            mark = data["Mark"]
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
                self.get_id(), self.get_name(), self.get_dob(), course.get_id(), course.get_name(), mark))
        print()
