🖥️ RISC-V Processor Simulator (Python)
Author: Jordan Fitzgerald


⸻


📌 Overview
This project simulates a simplified RISC-V processor in Python. The program accepts hexadecimal instructions, converts them into binary, decodes the instruction fields, and executes them while updating register values.
It demonstrates how a CPU interprets and executes machine-level instructions step by step.


⸻


🧠 Concepts Covered
Computer architecture fundamentals
Instruction decoding
Bit manipulation (shifting and masking)
Binary and hexadecimal conversion
Register operations
Memory access simulation
Branching and control flow
RISC-V instruction formats (R, I, S, B types)


⸻


⚙️ Features
The simulator supports the following RISC-V instructions:
🔹 Arithmetic & Logic (R-Type)
add
sub
and
or
xor
🔹 Immediate (I-Type)
addi
🔹 Memory Operations
ld (load)
sd (store)
🔹 Branching (B-Type)
beq (branch if equal)
bne (branch if not equal)
🧪 Skills Practiced
Understanding how CPUs execute instructions
Working with low-level data representations
Debugging complex logic
Translating machine code into human-readable instructions
Simulation of real-world computer systems


⸻


🚀 Future Improvements
Add more RISC-V instructions (e.g., mul, div)
Implement full memory system
Add pipeline simulation
Create a graphical interface
Support instruction files instead of manual input


⸻


📎 Notes
Register x0 is always set to 0 (RISC-V rule)
Memory is simulated using a Python dictionary
Program counter (PC) updates after each instruction

