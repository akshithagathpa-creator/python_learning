#import calculator

#write a python program to access the elements such as -10, 10, 2, 3, 4, 10, 25, 0 withnew element as -20, and return all the items

'''list = [-10, 10, 2, 3, 4, 10, 25, 0]

list.append(-20)


print(list)'''

#write a python program to find the minimum element from the list without using built in methods elements: 10, 15, 25, 5, 3, 19

#list = [10, 15, 25, 5, 3, 19]

#print(list[4])
#list.sort()
#print(list)

#write a python program to find the max element from the list without usin built in method elements: 10, 20, 30, 40, 3, 2, 1, 23

'''num = [10, 20, 30, 40, 3, 2, 1, 23]

print(list[6])'''

#write a py program to find the sum of all the elements 

'''num = [10, 20, 20, 40, 50]
print(sum(num))'''

#write a py program to find total even numbers in the series 
#wite a py program to find all odd numbers in the series

'''numbers = [1, 2, 3, 4, 5,6, 7, 8 ,9]
for num in numbers:
    if num %2 ==0:
        print("even numbers: ", num)
    else:
        print("odd numbers: ", num)'''


#some arrays thing

n = int(input("enter how many elements: "))
list = list(map(int, input("enter elements: ").split()))
target = int(input("target: "))
found = 0

for i in range(0, n):
    if list[i] == target:
        print("index: ", i)
        found = 1
        break
if found == 0:
    print("-1")

