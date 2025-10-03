# here i am code with map function

# map()-- map function in pyhton is used to iterate over every element i take two element 
#  1. function 2. iterable

numbers = [1,2,3,4,5,6,7,8,9,10]

def square(x):
    return x*x

result = list(map(square , numbers))
print(result)

#  convert into string

result_string = tuple(map(str , numbers))

print(result_string)

# work on two list

numbers2 = [11,12,13,14,15,16,17,18,19,20]

result_sum = set(map(lambda x , y: x+y , numbers , numbers2))

print(result_sum)

#  solve this question using map

def add(x,y):
    return x+y

result_sum2 = set(map(add , numbers , numbers2))
print(result_sum2)


#  check what return map function 

def check_type(x):
    return type(x)

result = list(map(check_type , numbers))
print(result)