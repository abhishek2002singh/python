# #   write a function to find his factorial

# def factorial(n):
#     if n>=0:
#         _fact =1
#         for i in range(1 , n+1):
#             _fact*=i
#         return _fact
#     else:
#         print("negative number is not valid so we can not find factorial")

# a = int(input("input a number"))

# print(factorial(a))


# #  same code write in recursion

# def factorial(n):
   
#     if n == 0 or n == 1:
#         return 1
   
#     return n * factorial(n - 1)



# print(factorial(5))  


# calculate permutation and combinatin 

# permutation

def permutation(n):
    if n==0 or n==1:
        return 1
    return n*permutation(n-1)

n  = int(input("input a valtu of n"))
r= int(input("input a value of r"))

a=permutation(n)
b=permutation(n-r)
c=permutation(r)

print(a/(c*b))


# combination 

print("combination is " , a/c)
