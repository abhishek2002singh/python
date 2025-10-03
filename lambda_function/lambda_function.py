number = [1,2,3,4,5,6,7,8,9]
for i in range(1 , len(number)+1):
    print(i*i)
    

# calculate square of numbers
calculate_number = map(lambda x: x*x, number)

print(list(calculate_number))





