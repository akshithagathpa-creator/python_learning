#Student Tracker list

subjects = ["python", "web development", "data science", "machine learning"]
skills_you_are_learning = ['programming', 'problem solving', 'critical thinking']
goals = ["become a data scientist", "get a job in tech", "build a portfolio of projects"]

subjects.append("artificial intelligence")

count = 1

print("subjects you are learning are: ")
for subject in subjects:
    print(count, '-', subject)
    count += 1

count = 1

print("skills you are learning are: ")
for skill in skills_you_are_learning:
    print(count,'-', skill)
    count += 1

count = 1

print("your goals are: ")
for goal in goals:
    print(count,'-', goal)
    count += 1
