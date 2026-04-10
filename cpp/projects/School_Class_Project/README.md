🏫 School Class Hierarchy Project

Author: Jordan Fitzgerald
Date: 4/10/2026
Language: C++

⸻

📌 Project Overview

This project demonstrates object-oriented programming (OOP) concepts in C++ using a class hierarchy.

The program models a school system with three levels:
    •    School (Base Class)
    •    Division (Derived Class)
    •    Department (Derived from Division)

It uses:
    •    Inheritance
    •    Encapsulation
    •    Constructors
    •    Function prototypes
    •    Separate header and implementation files

⸻

🧱 Class Structure

1. School (Base Class)

Represents a school with:
    •    Name
    •    Location
    •    Tuition

Key Methods:
    •    setLocation()
    •    setTuition()
    •    getName()
    •    getLocation()
    •    getTuition()
    •    displayInfo()

⸻

2. Division (Derived from School)

Represents a division within a school.

Additional Attribute:
    •    Division Name

Key Methods:
    •    getDivisionName()
    •    displayDivisionInfo()

⸻

3. Department (Derived from Division)

Represents a department within a division.

Additional Attributes:
    •    Department Name
    •    Number of Faculty
    •    Number of Students

Key Methods:
    •    setNumFaculty()
    •    setNumStudents()
    •    getDepartmentName()
    •    getNumFaculty()
    •    getNumStudents()
    •    displayDepartmentInfo()

⸻

📂 File Structure
School-Class-Project/
│
├── main.cpp          # Main program execution
├── School.h          # Class declarations (header file)
├── School.cpp        # Function definitions
└── README.md         # Project documentation
⚙️ How It Works
    1.    A Department object is created.
    2.    It inherits:
    •    School properties (name, location, tuition)
    •    Division properties (division name)
    3.    Additional department details are set:
    •    Faculty count
    •    Student count
    4.    All information is displayed using a chain of inherited functions.

⸻

▶️ How to Compile & Run

Compile:
g++ main.cpp School.cpp -o program
./program
