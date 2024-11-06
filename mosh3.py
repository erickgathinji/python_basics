# FOR loops - loop variables
"""
for item in 'Python':
    print(item) #outputs each character in a separate line
for item in ['Mosh', 'Joe', 'Sam','Kim']: #A list
    print(item)

# Use a range when dealing with large data set
for item in range(0,10,2): #use a third number to specify gaps
    print(item)

# exercise find the total of the price list using for loop
prices = [10, 20, 30]
total = 0 # start by defining a variable
for item in prices:
    total += item
print(total) #make sure to indent well outside

# Nested Loops - a loop inside another
for x in range(4): # other values (1,2,3) will be executed after y. Each value executes the y values
    for y in range (3):
        print(f'({x}, {y})')

# Challenge

numbers = [5, 2, 5, 2, 2]

# for x_count in numbers:
#     print('x' * x_count) #1 way - shortcut
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#lists
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary' ]
# print(names[2:4]) #Mosh & Sarah - retrieve values
# replace or modify values
names[0] = 'Jon' #note this changes the list value [0]
print(names)

Find the largest number in list
numbers = [9, 8, 7, 4, 50, 90,43,34,56,97]
# print(max(numbers)) - 1 way
maxi = numbers [0] #2nd way
for number in numbers:
    if number > maxi:
        maxi = number
print(maxi)

# 2D Lists
matrix = [
    [1, 2, 3], #row
    [4, 5, 6],
    [7, 8, 9]
]
#retrieve 2 from the list:
print(matrix [0][1])
#change value of 2 in the list:
matrix [0][1] = 20
print(matrix)

matrix = [
    [1, 2, 3], #row
    [4, 5, 6],
    [7, 8, 9]
]
# use inner loops to iterate:
for row in matrix:
    for item in row:
        print(item)

#List Methods/functions
numbers = [5, 2, 1, 7, 4]
#add values to dataset
numbers.append(20)
print (numbers)
#insert values
numbers.insert(2,11) #index is the number to the right of new number
print(numbers)
#remove values
numbers.remove(2) #specify actual value, not index
print(numbers)
#remove all values
# numbers.clear()
# print(numbers)
#remove the last item in a list:
numbers.pop()
print(numbers)
#check if a value exists/check index:
print(numbers.index(11))
print(11 in numbers)

#count occurrences of an item
no = [3, 4, 5, 3, 2, 6,3,8,3]
print(no.count(3))
#sort your list
no.sort()
no.reverse() #after sort to arrange from largest
print(no)

# copy your list - not dynamic- its like a backup of original
no = [3, 4, 5, 3, 2, 6,3,8,3]
no2 = no.copy()
print(no2)

# write a program to remove the duplicates in a list
no = [3, 4, 5, 3, 2, 6,3,5,3]
new = []
for i in no:
    if i not in new:
        new.append(i)
print(new)
"""

