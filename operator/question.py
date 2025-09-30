order_size = 6025
Number_of_pallets = order_size// 6

print("Number of pallets needed:", Number_of_pallets)



#convert second to hour, minute, second

total_seconds = 5000
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"{hours} hours, {minutes} minutes, {seconds} seconds")




# check predication rule in operator

print(1-2+4*6/2)   # for check precidence of operator


# check number is even or odd 

a = 10

if a % 2 == 0:
    print("even")
else:
    print("odd")


    # find percentage of math subject

math_mark = 66
total_mark = 80

percentage = math_mark/total_mark*100

print(percentage)

