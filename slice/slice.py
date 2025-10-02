student_data = "abhishek yadav naugavan belsara karchhana praygraj"

print(student_data[1:-1])   # slice from index 1 to 5

# print(student_data[6 : 10 :-1])    it gave empty 

print(student_data[10 : 6 :-1])

# its print alternative if 2 element

print(student_data[::2])  

#  it is print a reverse order of string

print(student_data[::-1])


class_performance = [25,65,8,5,25,45,65,95,75,12]

print(class_performance[0:5])


# replace a number 5,25,45  with 99 56 72 

class_performance[3 : 6] = [99,56,72]

print(class_performance)