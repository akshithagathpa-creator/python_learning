#Read the temperature in centigrade and convert it into fahrenheit

#C= (F-32)*5/9
#F= C*9/5+32

#temp= int(input("enter the temperature in centigrade: "))
#print(type(temp))
#F = (temp*9/5)+32
#print("the temperature in fahrenheit is:  ", F)

#temp = int(input("enter temperature in fahrenheit: "))
#print(type(temp))
#C = (temp-32)*5/9
#print("the temperature in centigrade is: ", C)

'''write a python program to read two numbers and swap those 2 without using third variable'''
#x = 10
#y = 20
#print(x,y)

#x,y = y,x
#print(x,y)

'''Read a list of number and write a program to check whether a particular element is present or not using membership operators'''

#List= [1,2,3,4,5]
#Ele = int(input("enter any number: "))
#List.append(input("enter the number: "))
#if Ele in List:
    #print("Ele is present in the list")
#else:
   # print("Ele is not present")

'''Read a name, address, email and phone number of a person through and print the details'''

#name = input("enter your name: ")
#address = str(input("enter your address:"))
#email = str(input("enter your email: "))
#phone_number = int(input("enter your phone number: "))

#print("your name is", name)
#print("your address is", address)
#print("your email is", email)
#print("your phone number is", phone_number)

'''write a python program to check wether the year is leap year or not'''

#year%4==0
#year%100!=0
#year%400==0

#year = int(input("enter year: "))

#if year%4==0 and year%100!=0 or year%400==0:
    #print("it is a leap year")
#else:
    #print("not leap year")

'''Read four number and find maximum and minimum numbers among those numbers'''

numbers = [1,2, 3, 4]
print(min(numbers))
print(max(numbers))
