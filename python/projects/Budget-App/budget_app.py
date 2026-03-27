# Jordan Fitzgerald
# 3/27/2026
# Budget App

# This module implements a simple budget management system with a Category class to represent different budget categories and a function to create a spend chart. The Category class allows users to deposit funds, withdraw funds, check their balance, transfer funds between categories, and display the category information. The create_spend_chart function generates a text-based bar chart showing the percentage of total spending for each category. The main function demonstrates the functionality of the budget app by creating several categories, performing various transactions, and printing the results.

# The Category class represents a budget category and provides methods for managing the budget within that category.
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    # The deposit method allows users to add funds to the category by appending a dictionary with the amount and an optional description to the ledger. The get_balance method calculates the current balance by summing all the amounts in the ledger. The check_funds method checks if there are sufficient funds for a withdrawal or transfer. The withdraw method allows users to withdraw funds from the category, ensuring that there are enough funds available. The transfer method enables users to transfer funds from one category to another, updating both categories' ledgers accordingly. The __str__ method provides a string representation of the category, showing the name, ledger entries, and total balance.
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description":
        description})
    # The get_balance method calculates the current balance by summing all the amounts in the ledger. It iterates through each entry in the ledger, adding the amount to a total variable, and returns the final balance.
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
    # The check_funds method checks if there are sufficient funds for a withdrawal or transfer. It compares the requested amount with the current balance and returns True if there are enough funds, or False if there are insufficient funds.
    def check_funds(self, amount):
        return amount <= self.get_balance()
    # The withdraw method allows users to withdraw funds from the category, ensuring that there are enough funds available. If the withdrawal is successful, it appends a dictionary with the negative amount and an optional description to the ledger and returns True. If there are insufficient funds, it returns False without modifying the ledger.
    def withdraw(self, amount, description=""):
            if self.check_funds(amount):
                self.ledger.append({"amount": -amount, "description": description})
                return True
            return False
    # The transfer method enables users to transfer funds from one category to another, updating both categories' ledgers accordingly. It first checks if there are sufficient funds for the transfer. If the transfer is successful, it withdraws the amount from the current category with a description indicating the transfer and deposits the amount into the target category with a description indicating the source of the transfer. It returns True if the transfer is successful, or False if there are insufficient funds.
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    # The __str__ method provides a string representation of the category, showing the name, ledger entries, and total balance. It formats the category name centered within a line of asterisks, lists each ledger entry with its description and amount, and displays the total balance at the end.
    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"[:7]
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance()}"
        return title + items + total
# The create_spend_chart function generates a text-based bar chart showing the percentage of total spending for each category. It calculates the total amount spent across all categories and the percentage of spending for each category. It then constructs a vertical bar chart with percentage labels on the left and category names at the bottom, visually representing the spending distribution among the categories.
def create_spend_chart(categories):
    result = "Percentage spent by category\n"

    withdrawals = []
    total_spent = 0

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += -item["amount"]
        withdrawals.append(spent)
        total_spent += spent

    percentages = []
    for spent in withdrawals:
        percent = int((spent / total_spent) * 100)
        percentages.append(percent - (percent % 10))

    for i in range(100, -1, -10):
        result += f"{i:>3}|"
        for percent in percentages:
            if percent >= i:
                result += " o "
            else:
                result += "   "
        result += " \n"

    result += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = 0
    for category in categories:
        if len(category.name) > max_len:
            max_len = len(category.name)

    for i in range(max_len):
        result += "     "
        for category in categories:
            if i < len(category.name):
                result += category.name[i] + "  "
            else:
                result += "   "
        if i < max_len - 1:
            result += "\n"

    return result

def main():
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")

    food.deposit(1000, "Initial deposit")
    food.withdraw(150.25, "Groceries")
    food.withdraw(50.75, "Restaurant")

    entertainment.deposit(500, "Initial deposit")
    entertainment.withdraw(200, "Concert tickets")

    business.deposit(1000, "Initial deposit")
    business.withdraw(300, "Office supplies")

    print(food)
    print(entertainment)
    print(business)

    print(create_spend_chart([food, entertainment, business]))

if __name__ == "__main__":
    main()
