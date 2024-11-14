
# employee_management
class Employee:
    """Represents an employee with basic details."""
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def update_employee(self, name=None, department=None, salary=None):
        """Update employee details if provided."""
        if name:
            self.name = name
        if department:
            self.department = department
        if salary:
            self.salary = salary

    def __str__(self):
        """String representation of the employee."""
        return f"ID: {self.emp_id}, Name: {self.name}, Dept: {self.department}, Salary: {self.salary}"


class EmployeeManagementSystem:
    """System to manage multiple employees."""
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, department, salary):
        """Add a new employee to the system."""
        employee = Employee(emp_id, name, department, salary)
        self.employees.append(employee)
        print(f"Employee {name} added successfully.")

    def remove_employee(self, emp_id):
        """Remove an employee by ID."""
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print(f"Employee {emp_id} removed successfully.")
                return
        print(f"Employee with ID {emp_id} not found.")

    def update_employee(self, emp_id, name=None, department=None, salary=None):
        """Update an employee's details by ID."""
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.update_employee(name, department, salary)
                print(f"Employee {emp_id} updated successfully.")
                return
        print(f"Employee with ID {emp_id} not found.")

    def search_employee(self, emp_id):
        """Search for an employee by ID."""
        for employee in self.employees:
            if employee.emp_id == emp_id:
                print(employee)
                return
        print(f"Employee with ID {emp_id} not found.")

    def list_employees(self):
        """List all employees."""
        if not self.employees:
            print("No employees in the system.")
            return
        for employee in self.employees:
            print(employee)

    def run(self):
        """Run the system and handle user input."""
        while True:
            print("\nEmployee Management System")
            print("1. Add Employee")
            print("2. Remove Employee")
            print("3. Update Employee")
            print("4. Search Employee")
            print("5. List Employees")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Employee Name: ")
                department = input("Enter Department: ")
                salary = input("Enter Salary: ")
                self.add_employee(emp_id, name, department, salary)

            elif choice == '2':
                emp_id = input("Enter Employee ID to remove: ")
                self.remove_employee(emp_id)

            elif choice == '3':
                emp_id = input("Enter Employee ID to update: ")
                name = input("Enter new name (or press Enter to skip): ")
                department = input("Enter new department (or press Enter to skip): ")
                salary = input("Enter new salary (or press Enter to skip): ")
                self.update_employee(emp_id, name if name else None, department if department else None, salary if salary else None)

            elif choice == '4':
                emp_id = input("Enter Employee ID to search: ")
                self.search_employee(emp_id)

            elif choice == '5':
                self.list_employees()

            elif choice == '6':
                print("Exiting Employee Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please select again.")


if __name__ == "__main__":
    # Create and run the employee management system
    system = EmployeeManagementSystem()
    system.run()
