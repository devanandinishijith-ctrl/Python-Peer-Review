
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

    month = input("Enter payroll month (e.g. September 2026): ").strip()

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

    print("\n------ SALARY BREAKDOWN ------")
    print(f"Basic Salary: Rs. {salary['basic']:.2f}")
    # print(f"HRA: Rs. {salary['hra']:.2f}")
    # print(f"DA: Rs. {salary['da']:.2f}")
    print(f"Other Allowances: Rs. {salary['allowances']:.2f}")
    print(f"Gross Salary: Rs. {salary['gross']:.2f}")
    print(f"Deductions: Rs. {salary['deductions']:.2f}")

    print("------------------------------")
    print(f"NET SALARY: Rs. {salary['net']:.2f}")
    print("==============================")

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

def view_payroll():
    view_payroll_records()