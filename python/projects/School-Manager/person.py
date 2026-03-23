class Person:
    def __init__(self, name, age): # Constructor to initialize the person's name and age
        self.name = name
        self.age = age

    def display_info(self): # Method to display the person's information
        print(f"Name: {self.name}, Age: {self.age}")
