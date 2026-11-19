
from file_handler import save_payroll, view_payroll_records


def calculate_payroll(employees):

    emp_id = input("Enter Employee ID: ").strip()

    employee = next(
        (emp for emp in employees if emp.emp_id == emp_id),
        None
    )

    if employee is None:
        print("Employee not found.")
        return

    month = input("Enter payroll month: ").strip()

    if not month:
        print("Month cannot be empty.")
        return

    try:
        working_days = int(input("Enter working days (1-30): "))

        if not 1 <= working_days <= 30:
            print("Working days must be between 1 and 30.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    salary = employee.calculate_salary(working_days)

    print("\n========== PAYSLIP ==========")
    print("Employee ID:", employee.emp_id)
    print("Name:", employee.name)
    print("Department:", employee.department)
    print("Employee Type:", employee.employee_type)
    print("Month:", month)
    print("Working Days:", working_days)

    display_salary(salary)

    record = {
        "emp_id": employee.emp_id,
        "name": employee.name,
        "month": month,
        "working_days": working_days,
        "gross_salary": salary["gross"],
        "deductions": salary["deductions"],
        "net_salary": salary["net"]
    }

    save_payroll(record)


def display_salary(salary):

    print("\n------ SALARY BREAKDOWN ------")

    details = {
        "Basic Salary": salary["basic"],
        "Other Allowances": salary["allowances"],
        "Gross Salary": salary["gross"],
        "Deductions": salary["deductions"],
        "Net Salary": salary["net"]
    }

    for name, amount in details.items():
        print(f"{name}: Rs. {amount:.2f}")

    print("==============================")


def view_payroll():
    view_payroll_records()
