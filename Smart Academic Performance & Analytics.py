import csv
import os

FILENAME = "students_data.csv"

# Create file if not exists
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Roll No", "Name", "Math", "Physics", "Chemistry", "Total", "Average", "Grade"])


# Grade Function
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


# Add Student
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    math = float(input("Enter Math Marks: "))
    physics = float(input("Enter Physics Marks: "))
    chemistry = float(input("Enter Chemistry Marks: "))

    total = math + physics + chemistry
    avg = total / 3
    grade = calculate_grade(avg)

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, math, physics, chemistry, total, avg, grade])

    print("✅ Student Added Successfully!\n")


# View All Students
def view_students():
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


# Search Student
def search_student():
    roll_search = input("Enter Roll No to Search: ")
    found = False

    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == roll_search:
                print("Student Found:")
                print(row)
                found = True
                break

    if not found:
        print("❌ Student Not Found")


# Class Analytics
def class_analytics():
    total_students = 0
    total_marks = 0
    highest_avg = 0
    topper = ""

    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            total_students += 1
            avg = float(row[6])
            total_marks += avg

            if avg > highest_avg:
                highest_avg = avg
                topper = row[1]

    if total_students == 0:
        print("No student data available.")
        return

    class_avg = total_marks / total_students

    print("\n📊 Class Analytics")
    print("Total Students:", total_students)
    print("Class Average:", round(class_avg, 2))
    print("Topper:", topper, "with average", highest_avg)


# Main Menu
while True:
    print("\n===== SAPAS MENU =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Class Analytics")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        class_analytics()
    elif choice == "5":
        print("Exiting SAPAS... Goodbye!")
        break
    else:
        print("Invalid Choice. Try Again.")