import input_module as inp
import output_module as out

def main():
    while True:
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show marks")
        print("7. Calculate GPA")
        print("8. Sort students by GPA")
        print("9. Exit")
        option = int(input("Please enter your option: "))
        if option == 1:
            inp.input_students()
        elif option == 2:
            inp.input_courses()
        elif option == 3:
            inp.input_marks()
        elif option == 4:
            out.list_courses()
        elif option == 5:
            out.list_students()
        elif option == 6:
            out.show_marks()
        elif option == 7:
            out.calculate_gpa()
        elif option == 8:
            out.sort_students()
        elif option == 9:
            break

if __name__ == "__main__":
    main()
