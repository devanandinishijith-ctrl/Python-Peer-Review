
from employee_types import create_employee

def add_employee(employees):
    print("\n--- ADD EMPLOYEE ---")

    emp_id = input("Enter Employee ID: ").strip()

    if not emp_id:
        print("Employee ID cannot be empty.")
        return

    if any(emp.emp_id == emp_id for emp in employees):
        print("Employee ID already exists.")
        return

    name = input("Enter Name: ").strip()
    department = input("Enter Department: ").strip()
    designation = input("Enter Designation: ").strip()

    if not all([name, department, designation]):
        print("All fields are required.")
        return

    employee_type = input(
        "Enter Type (Permanent/Contract/Intern): "
    ).strip().title()

    if employee_type not in ["Permanent", "Contract", "Intern"]:
        print("Invalid employee type.")
        return

    try:
        basic_salary = float(input("Enter Monthly Basic Salary: "))

        if basic_salary <= 0:
            print("Salary must be greater than zero.")
            return

    except ValueError:
        print("Enter a valid salary.")
        return

    employee = create_employee(
        emp_id, name, department, designation,
        employee_type, basic_salary
    )

    employees.append(employee)
    print("Employee added successfully.")

def view_employees(employees):
    if not employees:
        print("No employee records found.")
        return

    print("\n--- ALL EMPLOYEES ---")

    for employee in employees:
        employee.display_details()
        print("------------------------")

def search_employee(employees):
    keyword = input(
        "Enter Employee ID, Name or Department: "
    ).strip().lower()

    if not keyword:
        print("Search cannot be empty.")
        return

    results = [
        emp for emp in employees
        if keyword in emp.emp_id.lower()
        or keyword in emp.name.lower()
        or keyword in emp.department.lower()
    ]

    if results:
        for employee in results:
            employee.display_details()
    else:
        print("No matching employee found.")

def update_employee(employees):
    emp_id = input("Enter Employee ID to update: ").strip()

    employee = next(
        (emp for emp in employees if emp.emp_id == emp_id),
        None
    )

    if employee is None:
        print("Employee not found.")
        return

    print("Press Enter to keep the existing value.")

    name = input(f"New Name [{employee.name}]: ").strip()
    department = input(
        f"New Department [{employee.department}]: "
    ).strip()
    designation = input(
        f"New Designation [{employee.designation}]: "
    ).strip()
    salary_input = input(
        f"New Monthly Salary [{employee.basic_salary}]: "
    ).strip()

    try:
        new_salary = (
            float(salary_input) if salary_input
            else employee.basic_salary
        )

        if new_salary <= 0:
            print("Salary must be greater than zero.")
            return

    except ValueError:
        print("Invalid salary.")
        return

    if name:
        employee.name = name

    if department:
        employee.department = department

    if designation:
        employee.designation = designation

    employee.basic_salary = new_salary

    print("Employee updated successfully.")