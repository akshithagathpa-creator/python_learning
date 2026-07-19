#H-E-R goal manager

goals = [input("Enter your goals: ")]

choice = input("do you want to add more goals? (yes/no):")

for i in range (3):
 if choice == "yes":
  goals.append(input("enter your goals:"))

 count = 1
 for goal in goals:
  print(count, '-', goal)
  count += 1

if len(goals) >= 3:
 print("you're building a strong foundation!")

else:
 print("keep goin', you're doin' great!")
