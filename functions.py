#your_name = input("enter your name: ")

def vowels(name):
    count = 0
    for char in name:
        if char.lower() in 'aeiou':
            count += 1
    return count

#print(vowels(your_name))

numbers = [12, 45, 7, 89, 32]
def highest_number(nums):
    highest_num = nums[0]
    for num in nums:
        if num > highest_num:
            highest_num = num
    return highest_num

#print(highest_number(numbers))

students = {
    "Asha": 78,
    "Riya": 42,
    "John": 31,
    "Sam": 65
}

def get_passed_students(students):
    passed_students = []
    for student in students:
        if students[student] >= 40:
            passed_students.append(student)
    return passed_students
#print(get_passed_students(students))


#sentence = input("enter a sentence: ")

def count_words(sentence):
    return len(sentence.split())
#print(count_words(sentence))

numbers = [12, 45, 7, 89, 32]

def second_highest(nums):
    highest = nums[0]
    second_high = nums[0]
    for num in nums:
        if num > highest:
            second_high = highest
            highest = num
        elif num > second_high and num != highest:
            second_high = num
    return second_high
#print(second_highest(numbers))


students = {
    "Asha": 78,
    "Riya": 42,
    "John": 31,
    "Sam": 65,
    "Maya": 91
}

def average(student):
    avg = sum(students.values())/len(students)
    return avg
print(average(students))

def highest_scorer(students):
    highest_score = 0
    highest_name = ""
    for name, score in students.items():
        if score > highest_score:
            highest_score = score
            highest_name = name
    return highest_score, highest_name
print(highest_scorer(students))

def get_passed_students(students):
    passed_students = []
    for student in students:
        if students[student] >= 40:
            passed_students.append(student)
    return passed_students
print(get_passed_students(students))

print(second_highest([5, 5, 3]))
print(second_highest([2, 1]))
print(second_highest([5, 5, 5]))