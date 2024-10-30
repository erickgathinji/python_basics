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

# Not inverts any boolean value given to it eg True to False
# scenario:If applicant has good credit and does not have a criminal record: Eligible for loan
# has_good_credit = True
# has_criminal_record = False
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

# Comparison operators;
# scenario: if temperature > 30 = it's a hot day
#             otherwise if < 30 = it's a cold day
#             otherwise it's neither hot nor cold
# temperature = 35
# if temperature > 30: #>,<,>=,=< are boolean.. same to != (not equal to) and == (not =, which is an assignment)
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

# Exercise
# name = input("Enter your name: ")
# if len(name) < 3:
#     print("name must be at least 3 characters")
# elif len(name) > 50:
#     print("name can be a maximum of 50 characters")
# else:
#     print("name looks good")

# Project: Weight Converter
# weight = input("Weight: ")
# unit = input("(L)bs or (K)g: ")
# if unit == 'L':
#     weight_kg = float(weight) * 0.45
#     print('You are', weight_kg, 'kilos')
#
# else:
#     # converted = float(weight) * 2.20
#     weight_lb = float (weight) / 0.45
#     print('You are ', weight_lb, 'pounds')

# loops - while + condition
i = 1
# while i <= 5:
#     print(i)
#     i = i + 1 # i += 1 since i will always be 1. This will end the loop
# print("Done")
# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1 # i += 1 since i will always be 1. This will end the loop
# print("Done")

# Guessing Game (loops)
# Scenario: There is a secret guess of 9, and have only 3 chances to guess the correct number.
# secret_number = 9
# guess_count = 0
# guess_limit = 3  # not <=
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('Congrats! You guessed the secret number!')
#         break
# else:
#     print('Sorry, you guessed the wrong number!')
