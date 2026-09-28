#level 1 
'''print('akshitha')
#or
name = input("enter your name: ")
print(name)

a = 10
b = 20
print(a+b)
#or
c = int(input("enter c value: "))
d = int(input("enter d value: "))

print(c+d)

e = 10
if e%2 == 0: print('even')
#or
f = int(input("enter f value: "))
if f%2 == 0:
    print("even")
else:
    print("odd")

g = [1, 2, 3, 4, 5, 6, 7]
print(max(g))
#or
h = input('enter values: ')
print(max(h))

for i in range(1, 101):
    print(i)'''

#level 2
'''n = int(input("enter a number: "))

factorial= 1
for i in range(1, n+1):
    factorial = factorial*i

print(factorial)

text= input("enter a song name: ")
reversed_text = text[::-1]
for i in reversed_text:
    print(i)
#or
text = 'akshitha'
print(text[::-1])'''

'''random = input("enter something random: ")
if random in 'aeiouAEIOU':
    print('contains vowels')
else:
    print('no vowels')'''

#level 3
'''list = {1, 2, 3, 6, 7, 6, 2}

print(list)'''

#level4
'''marks = [86, 90, 70, 92, 88]
#print(marks)
count =0
above_75 = []
for mark in marks:
    print(mark)
    if (mark >= 75 and mark <= 100):
     count += 1
    if mark > 75:
        above_75.append(mark)
print(above_75)
print(count)
print(max(marks))
print("average: ", sum(marks)/len(marks))'''

#level 5
'''scores = [42, 87, 65, 91, 38, 76, 54, 29]

pass_count = 0
largest = scores[0]
lowest = scores[0]
above_75 = []
for score in scores:
    print(score)
    if score > 40:
        pass_count += 1
    if score > largest:
        largest = score
    if score < lowest:
        lowest = score
    if score >= 75:
        above_75.append(score)
print("number of students passed: ", pass_count)
print("highest score is: ", largest)
print("lowest score is: ", lowest)
print("above 75: ", above_75)
print("average: ", sum(scores)/len(scores))'''

#31-08-26
'''numbers = [12, 7, 4, 19, 7, 2, 19, 8]
largest = numbers[0]
smallest = numbers[0]
even_count = 0
odd_count = 0
for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
    if number % 2 == 0:
        even_count +=1
    if number % 2 != 0:
        odd_count +=1
    
print(largest)
print(smallest)
print(even_count)
print(odd_count)'''

digits = [15, 16, 17, 18, 19, 20]
sum = 0
largest = digits[0]
second_largest = digits[0]
for digit in digits:
    sum += digit
    if digit > largest:
        second_largest = largest
        largest = digit
    if digit > second_largest and digit < largest:
        second_largest = digit
        
print(sum)
print(largest)
print(second_largest)

