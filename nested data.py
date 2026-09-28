students = [
    {"name": "A", "score": 85},
    {"name": "B", "score": 92},
    {"name": "C", "score": 78},
    {"name": "D", "score": 96}
]

highest = students[0]
for student in students:
    print(student["name"], ":", student["score"])
    if student["score"] > highest["score"]:
        highest = student
    if student["score"] > 85:
        print(student["name"], ":", student["score"])
print(highest)