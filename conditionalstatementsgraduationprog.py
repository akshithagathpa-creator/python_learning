#conditional statements graduation program 

mood = int(input("rate your mood on a scale of 1-10: "))
motivation = int(input("rate your motivation on a scale of 1-10: "))

if mood <= 6 and motivation <= 6:
    print("chill bro go to sleep!")
elif mood <= 6 and motivation >6:
    print("maybe you can try something productive actually")
elif mood >6 and motivation <= 6:
    print("maybe we can just do lil tasks and rest")
elif mood >6 and motivation >6:
    print("yayyy you can be very productive todayy!")