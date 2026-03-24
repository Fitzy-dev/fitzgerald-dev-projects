# Jordan Fitzgerald
# 3/24/2026
# User Configuration Manager
# This module provides functions to manage user settings, including adding, updating, deleting, and viewing settings.


def add_setting(settings, setting): # Add a new setting to the settings dictionary
    # Convert the key and value to lowercase to ensure consistency
    key = setting[0].lower()
    value = setting[1].lower()
    # Check if the key already exists in the settings dictionary to prevent overwriting existing settings
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    # Add the new setting to the settings dictionary
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, setting): # Update an existing setting in the settings dictionary
    key = setting[0].lower()
    value = setting[1].lower()
    # Check if the key exists in the settings dictionary before attempting to update it
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    # If the key does not exist, return an error message
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):# Delete a setting from the settings dictionary
    # Convert the key to lowercase to ensure consistency when checking for its existence in the settings dictionary
    key = key.lower()
    # Check if the key exists in the settings dictionary before attempting to delete it
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    # If the key does not exist, return an error message
    return "Setting not found!"
# View all current settings in the settings dictionary
def view_settings(settings):
    # Check if there are any settings available in the settings dictionary before attempting to display them
    if not settings:
        return "No settings available."
    # Create a string to display all current settings in a readable format
    result = "Current User Settings:\n"
    # Iterate through the settings dictionary and append each key-value pair to the result string, capitalizing the key for better readability
    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"
    
    return result
# Example usage of the user configuration manager functions
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}
# Test adding a new setting
print(add_setting(test_settings, ("Language", "English")))
# Test adding a setting that already exists
print(test_settings)
# Test updating and deleting an existing setting
print(update_setting(test_settings, ("Theme", "Light")))
print(delete_setting(test_settings, "volume"))
# Test updating a non-existing setting
print(view_settings(test_settings))



    

     
