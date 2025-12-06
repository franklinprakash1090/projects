students = []


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    marks = float(input("Enter Marks: "))

    student = {"roll": roll, "name": name, "dept": dept, "marks": marks}
    students.append(student)
    print("Student Added Successfully!\n")


def display_students():
    if not students:
        print("No student records available.\n")
        return
    print("---- Student Records ----")
    for s in students:
        print(
            f"Roll: {s['roll']}, Name: {s['name']}, Dept: {s['dept']}, Marks: {s['marks']}"
        )
    print()


def search_student():
    roll = input("Enter Roll Number to Search: ")
    for s in students:
        if s["roll"] == roll:
            print("Student Found:")
            print(f"Name: {s['name']}, Dept: {s['dept']}, Marks: {s['marks']}\n")
            return
    print("Student Not Found!\n")


def update_student():
    roll = input("Enter Roll Number to Update: ")
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter New Name: ")
            s["dept"] = input("Enter New Department: ")
            s["marks"] = float(input("Enter New Marks: "))
            print("Record Updated Successfully!\n")
            return
    print("Student Not Found!\n")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Record Deleted Successfully!\n")
            return
    print("Student Not Found!\n")


while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting System...")
        break
    else:
        print("Invalid Choice! Try Again.\n")
