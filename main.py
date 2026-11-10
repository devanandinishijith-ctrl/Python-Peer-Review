
from employee_operations import (
    add_employee,
    view_employees,
    search_employee,
    update_employee
)

from salary import calculate_payroll, view_payroll
from file_handler import load_employees, save_employees

def main():
    employees = load_employees()

    while True:
        print("\n===================================")
        print("              PAYNEXA")
        print("       EMPLOYEE PAYROLL SYSTEM")
        print("===================================")

        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Calculate Salary")
        print("6. View Payroll Records")
        print("7. Save Employee Records")
        print("8. Exit")

        print("===================================")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_employee(employees)
            save_employees(employees)

        elif choice == "2":
            view_employees(employees)

        elif choice == "3":
            search_employee(employees)

        elif choice == "4":
            update_employee(employees)
            save_employees(employees)

        elif choice == "5":
            calculate_payroll(employees)

        elif choice == "6":
            view_payroll()

        elif choice == "7":
            save_employees(employees)

        elif choice == "8":
            save_employees(employees)
            print("Thank you for using PAYNEXA!")
            break

        else:
            print("Invalid choice. Please enter 1-8.")

if __name__ == "__main__":
    main()