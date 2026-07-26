from Student import Student
from StudentManager import StudentManager
from Admin import Admin

manager = StudentManager()
admin = None

while True:

    print("\n<<Student Grade Analysis System>>")
    print("1. Student Register")
    print("2. Student Login")
    print("3. Admin Register")
    print("4. Admin Login")
    print("5. Exit")

    choice = input("Choose an option: ")

    #Student Register 

    if choice == "1":

        try:
            student_id = int(input("Student ID: "))
            name = input("Student Name: ")

            student = Student(student_id, name)
            manager.add_student(student)

            print("Registration successful!")

        except ValueError as e:
            print(e)

    #Student Login

    elif choice == "2":

        student_id = int(input("Student ID: "))

        student = manager.find_student(student_id)

        if student is None:
            print("Student not found.")
            continue

        while True:

            print(f"\nWelcome {student.name}")
            print("1. Show Grades")
            print("2. Show GPA")
            print("3. Show Level")
            print("4. Show Grade Chart")
            print("5. Logout")

            student_choice = input("Choose: ")

            if student_choice == "1":

                if len(student.grades) == 0:
                    print("No grades available.")
                else:
                    for course, grade in student.grades.items():
                        print(course, ":", grade)

            elif student_choice == "2":

                print(f"GPA: {student.calculate_gpa():.2f}")

            elif student_choice == "3":

                print(student.get_level())

            elif student_choice == "4":

                student.show_grades_chart()

            elif student_choice == "5":

                break

            else:
                print("Invalid option.")

    #Admin Registar
    elif choice == "3":

     if admin is not None:
        print("Admin already exists. Please login.")
        continue

     name = input("Admin Name: ")
     password = input("Password: ")

     admin = Admin(password, name)

     print("Admin registered successfully.")
    
   #Admin Login
    elif choice == "4":

     password = input("Password: ")

     if not admin.login(password):
            print("Wrong password.")
            continue

     while True:

            print("\n<<Admin Panel>>")
            print("1. Add Grade")
            print("2. Edit Grade")
            print("3. Remove Student")
            print("4. Show Best Student")
            print("5. Show Top 3 Students")
            print("6. Show Average GPA")
            print("7. Show Course Average")
            print("8. Show Failed Students")
            print("9. Logout")

            admin_choice = input("Choose: ")

            try:

                if admin_choice == "1":

                    student_id = int(input("Student ID: "))
                    course = input("Course: ")
                    grade = float(input("Grade: "))

                    admin.add_grade(manager, student_id, course, grade)

                    print("Grade added successfully.")

                elif admin_choice == "2":

                    student_id = int(input("Student ID: "))
                    course = input("Course: ")
                    grade = float(input("New Grade: "))

                    admin.edit_grade(manager, student_id, course, grade)

                    print("Grade updated.")

                elif admin_choice == "3":

                    student_id = int(input("Student ID: "))

                    manager.remove_student(student_id)

                elif admin_choice == "4":

                    print(manager.get_best_student())

                elif admin_choice == "5":

                    for student in manager.best_students():
                        print(student)

                elif admin_choice == "6":

                    print("Average GPA:", manager.calculate_average_gpa())

                elif admin_choice == "7":

                    course = input("Course: ")

                    print(manager.get_course_average(course))

                elif admin_choice == "8":

                    failed = manager.failed_students()

                    if len(failed) == 0:
                        print("No failed students.")

                    else:
                        for student in failed:
                            print(student)

                elif admin_choice == "9":

                    break

                else:
                    print("Invalid option.")

            except ValueError as e:
                print(e)

    #Exit

    elif choice == "5":

        print("Goodbye!")
        break

    else:
        print("Invalid option.")