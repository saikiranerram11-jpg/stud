employees = {}

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        employees[emp_id] = name
        print("Employee Successfully!")

    elif choice == "2":
        print("\nEmployee List:")
        for emp_id, name in employees.items():
            print(emp_id, "-", name)

    elif choice == "":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")
