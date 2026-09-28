'''write a py program to check whether the given number is even'''
'''a = int(input("enter a number: "))
if a%2==0:
    print("the number is even")'''
'''write the same code using short hand if'''

'''a = int(input("enter a number: "))
if a%2==0:print("even")'''

'''write a py program to check whether the given num is even or odd'''
'''a = int(input("enter a number: "))
if a%2==0:
    print("the number is even")
else:
    print("odd")'''
'''write a py program to find the largest of three num using multiway selection statement'''
a= 6
b= 7
c = 8
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")

'''write a py program 5 sub marks and find total and avg and display grade of a student'''
'''scores = int(input("enter your total score: "))
if scores >= 75:
    print("distinction")
elif scores >= 65 and scores<75:
    print("first class")
elif scores >=50 and scores <60:
    print("second class")
elif scores >= 35 and scores <50:
    print("thrid class")
else:
    print("fail")'''
'''maths = int(input("enter math score: "))
english = int(input("enter english scores: "))
german = int(input("enter german: "))
total = maths + english + german
avg = total/5
if avg >= 75:
    print("distinction")
elif avg >= 65 and avg<75:
    print("first class")
elif avg >=50 and avg <60:
    print("second class")
elif avg >= 35 and avg <50:
    print("thrid class")
else:
    print("fail")'''

'''write a py program to check if the given input is digit or lowercase char or uppercase char or a special char'''
char = input("enter something: ")

if char.isdigit():
    print("it is a digit")
elif char.isupper():
    print("uppercase")
elif char.islower():
    print("lowercase")
else:
    print("special symbol")