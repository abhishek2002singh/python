def gender(name):
    if "mr" in name:
        return {name : "Male"}
    else:
        return {name : "Female"}

print(gender("mr kamal yadav"))  

ex = ["mr kamal" , "mrs mamata" , "mr ajeet" , "mrs anjali"]

result = list(map(gender , ex))
print(result)