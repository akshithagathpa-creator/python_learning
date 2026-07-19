#task one 
num =  int(input("enter a number: "))

if num % 2 == 0:
    print("the number is even")

else: 
    print("the number is odd")

#task two 
num = int(input("enter a number: "))

if num < 0:
    print("it's a negative number!")
elif num > 0:
    print("it's a positive number!")
else:
    print("the number is zero")

#task three
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))

if a >= b and a >= c: 
    print("the largest number is: ", a)
elif b >= a and b >= c:
    print("the largest number is: ", b)
else:
    print("the largest number is: ", c)


#bonus task 
marks = int(input("enter your marks: "))

if marks >= 90:
    print("you get an A++")
elif marks >= 75:
    print("you get an A+")
elif marks >= 60: 
    print("you get an A")
elif marks >= 30:
    print("you get a B")
else:
    print("you lose bro")