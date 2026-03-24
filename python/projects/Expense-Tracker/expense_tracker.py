# Jordan Fitzgerald
# 3/24/2026
# Expense Tracker
# This module provides functions to manage expenses, including adding, updating, deleting, and viewing expenses

expenses = {
    'food': [],
    'transportation': [],
    'entertainment': []
}

def add_expense (expenses, category, amount): # Add a new expense to the specified category in the expenses dictionary
    category = category.lower()
    if not category in expenses:
        return f"Category '{category}' does not exist! Cannot add expense."
    else:
        if category in expenses:
            expenses[category].append(amount)
            return f"Expense of {amount} added to {category} category successfully!"

def get_total(expenses, category): # Get the total expenses for a specific category
    category = category.lower()
    if not category in expenses:
        return f"Category '{category}' does not exist! Cannot calculate total."
    else:
        total = sum(expenses[category])
        return f"Total expenses for {category} category: {total}"

def get_all_total(expenses): # Get the total expenses for all categories
    total = 0
    for category in expenses:
        total += sum(expenses[category])
    return f"Total expenses for all categories: {total}"

def highest_category(expenses): # Get the category with the highest total expenses
    highest = None
    highest_total = 0
    for category in expenses:
        total = sum(expenses[category])
        if total > highest_total:
            highest_total = total
            highest = category
    return f"Category with the highest total expenses: {highest} with a total of {highest_total}"

# Example usage of the expense tracker functions
print(add_expense(expenses, "Food", 50))
print(add_expense(expenses, "Transportation", 20))
print(add_expense(expenses, "Entertainment", 30))
print(add_expense(expenses, "Food", 25))

print(get_total(expenses, "Food"))
print(get_total(expenses, "Transportation"))
print(get_total(expenses, "Entertainment"))

print(get_all_total(expenses))
print(highest_category(expenses))
