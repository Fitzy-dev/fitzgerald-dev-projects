# Jordan Fitzgerald
# 3/18/26
# Number Pattern Generator
def number_pattern(n):
    nums = []
    # Test Case to see if n is an Integer
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    # Test Case to see if n is greater than 1
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    # For Loop to add numbers to the nums
    for i in range(1, n + 1):
        nums.append(str(i))

    return ' '.join(nums)
# Printing To the Console
print(number_pattern(0))
print(number_pattern(7))
print(number_pattern(14))
