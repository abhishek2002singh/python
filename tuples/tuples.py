student = {
    "fname" : "abhishek",
    "lname":"yadav",
    "age" : 24,
    "mobile":9569862364,
    "education" : "graducation"
}

print(type(student))


print(student["fname"])

print(student)

print(student.keys())  # return a all keys

# return all value

print(student.values())

# return all items

print(student.items())


# remove last element key value pair

print("kakaka",student.popitem()) 

# remove any specific key and value

print(student.pop("lname"))

print(student)


# dictionary (dict) == it is a store a key value pair and key can be unique and can be any type  and value can be any type

# you can store duplicate value , you can update a value 



