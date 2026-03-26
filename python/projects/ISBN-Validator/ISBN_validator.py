# Jordan Fitzgerald
# 3/25/2026
# ISBN Validator
# This program validates ISBN-10 and ISBN-13 codes. The user is prompted to enter an ISBN code and its length (10 or 13). The program checks the validity of the ISBN code based on its length and the check digit calculation.

# The validate_isbn function checks if the provided ISBN code has the correct length and valid characters. It then calculates the expected check digit using the appropriate algorithm for ISBN-10 or ISBN-13 and compares it with the given check digit to determine if the ISBN code is valid or not.
def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    main_digits = isbn[:length - 1]
    given_check_digit = isbn[length - 1]

    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print('Invalid character was found.')
        return

    if length == 10:
        if not (given_check_digit.isdigit() or given_check_digit == 'X'):
            print('Invalid character was found.')
            return
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        if not given_check_digit.isdigit():
            print('Invalid character was found.')
            return
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

# The following functions calculate the check digit for ISBN-10 and ISBN-13 codes based on the main digits provided by the user. The check digit is calculated using specific algorithms for each ISBN type, and the result is returned as a string.
def calculate_check_digit_10(main_digits_list):
    digits_sum = 0

    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)

# The calculate_check_digit_13 function computes the check digit for an ISBN-13 code by summing the main digits with specific weights (1 for even indices and 3 for odd indices) and then applying a modulo operation to determine the final check digit.
def calculate_check_digit_13(main_digits_list):
    digits_sum = 0

    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit
        else:
            digits_sum += digit * 3

    result = (10 - digits_sum % 10) % 10
    return str(result)

# The main function prompts the user for input, processes the input to extract the ISBN code and its length, and then calls the validate_isbn function to check the validity of the provided ISBN code. It also includes error handling for invalid input formats and values.
def main():
    user_input = input('Enter ISBN and length: ')
    values = user_input.split(',')

    if len(values) != 2:
        print('Enter comma-separated values.')
        return

    isbn = values[0]

    try:
        length = int(values[1])
    except ValueError:
        print('Length must be a number.')
        return

    if length not in (10, 13):
        print('Length should be 10 or 13.')
        return

    validate_isbn(isbn, length)


# main()
