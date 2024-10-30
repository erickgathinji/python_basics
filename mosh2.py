# if statements
# requirements: if it's hot, It's a hot day + Drink plenty of water
#               otherwise if it's cold, It's a cold day + Wear warm clothes
#               otherwise, It's a lovely day
# is_hot = False
# is_cold = False #either will be executed if ONLY true
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")  # If not indented, appears with or without True.
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else: #executed if both is_hot and is_cold are false
#     print(" It's a lovely day")
# print("Enjoy your day")

# #start 04:45 do exercise
# price = 1000000
# is_good_credit = True
# if is_good_credit:
#     down_payment = price * 0.1
#     print(down_payment) #or use the formatted one for print instead of including price in each:
# else:
#     down_payment = price * 0.2
#     print(down_payment) #or use the formatted one for print instead of including price in each:
# #or use the formatted one for print instead of including price in each:
# print(f"Down payment is ${down_payment}")

# Logical Operators -and / or / NOT
# scenario: if applicant has high income AND good credit - Eligible for loan
# has_high_income = False
# has_good_credit = True
# if has_high_income or has_good_credit:
#     print("Eligible for loan")

#Not inverts any boolean value given to it eg True to False
#scenario:If applicant has good credit and does not have a criminal record: Eligible for loan
# has_good_credit = True
# has_criminal_record = False
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

