# getting list for storing the student details
student_names = []
student_ages = []
student_grades = []

def add_Student():
    student_name = input("Enter the student name: ")
    student_age = input("Enter the student age: ")
    student_grade = input("Enter the student grade: ")
    student_names.append(student_name)
    student_ages.append(student_age)
    student_grades.append(student_grade)
    print("Student added successfully")

def search_Student():
    student_name = input("Enter the student name: ")
    if student_name in student_names:
        index = student_names.index(student_name)
        print(f"Name: {student_names[index]}, Age: {student_ages[index]}, Grade: {student_grades[index]}")
    else:
        print("Student not found")

def delete_Student():
    student_name = input("Enter the student name: ")
    if student_name in student_names:
        index = student_names.index(student_name)
        student_names.pop(index)
        student_ages.pop(index)
        student_grades.pop(index)
        print("Student deleted successfully")
    else:
        print("Student not found")

def update_Student():
    student_name = input("Enter the student name: ")
    if student_name in student_names:
        index = student_names.index(student_name)
        student_names[index] = input("Enter the new student name: ")
        student_ages[index] = input("Enter the new student age: ")
        student_grades[index] = input("Enter the new student grade: ")
        print("Student updated successfully")
    else:
        print("Student not found")

def display_Students():
    for i in range(len(student_names)):
        print(f"Name: {student_names[i]}, Age: {student_ages[i]}, Grade: {student_grades[i]}")

while True:
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Display Students")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_Student()
    elif choice == 2:
        search_Student()
    elif choice == 3:
        delete_Student()
    elif choice == 4:
        update_Student()
    elif choice == 5:
        display_Students()
    elif choice == 6:
        break
    else:
        print("Invalid choice")