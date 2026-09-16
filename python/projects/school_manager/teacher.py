from person import Person

class Teacher(Person):
    def __init__(self, name, age, subject): # Constructor to initialize the teacher's name, age, and subject
        super().__init__(name, age) # Call the constructor of the parent class (Person) to initialize name and age
        self.subject = subject

    def display_info(self): # Method to display the teacher's information
        print(f"Teacher Name: {self.name}, Age: {self.age}, Subject: {self.subject}")
