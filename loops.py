# loops

while True:
    print("Hello, loops")
    break  # stops the loop after running once

scores = [90, 56, 78, 80, 68, 50, 78, 67, 87, 89, 35, 65, 76, 87, 98, 99, 54, 43, 33, 22, 21, 44, 55, 66, 77, 88, 99]
# print each score one by one not print(scores)
# for each loop
for score in scores:                    #modulus (remainder) 2 confirms if divisible by 2
    if score >= 50 and score<= 70 and score % 2 == 0: #can add condition/s (and) before print
        print(score)

#now importing a fake dataset to manipulate it and check highest & lowest ranked students
#check loops example
