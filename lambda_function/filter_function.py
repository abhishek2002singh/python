# make prime number using filter method

def prime(n):
   for i in range(2,n):
      if n%i==0:
         return False
      
   return True

result = list(filter(prime , range(1000 ,2000)))

print(result)





# Filter words starting with 'a'
words = ["apple", "banana", "avocado", "cherry", "apricot"]
a_words = list(filter(lambda word: word.startswith('a'), words))
print(a_words) 


users = [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 17, "active": True},
    {"name": "Charlie", "age": 30, "active": False},
    {"name": "Diana", "age": 16, "active": True}
]

# Filter active users who are 18 or older

result1 = list(filter(lambda users: users["age"]>18 and users["active"] , users))

print(result1)


# print all value whose name is grater than 5

result2 = list(filter(lambda users: len(users["name"])>5 , users))
print(result2)