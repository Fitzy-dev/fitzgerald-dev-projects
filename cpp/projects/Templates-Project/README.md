📌 Maximum & Minimum Template Project

This project demonstrates the use of function templates in C++ by implementing two generic functions:
    •    minimum() → returns the smaller of two values
    •    maximum() → returns the larger of two values

Both functions are written using templates so they can work with multiple data types without rewriting code.

⸻

🧠 Concepts Covered
    •    Function Templates (template <typename T>)
    •    Generic Programming
    •    Code Reusability
    •    Conditional Logic
    •    Multiple Data Type Handling
⚙️ How It Works
    1.    The template functions are defined at the top of the file:
    •    minimum(T a, T b)
    •    maximum(T a, T b)
    2.    The main() function:
    •    Calls both functions with different data types
    •    Displays the results
    3.    The compiler automatically determines the correct type for each function call.
▶️ How to Compile & Run

Compile: g++ temp_min-max.cpp -o program
RUN: ./program
