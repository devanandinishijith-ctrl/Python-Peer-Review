
from employee import Employee

class PermanentEmployee(Employee):
    def calculate_salary(self, working_days=30):
        basic = self.basic_salary * working_days / 30
        hra = basic * 0.20
        da = basic * 0.10
        allowances = 0
        gross = basic + hra + da
        deductions = basic * 0.05

        return {
            "basic": basic,
            "hra": hra,
            "da": da,
            "allowances": allowances,
            "gross": gross,
            "deductions": deductions,
            "net": gross - deductions
        }

class ContractEmployee(Employee):
    def calculate_salary(self, working_days=30):
        basic = self.basic_salary * working_days / 30
        hra = 0
        da = 0
        allowances = 0
        gross = basic
        deductions = 0

        return {
            "basic": basic,
            "hra": hra,
            "da": da,
            "allowances": allowances,
            "gross": gross,
            "deductions": deductions,
            "net": gross
        }

class Intern(Employee):
    def calculate_salary(self, working_days=30):
        basic = self.basic_salary * working_days / 30
        hra = 0
        da = 0
        allowances = 0
        gross = basic
        deductions = 0

        return {
            "basic": basic,
            "hra": hra,
            "da": da,
            "allowances": allowances,
            "gross": gross,
            "deductions": deductions,
            "net": gross
        }

def create_employee(emp_id, name, department, designation,
                    employee_type, basic_salary):

    employee_classes = {
        "Permanent": PermanentEmployee,
        "Contract": ContractEmployee,
        "Intern": Intern
    }

    employee_class = employee_classes.get(employee_type)

    if employee_class is None:
        raise ValueError("Invalid employee type.")

    return employee_class(
        emp_id, name, department, designation,
        employee_type, basic_salary
    )