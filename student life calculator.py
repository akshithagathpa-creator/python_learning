#student life calculator 
number_of_classes = int(input("Enter the number of classes you have: "))
hours_studied = float(input("enter the number of hours you study per week: "))
screen_time = float(input("enter the amount of time you spent on phone:"))

print(f"classes you've attended: {number_of_classes}")
print(f"hours you study per week: {hours_studied}")
print(f"time you spent on phone: {screen_time}")

if hours_studied < screen_time:
    print("lol bro you're screen time is more than you study time lock in twin!")
else:
    print("you've locked in twin!")