
class Employee:
    def __init__(self, emp_id, name, department, designation,
                 employee_type, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation
        self.employee_type = employee_type
        self.basic_salary = float(basic_salary)

    def display_details(self):
        print("\nEmployee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Designation:", self.designation)
        print("Employee Type:", self.employee_type)
        print("Monthly Basic Salary: Rs.", self.basic_salary)

    def calculate_salary(self, working_days=30):
        raise NotImplementedError(
            "Salary calculation must be defined in the child class."
        )
