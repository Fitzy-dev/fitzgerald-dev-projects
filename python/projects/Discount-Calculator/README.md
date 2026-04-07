File: Discount_Calculator

🧾 Overview

This project implements a flexible discount system using Python. It models products and applies different discount strategies based on conditions such as user tier and discount type.

The program uses object-oriented design and the Strategy Pattern to calculate the best possible price for a product.

⸻

⚙️ Features
    •    Create a Product with name and price
    •    Apply multiple discount strategies:
    •    Percentage discount
    •    Fixed amount discount
    •    Premium user discount
    •    Validate discount applicability before applying
    •    Calculate all possible discounted prices
    •    Return the best (lowest) price
    •    Supports multiple strategies dynamically

⸻

🧠 Concepts Used
    •    Object-Oriented Programming (OOP)
    •    Inheritance and Abstract Base Classes
    •    Strategy Design Pattern
    •    Method overriding
    •    Encapsulation and validation
    •    Lists and iteration
    •    Conditional logic
    •    Type hints
    •    Exception handling

⸻

🧩 Classes Breakdown

Product

Represents an item with:
    •    name
    •    price

⸻

DiscountStrategy (Abstract Class)

Defines the structure for all discount types:
    •    is_applicable(product, user_tier)
    •    apply_discount(product)

⸻

PercentageDiscount
    •    Applies a percentage-based discount
    •    Only valid if percentage ≤ 70

⸻

FixedAmountDiscount
    •    Subtracts a fixed amount from the price

⸻

PremiumUserDiscount
    •    Applies only if user tier is "premium"

⸻

DiscountEngine
    •    Takes a list of discount strategies
    •    Iterates through them
    •    Applies valid discounts
    •    Returns the lowest price
