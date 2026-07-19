num1 = int(input("enter number 1: "))
num2 = int(input('enter number 2: '))

print("addition: ", num1 + num2)
print("subtraction: ", num1 - num2)
print("multiplication: ", num1*num2)
print("division: ", num1/num2)

num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))

if num1 > num2:
    print("you win!!")
elif num1 < num2: 
    print("you lose:(")
elif num1 == num2:
    print("it's a tie!")
else: 
    print("enter the right values")

again == input("do you wanna play again?(yes/no): ").lower() # type: ignore
if again == "no":
    print("thanks for playing")
