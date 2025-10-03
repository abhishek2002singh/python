# def prime_number(a, b):
#     primes = []
#     for i in range(a, b + 1):
#         if i < 2:  
#             continue
#         prime = True
#         for j in range(2, i):
#             if i % j == 0:
#                 prime = False
#                 break
#         if prime == True:
#             primes.append(i)
#     return primes

# result = prime_number(a=10, b=20)
# print(result)

def primeNumber(a,b):
    for i in range(a,b+1):
        prime = True
        for j in range(2 ,i):
            if i%j==0:
                prime = False
                break
        if prime == True:
            print(i)


primeNumber(a= 10 , b=20)


def pascal(n):
    x = 0
    y = 1
    i = 0  
    while i < n:
        print(x)
        next_val = x + y
        x = y
        y = next_val
        i += 1  

pascal(10)

# make a tringle useing pascal tringle

def pascal_tringle(n):
    x,y,i=0,1,0
    while i<n:
        print(x)
        next_val = x + y
        x = y
        y = next_val
        i += 1  

pascal(10)
      