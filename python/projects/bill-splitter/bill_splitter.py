# Jordan Fitzgerald
# 2/24/2026
# Bill Splitter
running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21
# Print the total of all of the meals
running_total = appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)
# Calculate and print the tip 
tip = running_total * 0.25
print('Tip amount:', tip)
# Add the tip to the total and print
running_total += tip
print('Total with tip:', running_total)
# Divide the total amongst the num_of_friends variable
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)
# Round up to 2 decimal places and print what each person has to pay
each_pays = round(final_bill, 2)
print("Each person pays:", each_pays)
