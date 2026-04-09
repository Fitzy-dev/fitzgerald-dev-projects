📊 Log File Analyzer (Python)

📄 File Name

log_file_analyzer.py

⸻

🧾 Overview

This project simulates a basic log monitoring system used in real-world applications such as backend services, cloud systems, and cybersecurity tools.

The program analyzes a list of log messages, identifies patterns, counts occurrences, detects duplicates, flags important events, and evaluates system health based on error frequency.

⸻

✨ Features
    •    Counts occurrences of each log type (ERROR, WARNING, INFO)
    •    Identifies and prints flagged logs (ERROR and WARNING)
    •    Displays timestamps alongside flagged logs
    •    Finds the most common log message
    •    Displays the top 3 most frequent log messages
    •    Detects duplicate log entries
    •    Calculates error rate
    •    Determines overall system status (OK, WARNING, CRITICAL)

⸻

🧠 Concepts Used
    •    Dictionaries (frequency counting)
    •    Sets (duplicate detection)
    •    Lists and list operations
    •    String parsing (split)
    •    Sorting with lambda
    •    Looping and conditional logic
    •    Data analysis techniques
    •    Basic monitoring and security concepts

⸻

⚙️ How to Run the Program

1. Ensure Python is installed
   python --version
2. Run the program
   python log_file_analyzer.py
