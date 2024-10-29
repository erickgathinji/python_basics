# print('*' * 10)
# integer, float, string, boolean (use capital False, True)
# is_new_patient = True

# inputs
# name = input('What is your name? ')
# favorite_color = input('What is your favorite color? ')
# print(name + " likes " + favorite_color)

# convert datatypes using int(), float(), bool()..
# birth_year = input("Birth Year: ") #all inputs are strings.
# print(type(birth_year)) #use type() to find the data type
# age = 2024 - int(birth_year) #convert the input to integer
# print(type(age))
# print(age)
# **********
# weight_lbs = input("Weight (lbs): ") #lbs=pounds
# weight_kg = float(weight_lbs) * 0.45
# print(weight_kg)

# Apostrophe / double quotes / triple single quotes eg for email/multi-lined paragraph
# Indexes - use variable[number] to specify an index specific character starting from 0
# course = "Python Programming for Beginners"
# print(course[0])
# print(course[0:3]) #doesn't return 3rd character
# print(course[:])
# name = 'Erick'
# print(name[1:-1]) #will print from 1 to -2 (eliminates -1)

# formatted strings
# first = 'John'  # you want a statement like John [Smith] is a coder
# last = 'Smith'
# message = first + ' [' + last + '] is a coder' #first way
# msg = f'{first} [{last}] is a coder' # f for formatted strings
# print(message)
# print(msg)

# String Methods --- variable.x
# .find finds the index, in gives a boolean output
# course = 'Python for Beginners'
# print(course.upper())
# print(course.lower())
# print(course.find('Z')) #find the index of the character. If -1, character not present.
# print(course.find('Beginners')) # returns index of B.
# print(course.replace('Beginners','Absolute Beginners')) #replace
# print('Python' in course) #in checks if there's a character in the data set. Returns Boolean

# Arithmetic operations +, /, // (integer)
# print(1000//3) #returns 333 (integer)
# print(100 % 3) #modulus returns the remainder of the division ie, 1
# print(10 ** 3) #power of ...
# x = 10 #add 3 to x
# # x = x + 3
# x += 3 #augmented/enhanced assignment interpreter - same as x = x+3
# # use with -=, *=
# print(x)

# Operator precedence - BODMAS

# Math Functions - at the top of .py, write import math
# x = 2.54673
# print(round(x)) #rounds to a whole number
# print(abs(-2.9)) #absolute returns a positive value
# import math  #makes maths functions available
# from math import floor
# print(math.ceil(5.1)) #rounds up a number ie, 6
# print(floor(3.8993)) #rounds down a number ie, 3

