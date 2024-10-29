#list []
scores = [90, 75, 56, 45, 33, 76, 60, 55, 44, 33]

# access / retrieve a value
print(scores[0])
print(scores[2])

# add a value
scores.append(61)
print(scores)

# remove a value
scores.pop(-3)
print(scores)

#sort data
scores.sort(reverse=True) #if from smallest, sort()
print(scores)