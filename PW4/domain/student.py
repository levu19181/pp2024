import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0

    def input_mark(self, course, mark, credit):
        self.marks[course] = (math.floor(mark * 10) / 10, credit)

    def calculate_gpa(self):
        if not self.marks:
            self.gpa = 0
        else:
            total_marks = np.array([mark for mark, credit in self.marks.values()])
            total_credits = np.array([credit for mark, credit in self.marks.values()])
            self.gpa = np.average(total_marks, weights=total_credits)
