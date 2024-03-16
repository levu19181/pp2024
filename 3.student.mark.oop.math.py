# Importing necessary libraries
import math
import numpy as np

# Defining the Student class
class Student:
    def __init__(self, name, id, DoB):
        self._name = name
        self._id = id
        self._DOB = DoB
        self._gpa = 0

    # Getter methods for student attributes
    def getName(self):
        return self._name
    def getId(self):
        return self._id
    def getDob(self):
        return self._DOB
    def getGpa(self):
        return self._gpa
    
    # Setter method for GPA
    def setGpa(self, gpa):
        self._gpa = gpa
    
    # Method to display student information
    def studentInfo(self):
        print(f"The name of student: {self._name} ")
        print(f"The student id: {self._id}")
        print(f"The date of birth: {self._DOB} ")

# Defining the Course class
class Course:
    def __init__(self, cname, cid):
        self._cname = cname
        self._cid = cid

    # Getter methods for course attributes
    def getCname(self):
        return self._cname
    def getCid(self):
        return self._cid
    
    # Method to display course information
    def courseInfo(self):
        print(f"The name of the course: {self._cname}")
        print(f"The course id: {self._cid}")

# Defining the Grade class
class Grade:
    def __init__(self, studentId, course, mark):
        self._studentID = studentId
        self._course = course
        self._mark = mark

    # Getter methods for grade attributes
    def getId(self):
        return self._studentID
    def getCourse(self):
        return self._course
    def getMark(self):
        return self._mark
    
    # Method to display grade information
    def gradeInfo(self):
        print(f"Mark for student with id {self._studentID} in course {self._course} is {self._mark}")

# Function for inputting student information
def studentInput():
    studentList = []
    numbstu = int(input("Enter the number of students: "))
    for i in range(numbstu):
        name = input("Enter the name of student: ")
        id = input("Enter the student's id: ")
        dob = input("Enter the date of birth: ")
        student = Student(name, id, dob)
        studentList.append(student)
    return studentList

# Function for inputting course information
def courseInput():
    courseList = []
    creditList = []
    numbcourse = int(input("Enter the number of courses: "))
    for i in range(numbcourse):
        coursename = input("Enter the course name: ")
        courseId = input("Enter the course id: ")
        credit = int(input("Enter the number of credit: "))
        course = Course(coursename, courseId)
        courseList.append(course)
        for i in range(numbstu):
            creditList.append(credit)
    return courseList

# Function for inputting grades
def gradeInput(studentList, courseList):
    markList = []
    for i in studentList:
        for j in courseList:
            cre = np.array(creditList)
            mark = float(input(f"Enter the grade for {i.getName()} in course {j.getCname()}: "))
            result = math.floor(mark * 10) / 10
            markList.append(result)
            point = np.array(markList)
        gpa = (np.dot(cre, point)) / np.sum(cre)
        i.setGpa(gpa)
    return markList

# Function to print student information
def Print():
    studentList = studentInput()
    courseList = courseInput()
    gradeInput(studentList, courseList)
    i = 0
    for student in studentList:
        print(f"Name of the student: {student.getName()}")
        for course in courseList:
            print(f"Name of course: {course.getCname()}")
            print(f"The grade for {student.getName()} in course {course.getCname()} is {markList[i]}")
            i += 1
        print(f"GPA of student {student.getName()} is {student.getGpa()}")
          
Print()
