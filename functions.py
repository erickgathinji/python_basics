# functions
# define area of a triangle - blue thing is the name
import math
from datetime import date
from site import USER_BASE


def calc_area_triangle(b, h):
    area = 0.5 * b * h
    print(area)


def cal_area_circle(radius):
    area = math.pi * radius ** 2  # 22/7 * radius * radius
    area = round(area, 2) # specify number of decimal places
    print("Area of circle is", area, "square cm")  # not the best cm squared

def print_todays_date():
    today = date.today()
    print(today)

def add(*args): #(arguments) - this function adds numbers dynamically
    total = 0
    for num in args: #number
        total += num
        print("Total is ",total)

def sayHi(name, age=21): #the 21 is default, but user can input age
    print("Hello ", name, "I am ", age, " years old")



#Triangle
# use a function == calling the function
# calc_area_triangle(8, 10)
# calc_area_triangle(40, 66)

# have a list with many triangles - a list with mini-lists
# triangles = [[12, 16], [8, 12], [40, 30], [68, 97], [12, 35], [35.8, 90]]
# use a loop to calculate area for each
# for triangle in triangles:  # for each triangle in triangles
# calc_area_triangle(*triangle)
# calc_area_triangle(triangle[0], triangle[1])

#Circle
# cal_area_circle(28.73653)

# #Date
# print_todays_date()

#add
# add(3,5,10,8,7,9)

#sayHi
# sayHi("Eric")
# sayHi("Eric", age=26)

