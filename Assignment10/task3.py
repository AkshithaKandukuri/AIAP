class Employee:
    """
    Represents an employee with a name and salary.
    Provides functionality to increase salary and display employee info.
    """

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def increase_salary(self, percent):
        """Increase the employee's salary by a given percentage."""
        self._salary += self._salary * (percent / 100)

    def display_info(self):
        """Print formatted employee details."""
        print(f"Employee: {self._name} | Salary: ₹{self._salary:,.2f}")


# ---- INPUT FUNCTIONS ----

def main():
    name = input("Enter employee name: ")

    try:
        salary = float(input("Enter salary: "))
    except ValueError:
        print("Invalid salary. Please enter a numeric value.")
        return

    try:
        percent = float(input("Enter salary increase %: "))
    except ValueError:
        print("Invalid percentage. Please enter a number.")
        return

    emp = Employee(name, salary)
    emp.increase_salary(percent)

    print("\nUpdated Employee Info:")
    emp.display_info()


# Run the program
main()
