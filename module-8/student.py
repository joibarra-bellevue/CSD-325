"""Jorge Ibarra 
Module 8.2 Assignment 
CSD-325
2/13/2026
This program reads a list of students from a JSON file, prints the original list, adds a new student to the list, prints the updated list, and then writes the updated list back to the JSON file."""

import json
# This function prints each student in the list
def print_students(student_list):
    for student in student_list:
        last = student["L_Name"]
        first = student["F_Name"]
        sid = student["Student_ID"]
        email = student["Email"]

        print(last + ", " + first + " : ID = " + str(sid) + " , Email = " + email)

# Load the JSON file into a Python list
file = open("student.json", "r")
students = json.load(file)
file.close()

print("\nThis is the ORIGINAL student list:\n")
print_students(students)

# Created a new student 
new_student = {
    "F_Name": "Jorge",
    "L_Name": "Ibarra",
    "Student_ID": 21531469,
    "Email": "joibarra@my365.bellevue.edu"
}

# Add the new student to the list
students.append(new_student)

print("\nThis is the UPDATED student list:\n")
print_students(students)

# Write the updated list back to the json file
file = open("student.json", "w")
json.dump(students, file, indent=4)
file.close()

print("\nThe student.json file has been updated.")