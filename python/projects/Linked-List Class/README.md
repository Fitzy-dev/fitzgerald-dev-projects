🔗 Linked List Project
📌 Overview
This project builds a singly linked list from scratch in Python. It demonstrates how linked lists work internally by creating nodes, connecting them together, adding elements, checking if the list is empty, and removing elements.
The project focuses on understanding pointer-style logic in Python, especially how to move through nodes using current_node and previous_node.


⸻


🧠 Concepts Covered
Classes and objects
Nested classes
Nodes and pointers
Singly linked lists
Traversal
Insertion
Removal
Conditional logic
Data structures fundamentals

⚙️ Features
This linked list implementation includes:
Node class to store:
element
next
LinkedList class with:
head
length
Methods to:
check if the list is empty
add elements to the end
remove an element
track the list length


⸻


🔍 How It Works
Node
Each node stores:
a value (element)
a reference to the next node (next)
LinkedList
The linked list keeps track of:
the first node (head)
how many elements are in the list (length)
Remove Logic
The remove() method:
starts at the head
moves through the list with current_node
tracks the previous node with previous_node
updates links to remove the matching node
This is one of the most important linked list patterns in data structures.

▶️ How to Run

Run the file with Python:
python linked_list_tracker.py
