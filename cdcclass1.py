#pizza = int(input("enter the number of pizzas: "))
#puffs = int(input("enter the number of puffs: "))
#cool_drinks = int(input("enter the number of cool drinks: "))

#total_amount = pizza*100+puffs*20+cool_drinks*10

'''print("number of pizzas: ", pizza)
print("number of puffs: ", puffs)
print("number of cool drinks: ", cool_drinks)

print("total cost is: ", total_amount)

print("enjoy your meal!!")'''

'''tickets = int(input("enter the number of tickets: "))
circle = input("enter the circle(K/Q): ").upper()

if circle == "K":
    price = 75

elif circle == "Q":
    price = 150

refreshments = input("do you want refreshment?(Y/N): ").upper()

grand_total = tickets*price


if refreshments =="Y":
    grand_total += price*50

else:
    print("no refreshments opted")

grand_total = tickets*price

if tickets> 20:
    print("10% discount applicabe for the purchase")
    discount = grand_total * 0.10
    final_amount = grand_total-discount

    print("your total after discount will be: ", final_amount)
else:
    print("price of the ticket is: ", price)'''

''''write a python program to print alphabets in the following fromat
input format: enter the number 3 expected output: char: C input format 2: enter the number 28 expected output char: b'''

''' = int(input("enter the number: "))

if num > 0:
    print("number is positive")
else:
    print("number is negative")'''

'''num = int(input("enter a value: "))

if num %2 == 0:
    print("number is even")

else:
    print("number is odd")'''

'''age = int(input("enter age: "))

if age >= 18:
    print("student is eligible to vote")'''


'''num = int(input("enter number: "))

if num % 5 == 0:
    print("number is divisible by 5")
else:
    print("not divisible by 5")'''

'''char = input("enter a letter: ")
if char in ['a', 'e','i', 'o', 'u']:
    print("vowel")
else:
    print("consonant")'''

#find the largest of two numbers take two numbers and print the the large one 
'''a = int(input("enter a number: ")) 
b = int(input("enter a number: "))
if a > b:
    print("a is greater than b")
else:
    print("b is greater")'''
#2
'''a = int(input("enter a three digit number: "))

if a >= 100 and a<= 999:
    print("it's three digit number")
else:
    print("it's not a three digit number")'''
#3
'''char = input("enter a character: ")

if char.isalpha():
    print("it's an alphabet")
else:
    print("not an alphabet")'''
#4
'''a = input("enter a word: ")

if a.isupper():
    print("it's uppercase")
else:
    print("it's lowercase")'''
#5
'''a = int(input("enter a number: "))

if a%3 == 0 and a%7 == 0:
    print("number is divisible by both 3 and 7")
else:
    print("number is not divisible by 3 and 7")'''
'''a = int(input("enter a number: "))
print(abs(a))'''

#6
'''grades = int(input("enter your grades: "))

if grades >=90 and grades <=100:
    print("you get an A+")
elif grades >=80 and grades<= 89:
    print("you get an A")
elif grades >=70 and grades <=79:
    print("you get a B+")
elif grades >= 60 and grades <=69:
    print("you get a B")
elif grades <60:
    print("you fail bro")
else:
    print("enter a valid score")'''
#7
'''age = int(input("enter your age: "))'''

'''if age >= 0 and age<=12:
    print("your are a child")
elif age >= 13 and age<=19 :
    print("you're a teen")
elif age >=20 and age <=59 :
    print("you're an adult")
elif age > 60:
    print("you're a senior citizen")'''
#8
'''traffic_signal = input("enter the traffic signal color: ").lower()

if traffic_signal == "red":
    print("stop")
elif traffic_signal == "yellow":
    print("wait")
elif traffic_signal == "green":
    print("go")
else:
    print("invalid signal!")'''

#9
'''day_of_the_week = int(input("enter a number from (1-7): "))

if day_of_the_week == 1:
    print("Monday")
elif day_of_the_week == 2:
    print("tuesday")
elif day_of_the_week == 3:
    print("wednesday")
elif day_of_the_week == 4:
    print("thursday")
elif day_of_the_week == 5:
    print("friday")
elif day_of_the_week == 6:
    print("satuday")
elif day_of_the_week == 7:
    print("sunday")
else:
    print("invalid day!")'''

#10
'''electricity_bill = int(input("enter the electricity bill: "))

if electricity_bill == 100:
    print("2 ruppes per unit")

elif electricity_bill > 200:
    print("5 rupees per unit")'''

#11
'''annual_income = float(input("enter your annual income: "))

if annual_income <= 250000:
    print("no tax")
elif annual_income >=250001 and annual_income <=500000:
    print("5% tax")
elif annual_income >=500001 and annual_income <= 1000000:
    print("20% tax")
elif annual_income >1000000:
    print("30% tax")'''

#12
'''height = int(input("enter your height: "))
weight = int(input("enter your weight: "))

bmi = weight/(height**2)
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi <=24.9:
    print("normal weight")
elif bmi >=25 and bmi <29.9:
    print("overweight")
else:
    print("obese")'''
#13
'''a=int(input("Enter the side a:"))
b=int(input("Enter the side b:"))
c=int(input("Enter the side c:"))

if a==b==c:
    print("Equilateral triangle")
elif a==b!=c:
    print("Isosceles triangle") 
elif a!=b!=c:
    print("Scalene triangle")  
else:
    print("Invalid triangle")'''
#14
'''a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))

print(max(a, b, c))'''

#14
from pyexpat import model


print("enter your password")
'''while Trail == 0: 
    passcode = input("enter your passcode: ")
    if passcode == "akshitha":
        print("welcome")
        break
    else:
    
        print("wrong password")'''
'''for i in range(3):
    passcode = input("enter your passcode: ")
    if passcode == 'akshitha':
        print("welcome")
        break
    else:
        print("wrong password")'''

'''age = int(input("enter your age: "))
match age:
    case 18:
        print("adult")
    case 100:
        print("old")'''

        


 