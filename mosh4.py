"""#tuples - immutable lists - cant be changed - () not []
numbers = (1, 2, 3)
# numbers[0] = 10 #an error
print(numbers[0]) #retrieve values

#unpacking - also applies to lists
coordinates = (1,2,3) #a tuple
#multiply the 3 values
# x = coordinates[0] #normal way
# y = coordinates[1]
# z = coordinates [2]
x, y, z = coordinates # same as above assignments
print(x*y*z)

#Dictionaries- {} - storage - each value eg name should be unique
customer = {
    'name': 'Erick Kim',
    'age': 30,
    'is_verified': True
}
# print(customer['name'])
#an error returns if you use a new value eg print(customer['Name' or 'Birth'])
#use get to confirm
# print(customer.get("Birth")) #returns value if present, or none if absent
# print(customer.get("Birth", "Jan 1 1999")) #assigns a default value if the value is absent

# assign new values
customer["name"] = "John Doe"
print(customer["name"])

# add new key
customer ["dob"] = "Jan 1 1990"
print(customer)

# A program that gives alphabetic output for numeric input
phone = (input("Phone:"))
digits_mapping = {
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five',
    '6':'Six',
    '7': 'Seven',
    '8':'Eight',
    '9': 'Nine',
    '0':'Zero'
}
output = ''
for char in phone:
    output += digits_mapping.get(char,'!') + ' ' #The ' ' ensures space between the output
print(output)

import emoji

#Emoji Converter - save the characters in a dictionary
message = input('>')
words = message.split (' ') #splits the input and separates it using the ' '
emojis = { #define emojis using a dictionary --- win; --- # print(emoji.emojize('😊'))
    "smile": "😄", #dont forget comma, and double quote
    "sad": "😞" #use sad / smile in terminal
}
output = "" #means string
for word in words:
    output += emojis.get(word, word) + " "
print(output)


#FUNCTIONS
# To create a greeting-- Hi There! Welcome aboard
def greet_user (): #def = define
    print('Hi there!')
    print('Welcome aboard')

print("Start") #just a test of calling
greet_user()  # called the function - note this does not need print to appear on the terminal
print("Finish")

# PARAMETERS - The placeholders defined - example name in the definition
#***Note that ARGUMENTS are the actual pieces of info supplied example John
def greet_user (name): #def = define
    print(f'Hi {name} !')
    print('Welcome aboard')

greet_user("John") #defined the name inside the bracket
# greet_user() #if name not included, an error

def greet_user (first_name, last_name):
    print(f'Hi {first_name} {last_name} !')
    print('Welcome aboard')

greet_user("John", "Smith") # just separate using  comma
greet_user("Mary", "Smith") #if you don't include 2nd argument, an error


# KEYWORD ARGUMENTS -- the above example is a positional argument
def greet_user (first_name, last_name):
    print(f'Hi {first_name} {last_name} !')
    print('Welcome aboard')
greet_user(last_name="Smith", first_name="John")

# calc_cost (50, 5, 0.1) example in such a scenario, use keyword arguments to improve readability of the code
# calc_cost (total=50, shipping=5, discount=0.1)
#when using both positional + keyword arguments, let the positional always come first
"""












