#error handling (try + except) - like data validation
x = input("Enter First Number: ") #inputs are strings
y = input ("Enter Second Number: ")
z = input ("Enter Third Number: ")

try: #before inserting try & except, first write the intended code
    x_num = int(x)
    y_num = int(y)
    z_num = int (z)
    print (x_num * y_num * z_num)
except:
    print("Enter valid numbers")