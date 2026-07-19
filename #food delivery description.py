#food delivery description 

'''def place_order(item, quantity, address):
    return f"{quantity} {item} (s), will be delivered to {address}"

#item = input("enter the item: ")
#quantity = int(input("enter the quantity: "))
#address = input("enter the address: ")

#print(place_order(item, quantity, address))
 #print('food item: '+item+ 'quantity: ' +quantity+ 'address: ' +address+)
#place_order(item ='pizza', quantity= '3', address= 'reddy enclave')

print(place_order(
    quantity= 4,
    address= "reddy encalve",
    item = "waffles"
))'''

#grade calculator 

'''def calculate_average(mark1, mark2, mark3):

    average = (mark1 + mark2 + mark3) / 3

    return average

def calculate_grade(average):

    if average >= 90:
        return "A"

    elif average >= 75:
        return "B"

    elif average >= 50:
        return "C"

    else:
        return "Fail"


def display_result():

    mark1 = int(input("Enter mark 1: "))
    mark2 = int(input("Enter mark 2: "))
    mark3 = int(input("Enter mark 3: "))

    # Calling Worker 1
    average = calculate_average(mark1, mark2, mark3)

    # Calling Worker 2
    grade = calculate_grade(average)

    # Printing final result
    print("Average:", average)
    print("Grade:", grade)



# MAIN PROGRAM

display_result()'''

#scope program 

gender = 'female'

def student_name():
    name = 'akshitha'

    print(name)

    print(gender)

student_name()
