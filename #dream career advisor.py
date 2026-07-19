#dream career advisor 
#name = input("enter your name: ")
#age = int(input("enter your age: "))
#current_GPA = float(input("enter your current GPA: "))

#if current_GPA >= 8.5:
    #print(f"{name}, you have a great gpa! keep goin'")
#elif current_GPA >= 7.0:
    #print(f"{name}, your gpa is good but could be better.")
#else:
    #print(f"{name}, bro you're losin' aura points with that gpa level up girl!")

#College attendance checker 
#Total_classes = int(input("enter the total number of classes: "))
#Attended_classes = int(input("enter the number of classes you attended: "))

#percentage_attendance = (Attended_classes/Total_classes)*100
#print("your attendance percent is:", percentage_attendance,"%")

#if percentage_attendance >= 75:
    #print("you have a good attendance record!")

#elif percentage_attendance >= 50:
    #print("yes bruhh you almost there sit for few more classes and you'll be good to go!")

#else:
    #print("you're cooked bro, you better attend or you're gone!")

#startup idea validator 
#problem_name = input("enter your problem name: ")
#number_of_people = int(input("enter the number of people facing this problem: "))
#choice = input("are these people willing to pay for a solution? (yes/no): ")

#if choice.lower() == "yes":
    #number_of_people_willing_to_pay = int(input("enter the number of people willing to pay for a solution: "))
#if choice.lower() == "no":
    #number_of_people_willing_to_pay = 0
    #print("you need a better problem to solve")

#if number_of_people_willing_to_pay > 100:
    #print("yeahh shawttyy you got this just go for it and make that money!")
#elif number_of_people_willing_to_pay > 50:
    #print("hmm that's good but gotta improve your marketing strategy to reach more people")
#else:
    #print("go home shawtyy think of a better solution or better problem to solve ")

#AI study planner
#hours_available_today = float(input("enter how many hours available today: "))

#if hours_available_today == 1:
    #print("yes keep wastin you're like that!")
#elif hours_available_today == 2:
    #print("you can plan what to do and clean your room")
#elif hours_available_today >= 3:
    #print("you can do all the tasks you planned")
#else:
    #print("you're so unc bro wth are ya doin! ")

#Mood recovery program 
Mood = float(input("Rate your mood on a scale of 1-10: "))
Motivation = float(input("Rate your motivation level on a scale of 1-10: "))

if Mood <= 5 and Motivation <= 5:
    print("nah bro don't even try listen to music and sleep")
elif Mood <= 10 and Motivation <= 10:
    print("yeahh you can try doin something productive")
