# Login Attempts Analyzer

## 📌 Overview

This project is a Python function-based program that analyzes failed login attempts and returns a message based on a maximum attempt limit. It uses conditional logic to report a safe status, issue a warning, or indicate that the account has reached the lockout threshold.

---

## 🚀 Features

- Accepts the number of failed login attempts and the maximum allowed attempts
- Calculates the ratio of failed attempts to the maximum
- Returns feedback based on three conditions:
  - **Account Locked:** Failed attempts meet or exceed the maximum
  - **Warning:** Failed attempts reach at least 50% of the maximum but remain below the limit
  - **Safe:** Failed attempts are below 50% of the maximum
- Displays the number of remaining attempts when the status is safe
- Includes a `main()` function demonstrating all three outcomes

The program returns status messages; it does not connect to an account system or enforce account locking.

---

## 🧠 Concepts Used

- Python functions and parameters
- Conditional statements (`if`, `elif`, `else`)
- Arithmetic and comparison operators
- Type conversion using `float()` and `str()`
- String concatenation
- Return values
- Program entry point using `if __name__ == "__main__"`

---

## 🛠️ Usage Example

```python
print(analyze_login_attempts(3, 5))
print(analyze_login_attempts(8, 5))
print(analyze_login_attempts(1, 5))
```

Use a nonnegative number of failed attempts and a positive maximum. The function does not validate inputs, and a maximum of `0` causes a division-by-zero error.

---

## 📋 Example Output

```text
Warning: You have failed 3 login attempts
Account Locked. You have exceeded the maximum number of login attempts.
Safe. You have 4 attempts remaining.
```

---

## 🎯 Purpose

This project reinforces foundational programming skills, including writing reusable functions, evaluating conditions, performing calculations, and returning clear feedback based on input values.

---

## 👨‍💻 Author

Jordan Fitzgerald