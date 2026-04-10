# Rectangle Class Project (C++)

## 📌 Overview
This project demonstrates Object-Oriented Programming (OOP) concepts in C++ by implementing a `Rectangle` base class and a `Square` derived class. It focuses on class design, inheritance, and separation of code into multiple files using headers and implementation files.

---

## 🧠 Concepts Used
- Classes and Objects
- Constructors (Default)
- Accessors (Getters)
- Mutators (Setters)
- Inheritance
- Function Prototypes
- Header Files (`.h`)
- Implementation Files (`.cpp`)
- Separate compilation

---

## 📂 Project Structure
Rectangle-Class-Project/
│── main.cpp          # Runs the program
│── Rectangle.h       # Class declarations
│── Rectangle.cpp     # Class definitions
│── README.md         # Project documentation

---

## ⚙️ How It Works

### 🔷 Rectangle Class
The `Rectangle` class includes:
- Private variables:
  - `length`
  - `width`
- Public methods:
  - `set(int l, int w)` → sets dimensions
  - `get_Area()` → returns area
  - `get_Length()` → returns length
  - `get_Width()` → returns width
  - `displayInfo()` → prints rectangle details

---

### 🔶 Square Class (Derived)
The `Square` class inherits from `Rectangle` and:
- Uses a single value for both length and width
- Overrides the `set()` method
- Adds:
  - `get_Perimeter()` → calculates perimeter

---

### ▶️ Main Program
- Prompts the user to enter the side length
- Creates a `Square` object
- Sets the value using the `set()` method
- Displays:
  - Length
  - Width
  - Area
  - Perimeter

---

## ▶️ How to Run

### Compile:
```bash
g++ main.cpp Rectangle.cpp -o program
./program
