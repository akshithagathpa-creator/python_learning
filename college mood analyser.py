#college mood analyser 
input_mood = int(input("Rate your mood on a scale of 1-10: "))
input_motivation = int(input("rate your motivation level on a scale of 1-10: "))

if int(input_mood) >= 8:
    print("You're doing great!")
else:
    print("Try to improve your mood.")

if int(input_motivation) >= 8:
    print("you can get your tasks done!")
else:
    print("recovery day it is then!")