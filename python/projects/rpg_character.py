# Jordan Fitzgerald
# 3/2/2026
# RPG Character
full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # Pre-Conditions for Name parameter
    if not isinstance(name, str):
        return 'The character name should be a string'

    if name == '':
        return 'The character should have a name'

    if len(name) > 10:
        return 'The character name is too long'

    if ' ' in name:
        return 'The character name should not contain spaces'

    # Pre-Conditions for Stats 
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    
    if (strength + intelligence + charisma) != 7:
        return 'The character should start with 7 points'
    # Filling out the stats based on full_dot and empty_dot
    str_line = f"STR {full_dot * strength}{empty_dot * (10 - strength)}"
    int_line = f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}"
    cha_line = f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
    # Returning the final results 
    return f"{name}\n{str_line}\n{int_line}\n{cha_line}"

# Display Characters 
print(create_character('Ren', 4, 2, 1))
print(create_character('Nick', 2, 3, 2))
print(create_character('Josh', 1, 2, 4))
print(create_character('Stephen', 4, 1, 2))




