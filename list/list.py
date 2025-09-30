# student = ["abhishek" , "singh" , 20,9569862364 , "graduate"]

# print(type(student))

# #   list can store sequence of element and can be any data type . it is a mutable means you can add delete and update

# #  it is follow zero indexing 


# # add a new make at the end 

# student.append(20)

# print(student)

# #  insert any element at any specific index

# student.insert(2 , "yadav")

# print(student)


student_marks = [4,5,6,7,8,9,6,2,3,5,6,6]

# sort the student mark

student_marks.sort()

print(student_marks)

#  sort by decending order

student_marks.sort(reverse=True)

print(student_marks)

#  calculate average 

average_sum = sum(student_marks)

list_length = len(student_marks)

average = average_sum/list_length

print(average)


