# if statements
# store dats - list, tuple, dictionary, set
# loops

# if statements --- else
entered_value = input("Enter the score: ") #string
# print(type(entered_value))

if not entered_value.isnumeric(): #data validation
    print("Please enter a valid number.")
    exit(0) #stop program

score = int(entered_value) #convert to integer

if score >= 78:
    print("A")
elif score >= 71 and score <= 77:
    print("A-")
elif score >= 64 and score <= 70:
    print("B+")
elif score >= 57 and score <= 63:
    print("B")
elif score >= 50 and score <= 56:
    print("B-")
elif score >= 43 and score <= 49:
    print("C+")
else:
    print("C")
