#---------------------------------------------
# Title: Module 5, Lab 3
# Desc: An activity to practice working with exceptions
# Change Log (who, when, what)
#       KHarrison, 06/06/2024, created script
#---------------------------------------------

# imports #

import json

# constants #

FILE_NAME: str = "mylabdata.json"

MENU: str = '''
------------------Student GPA------------------
    Select from the following menu:
        1. Show current student data
        2. Enter new student data
        3. Save data to a file
        4. Exit the program
-----------------------------------------------
'''

# global variables #

student_first_name: str = ""
student_last_name: str = ""
student_gpa: float = 0.0
message: str = ""
menu_choice: str = ""
student_data: dict = {}
students: list = []
file_data: str = ""
file = None


# functions and execution #

while True:
    print(MENU)
    menu_choice = input("Please choose an option: ")
    print()


    if menu_choice == "1":
        try:
            with open(FILE_NAME, "r") as file:
                students = json.load(file)
                for student_row in students:
                    student_first_name = student_row["First Name"]
                    student_last_name = student_row["Last Name"]
                    student_gpa = student_row["GPA"]
                    if student_gpa >= 4.0:
                        message = f"{student_first_name} {student_last_name} earned an A with a {student_gpa} GPA"
                    elif student_gpa >= 3.0:
                        message = f"{student_first_name} {student_last_name} earned a B with a {student_gpa} GPA"
                    elif student_gpa >= 2.0:
                        message = f"{student_first_name} {student_last_name} earned a C with a {student_gpa} GPA"
                    elif student_gpa >= 1.0:
                        message = f"{student_first_name} {student_last_name} earned a D with a {student_gpa} GPA"
                    else:
                        message = f"{student_first_name} {student_last_name} earned an F with a {student_gpa} GPA"
                    print(message)
        except FileNotFoundError as file_not_found_details:
            print("Text file must exist before running this script!\n")
            print("-- Technical Error Message --")
            print(file_not_found_details,file_not_found_details.__doc__, type(file_not_found_details),sep = "\n")
        except Exception as unspecified_error_details:
            print("There was a non-specific error.\n")
            print("-- Technical Error Message --")
            print(unspecified_error_details,unspecified_error_details.__doc__, type(unspecified_error_details),sep = "\n")
        
    
    elif menu_choice == "2":
        try:    
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            
            try:    
                student_gpa = float(input("What is the student's GPA? "))
            except ValueError:
                raise ValueError("GPA must be a numeric value.")    
                
            student_data = {"First Name": student_first_name, "Last Name": student_last_name, "GPA": student_gpa}
            students.append(student_data)

        except ValueError as value_error_details:
            print(value_error_details)
            print(" -- Technical Error Message -- ")
            print(value_error_details.__doc__)
        except Exception as unspecified_error_details:
            print("There was a non-specific error.\n")
            print("-- Technical Error Message --")
            print(unspecified_error_details,unspecified_error_details.__doc__, type(unspecified_error_details),sep = "\n")
    
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                json.dump(students, file)

        except TypeError as type_error_details:
            print("Please check that the data is a valid JSON format\n")
            print(" -- Technical Error Message -- ")
            print("Built-in Python error info: ")
            print(type_error_details, type_error_details.__doc__, type(type_error_details), sep = "\n")


    elif menu_choice == "4":
        break

    else:
        print("Please enter a choice from options 1-4")
        continue