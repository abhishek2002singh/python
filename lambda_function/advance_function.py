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


# print vowel and consonent 

def check_vowel(c):
    vowel =[]
    consonent = []
    if c.lower() in "aeiou":
        vowel.append(c)
        return "vowel" , vowel
    else:
        consonent.append(c)
        return "consonent" , consonent
    
words = "AbhishekSiNgh"

result2 = list(map(check_vowel , words))
print(result2)


# print vowel and consonent 

def check_vowel1(c):
   
    if c.lower() in "aeiou":
        vowel1.append(c)
        return "vowel"
    else:
        consonent1.append(c)
        return "consonent" 
    
vowel1 =[]
consonent1 = []    
words1 = "AbhishekSiNgh"

result3 = list(map(check_vowel1 , words1))
print(result3)
print(vowel1)
print(consonent1)


#  print prime number 

def prime_number( a,b):

    for i in  range(a,b+1):
       prime = True
       for j in range(2 , i):
           if i%j==0:
               prime= False
               break
       if prime == True:
            print(i)


a= int(input("enter a number"))
b= int(input("enter a number"))
prime_number(a , b)

           