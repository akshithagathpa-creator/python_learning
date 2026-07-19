num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))

print("addition:", num1 + num2)
print("multiplication:", num1 * num2)
print("subtraction:", num1 - num2)
print("division:", num1/num2)

choice = input("convert from (C/F): ")

if choice.upper() == "C":
    C = float(input("enter temperature in celsius: "))
    f = (c*9/5) + 32 
    print(c, "°C =", f, "°F")

elif choice.upper() == "F":
    f = float(input("enter temperature in farenhiet: "))
    C = (f - 32)* 9/5
    print(f,"°F= ", c, "°C")

else:
    print("Invalid choice please enter C or F.")


p = float(input("enter principal: "))
r = float(input("enter rate of interest: "))
t = float(input("enter time in years: "))

si = (p * r * t) / 100
print("simple interest: ", si)