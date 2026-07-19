#task1 
num = int(input("enter a number: "))
if num % 2 == 0:
    print("even number")
else:
    print("odd number")

#task2
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))

if a > b and a > c:
    print("a is the greatest")
elif b > c: 
    print("b is the greatest")
else:
    print("c is the greatest")

#task3
grades = int(input("enter the grades: "))

if grades >= 90:
    print("your grade is A+")
elif grades > 79: 
    print("your grade is A ")
elif grades > 69:
    print("your grade is B")
elif grades > 59: 
    print("your grade is C")
else:
    print("you get an F")