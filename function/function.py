#  in python function have three type 

#   1. inbuild function
#   2. custom function
#   3. anonymous function

#  1. inbuild function - in python provide some inbuid function to perform specific task in python 
#   for ex -  max , min , len , count.......etc

student_name = ["kamal" , "lalu" , "ujjwal" , "abhishek"]

number_of_student = len(student_name)

print(student_name)
print(number_of_student)


print(student_name.count("kamal"))


#  custom function - it is manualy make a function use def keyword

def AP_rantengal( len , width):
    area = len * width
    per = 2*(len + width)

    return area , per

print(AP_rantengal(3,4))


a , p = AP_rantengal(8,9)

print("area of rentangel is : " , a)

print("parameter of rantangel is : " , p)

def order_name(name , product_name):
    print(name," order a product name is " , product_name )

order_name("kamal yadav" , "mixer")
order_name("abhishek yadav" , "laptop")


#  take a value from any person 

def take_number():
    a = input("enter a number")
    print(a)

check = take_number()

print("what will be print here" , check)
print(type(check))