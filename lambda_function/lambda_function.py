# number = [1,2,3,4,5,6,7,8,9]
# for i in range(1 , len(number)+1):
#     print(i*i)
    

# # calculate square of numbers
# calculate_number = map(lambda x: x*x, number)

# print(list(calculate_number))


#  write code for check who is vowel and consonent

studunt_name = "kamalyadav"

vowel = list(map(lambda ch: {ch : "vowel"} if ch in "aeiou" else {ch : "consonent"}, studunt_name))

print(vowel)

# remove all vowel and print only consonent


consonants = list(filter(lambda ch: ch not in "aeiou", studunt_name))

consonant_string = ''.join(consonants)
print(consonant_string)
