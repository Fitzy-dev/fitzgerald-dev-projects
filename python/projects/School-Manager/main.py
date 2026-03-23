from student import Student
from teacher import Teacher


def main(): # Main function to create instances of Student and Teacher and display their information
    student1 = Student("Alice", 17, "12th Grade")
    student2 = Student("Bob", 16, "11th Grade")

    teacher1 = Teacher("Dr. Smith", 45, "Physics")
    teacher2 = Teacher("Dr. Johnson", 50, "Chemistry")

    student1.display_info()
    student2.display_info()
    teacher1.display_info()
    teacher2.display_info()
    print("All students and teachers have been displayed.")

    if __name__ == "__main__": # Check if the script is being run directly (instead of imported as a module) and call the main function 
        main()
