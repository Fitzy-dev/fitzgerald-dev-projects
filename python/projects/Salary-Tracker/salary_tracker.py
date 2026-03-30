# Jordan Fitzgerald
# 3/30/2026
# Salary Tracker
# This module implements a simple salary tracking system with an Employee class to represent employees and their salary information. The Employee class allows users to create employee instances with a name, level, and salary. It provides methods to update the employee's name, level, and salary while enforcing certain constraints. The main function demonstrates the functionality of the salary tracker by creating an employee instance, displaying its information, and updating the employee's level and salary.
class Employee:
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }
    # The __init__ method initializes an Employee instance with a name and level. It checks if the provided name and level are valid strings and if the level is one of the predefined levels in the _base_salaries dictionary. If the inputs are valid, it sets the employee's name, level, and salary based on the base salary for the given level.
    def __init__(self, name, level):
        if not (isinstance(name, str) and isinstance(level, str)):
            raise TypeError("'name' and 'level' attribute must be of type 'str'.")
        if level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")
        self._name = name
        self._level = level
        self._salary = Employee._base_salaries[level]
    # The __str__ method provides a string representation of the Employee instance that includes the employee's name and level. This method is useful for displaying the employee's information in a readable format when printed.
    def __str__(self):
        return f'{self.name}: {self.level}'
    # The __repr__ method provides a string representation of the Employee instance that includes the employee's name and level. This method is useful for debugging and provides a clear representation of the employee's information when printed or displayed in a list.
    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"
    # The name property allows users to get and set the employee's name. The setter method checks if the new name is a string and updates the employee's name if it is valid, printing a confirmation message.
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{self.name}'.")
    # The level property allows users to get and set the employee's level. The setter method checks if the new level is a valid string and if it is different from the current level. It also ensures that the new level is not lower than the current level. If the new level is valid, it updates the employee's salary to the base salary of the new level and prints a confirmation message.
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        if new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")
        if Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError(f"Cannot change to lower level.")
        print(f"'{self.name}' promoted to '{new_level}'.")
        self.salary = Employee._base_salaries[new_level]
        self._level = new_level
    # The salary property allows users to get and set the employee's salary. The setter method checks if the new salary is a number and if it is higher than the minimum salary for the employee's current level. If the new salary is valid, it updates the employee's salary and prints a confirmation message.
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        if new_salary <= Employee._base_salaries[self.level]:
            raise ValueError(f'Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}.')
        self._salary = new_salary
        print(f'Salary updated to ${self.salary}.')
# The main function demonstrates the functionality of the Employee class by creating an instance of an employee, displaying its information, and updating the employee's level and salary. It creates an employee named "Charlie Brown" with the level "trainee", prints the employee's information and base salary, promotes Charlie Brown to "junior", and then creates another employee named "John Doe" with the level "mid-level". It prints John Doe's information and base salary, updates John Doe's salary to $3500, promotes him to "senior", and prints his updated information.
def main():
    charlie_brown = Employee('Charlie Brown', 'trainee')
    print(charlie_brown)
    print(f'Base salary: ${charlie_brown.salary}')
    charlie_brown.level = 'junior'

    john_doe = Employee('John Doe', 'mid-level')
    print(john_doe)
    print(f'Base salary: ${john_doe.salary}')
    john_doe.salary = 3500
    john_doe.level = 'senior'
    print(john_doe)

if __name__ == "__main__":
    main()
