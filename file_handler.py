
import csv
import os

from employee_types import create_employee

EMPLOYEE_FILE = "employees.csv"
PAYROLL_FILE = "payroll.csv"

EMPLOYEE_FIELDS = [
    "emp_id", "name", "department", "designation",
    "employee_type", "basic_salary"
]

PAYROLL_FIELDS = [
    "emp_id", "name", "month", "working_days",
    "gross_salary", "deductions", "net_salary"
]

def save_employees(employees):
    try:
        with open(EMPLOYEE_FILE, "w", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=EMPLOYEE_FIELDS
            )

            writer.writeheader()

            for emp in employees:
                writer.writerow({
                    "emp_id": emp.emp_id,
                    "name": emp.name,
                    "department": emp.department,
                    "designation": emp.designation,
                    "employee_type": emp.employee_type,
                    "basic_salary": emp.basic_salary
                })

        print("Employee records saved successfully.")

    except (OSError, csv.Error) as error:
        print("Error saving employees:", error)

def load_employees():
    employees = []

    if not os.path.exists(EMPLOYEE_FILE):
        return employees

    try:
        with open(EMPLOYEE_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames or not set(
                EMPLOYEE_FIELDS
            ).issubset(reader.fieldnames):
                print("Employee CSV has an invalid format.")
                return employees

            for row in reader:
                try:
                    employee = create_employee(
                        row["emp_id"],
                        row["name"],
                        row["department"],
                        row["designation"],
                        row["employee_type"],
                        float(row["basic_salary"])
                    )

                    if not any(
                        emp.emp_id == employee.emp_id
                        for emp in employees
                    ):
                        employees.append(employee)

                except (ValueError, TypeError, KeyError):
                    print("Skipping an invalid employee record.")

    except (OSError, csv.Error) as error:
        print("Error loading employees:", error)

    return employees

def save_payroll(record):
    try:
        file_exists = os.path.exists(PAYROLL_FILE)
        write_header = (
            not file_exists or os.path.getsize(PAYROLL_FILE) == 0
        )

        with open(PAYROLL_FILE, "a", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=PAYROLL_FIELDS
            )

            if write_header:
                writer.writeheader()

            writer.writerow(record)

        print("Payroll record saved successfully.")

    except (OSError, csv.Error) as error:
        print("Error saving payroll:", error)

def view_payroll_records():
    if not os.path.exists(PAYROLL_FILE):
        print("No payroll records found.")
        return

    try:
        with open(PAYROLL_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            print("\n--- PAYROLL HISTORY ---")

            found = False

            for record in reader:
                found = True
                print(
                    f"ID: {record['emp_id']} | "
                    f"Name: {record['name']} | "
                    f"Month: {record['month']} | "
                    f"Net Salary: Rs. {float(record['net_salary']):.2f}"
                )

            if not found:
                print("No payroll records found.")

    except (OSError, csv.Error, ValueError, KeyError) as error:
        print("Error reading payroll:", error)