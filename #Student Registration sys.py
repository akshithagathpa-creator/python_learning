#Student Registration sys


'''print("\n---student registration---")
registrants = set()#empty set 


while True:
    registrations = input("enter your names to register(or enter done when over): ").lower()
    if registrations == 'done':
        print("you're successfully registered!")
        break
    registrants.add(registrations)

print("\n-----registors list below!-----")
count = 1
for registrations in registrants:
    print(count, '-', registrations)
    count += 1'''
#bus pass application
'''print("\n----bus pass application----")

students = {}
while True: 
    roll_number = input("enter your roll number(or enter 'done' when over): ").lower()
    if roll_number == 'done':
        print("your application is done!")
        break

    name = input("enter your name: ")
    bus_route = input("enter your route number: ")

    students[roll_number] = {
        'name': name,
        'route': bus_route
    }
print("\n---- Here's your application----")
count = 1
for roll_number in students:
    print(f"\n ROll number: {roll_number}")
    print(f"Name : ",name)
    print(f"Bus route: ", bus_route)
    count +=1 '''

#app user profile

print("\n----create your application here!----")

Users = {}
while True:
    name = input("enter your name(or enter 'done' when over): ").lower()
    if name == 'done':
        print("your application is done!")
        break
    branch = input("enter your branch: ")
    gpa = float(input("enter your gpa: "))
    dream = input("enter your dream: ")
    Users[name] = {
        'branch': branch,
        'gpa': gpa, 
        'dream': dream
    }

print("\n----welcome" , name, "!your application is here!----")
count = 1
for name in Users:
    print(f"\n Name: {name}")
    print(f" branch: ", branch)
    print(f" gpa: ", gpa)
    print(f"dream: ", dream)