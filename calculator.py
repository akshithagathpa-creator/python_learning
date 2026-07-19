num1 = float(input(" enter the first number: "))
num2 = float(input("enter the second number: "))

op = input("enter operations(+, -, *, /, %,//, **): ")

def calculator(num1, num2, op):
        if op == '+':
         return num1 + num2
        elif op == '-':
         return num1 - num2
        elif op == '*':
         return num1 * num2
        elif op == '/':
         return num1 / num2
        elif op == '%':
         return num1 % num2
        elif op == '//':
         return num1 // num2
        elif op == '**':
         return num1 ** num2
        else:
         return "enter the correct shit duh"
print(calculator(num1, num2,op))
#import (file name)