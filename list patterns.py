#list patterns 

'''numbers = [12, 7, 4, 19, 7, 2, 19, 8]
count_seven = 0
no_duplicates = []
smallest = float("inf")
second_smallest = float("inf")
for number in numbers:
    if number == 7:
        count_seven += 1
    if number not in no_duplicates: 
        no_duplicates.append(number)
    if number < smallest:
         second_smallest = smallest
         smallest = number
    elif smallest < number < second_smallest:
        second_smallest = number
print(count_seven)
print(no_duplicates)
print(numbers[::-1])
print(smallest)
print(second_smallest)

numbers = [4, 9, 2, 9, 7, 4, 1, 8]
largest = None

for number in numbers:
    if numbers.count(number) == 1:
     if largest is None or number > largest:
        largest = number
print(largest)'''

#DSA linear search

numbers = [14, 27, 8, 31, 6, 19]

target = 31

for number in numbers:
    if number == 31:
        found = True
if found:
    print('found')
else:
    print('not found')