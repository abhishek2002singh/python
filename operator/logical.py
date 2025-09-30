# logical operators - logical operators are used to combine conditional statements and return boolean values

# and - returns true if both statements are true
# or - returns true if one of the statements is true
# not - reverse the result, returns false if the result is true


print(10 > 5 and 5 < 10)  # true and true = true
print(10 > 5 and 5 > 10)  # true and false =
print(10 > 5 or 5 > 10)  # true or false = true true
print(10 < 5 or 5 > 10)  # false or false =
print(not(10 > 5))  # not true = false false
print(not(10 < 5))  # not false = true
print(not(True))  # not true = false
print(not(False))  # not false = true