import json

with open('database.json', 'r') as file:
    database_local = json.load(file)

for group, students in database_local.items():
    for student, marks in students.items():
        print(f"Студент: {student}")
        for mark in marks:
            print(mark)