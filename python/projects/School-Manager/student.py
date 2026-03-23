from person import Person

class Student(Person):
    def __init__(self, name, age, grade): # Constructor to initialize the student's name, age, and grade
        super().__init__(name, age) # Call the constructor of the parent class (Person) to initialize name and age
        self.grade = grade

    def display_info(self): # Override the display_info method to include the student's grade
        super().display_info() # Call the display_info method of the parent class to display name and age
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}")
    
    def is_senior(self): # Method to check if the student is a senior (12th grade)
        return self.grade == "12th Grade"
