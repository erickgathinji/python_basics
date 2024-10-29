#Dictionary {} ---- [] in retrieve
student = {"name": "Jane Kim", "id": 1234, "age":21, "gender": "F"}
print(student["name"])
print(student["id"])

student["weight"] = 61 #add item/value to the dictionary
print(student)

#set - removes duplicates - only one existence per item, unordered, mutable
people = {"Jane", "Bill", "Ken", "Jane"}
print(people)
people.add ("Willy")
print(people)
people.discard("Bill")
print(people)
print(len(people))
