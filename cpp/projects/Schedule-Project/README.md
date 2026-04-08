📘 Schedule Project (C++)

📄 File Name

schedule.cpp

⸻

🧾 Overview

This program allows the user to create and manage a schedule of courses. The user is prompted to enter information for multiple courses (minimum of 3), and the program stores this data using an array (vector) of objects.

Each course is represented by a Schedule class that contains details such as the course name, duration, location, and credit hours.

⸻

✨ Features
    •    Prompts user to enter number of courses (minimum of 3)
    •    Stores multiple course objects using a vector
    •    Uses constructors, accessors, and mutators
    •    Allows user to input:
    •    Course name
    •    Duration (in minutes)
    •    Location
    •    Credit hours
    •    Displays all course information in a clean format
    •    Prevents invalid input (less than 3 courses)

⸻

🧠 Concepts Used
    •    Object-Oriented Programming (OOP)
    •    Classes and Objects
    •    Constructors (default and parameterized)
    •    Accessors (getters)
    •    Mutators (setters)
    •    Vectors (dynamic arrays)
    •    Loops (for, while)
    •    User input/output (cin, cout)
    •    getline() for string input
    •    Input buffer handling (cin.ignore)
    •    Data encapsulation

⸻

⚙️ How to Run the Program

1. Compile the program
   g++ schedule.cpp -o schedule
2. Run the program
   ./schedule
