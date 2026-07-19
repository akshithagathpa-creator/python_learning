#task one
a = 7
b = 13

print("addition: ", a+b)
print("subtraction: ", a-b)
print("multiplication: ", a*b)
print("division: ", a/b)
print("floor divison: ", a//b)
print("modulus: ", a%b)
print("power: ", a**b)

# task two type casting
x = 7
y = int(x)
z = float(x)

print(y + 5)
print(z + 2.5)

# task three
x = 5
x += 3
print(x)


# task three 
weight = float(input("enter your weight: "))
height = float(input("enter your height: "))

bmi = weight/ height ** 2 

print("your BMI: ", bmi)

#task four 
p = float(input("enter principal amount: "))
R = float(input("enter the rate of interest(%): "))
T = float(input("enter time(years): "))

SI = (p*R*T)/100
print("simple interest: ", SI)