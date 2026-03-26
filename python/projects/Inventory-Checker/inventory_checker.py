# Jordan Fitzgerald
# 3/25/2026
# Inventory Checker

# This module implements a simple inventory management system for a store. It includes functions to add items to the inventory, remove items from the inventory, check the stock of specific items, identify low stock items, and calculate the total number of items in the inventory. The module demonstrates these functionalities through a main function that performs various operations on the inventory and prints the results.
inventory = {
    'laptop': 5,
    'mouse': 12,
    'keyboard': 3,
    'monitor': 2
}
# The add_item function adds a specified quantity of an item to the inventory. If the item already exists, it updates the quantity. The remove_item function removes a specified quantity of an item from the inventory, ensuring that the item exists and that there is enough quantity to remove. The check_stock function checks if an item is in stock and returns its quantity. The low_stock function identifies items that are low in stock (quantity less than 5) and returns a list of those items. The total_items function calculates the total number of items in the inventory.
def add_item(inventory, item, quantity):
    item = item.lower()
    if item in inventory:
        inventory[item] += quantity
        return f"\nItem already exists. Updated quantity of {item} to {inventory[item]}."
    else:
        inventory[item] = quantity
    return f"\n{quantity} {item}(s) added to inventory."
# The remove_item function removes a specified quantity of an item from the inventory, ensuring that the item exists and that there is enough quantity to remove. If the item does not exist or if there is not enough quantity, it returns an appropriate message. If the quantity of the item reaches zero after removal, it deletes the item from the inventory.
def remove_item(inventory, item, quantity):
    item = item.lower()
    if item not in inventory:
        return f"\nItem '{item}' does not exist in inventory! Cannot remove item."
    if inventory[item] < quantity:
        return f"\nNot enough {item}(s) in inventory to remove! Current quantity: {inventory[item]}."
    inventory[item] -= quantity
    if inventory[item] == 0:
        del inventory[item]
        return f"\n{item} removed from inventory."
    return f"\n{quantity} {item}(s) removed from inventory. Remaining quantity: {inventory[item]}."
# The check_stock function checks if an item is in stock and returns its quantity. If the item is not found in the inventory, it returns a message indicating that the item is not available.
def check_stock(inventory, item):
    item = item.lower()
    if item in inventory:
        return f"\n{item} is in stock. Quantity: {inventory[item]}."
    else:
        return f"\n{item} is not found in inventory."
# The low_stock function identifies items that are low in stock (quantity less than 5) and returns a list of those items. If there are no low stock items, it returns a message indicating that all items are sufficiently stocked.
def low_stock(inventory):
    low_stock_items = {item: quantity for item, quantity in inventory.items() if quantity < 5}
    if low_stock_items:
        return f"\nLow stock items: {', '.join(low_stock_items.keys())}."
    else:
        return "\nNo items are low in stock."
# The total_items function calculates the total number of items in the inventory by summing the quantities of all items. It returns a message with the total count of items in the inventory.
def total_items(inventory):
    total = sum(inventory.values())
    return f"\nTotal items in inventory: {total}."
# The main function demonstrates the functionality of the inventory management system by performing various operations such as adding items, removing items, checking stock, identifying low stock items, and calculating the total number of items in the inventory. It prints the results of each operation to the console.
def main():
    print(add_item(inventory, 'Laptop', 3))
    print(add_item(inventory, 'Headphones', 10))
    print(remove_item(inventory, 'Mouse', 5))
    print(remove_item(inventory, 'Keyboard', 4))
    print(check_stock(inventory, 'Monitor'))
    print(check_stock(inventory, 'Tablet'))
    print(low_stock(inventory))
    print(total_items(inventory))

if __name__ == "__main__":
    main()
