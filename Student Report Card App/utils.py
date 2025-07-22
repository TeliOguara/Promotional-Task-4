# utils.py

import os
import json
from student import Student

DATA_FILE = "students.json"

def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return [Student.from_dict(item) for item in data]

def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump([s.to_dict() for s in students], f, indent=4)

def add_student():
    name = input("Enter student name: ")
    num_subjects = int(input("How many subjects? "))
    subjects_scores = {}

    for _ in range(num_subjects):
        subject = input("Subject name: ")
        score = float(input(f"Score for {subject}: "))
        subjects_scores[subject] = score

    student = Student(name, subjects_scores)
    print(f"Added {student.name} with grade {student.grade}")
    return student

def view_students(students):
    if not students:
        print("No students available.")
        return
    for s in students:
        print(f"\nName: {s.name}")
        print(f"Scores: {s.subjects_scores}")
        print(f"Average: {s.average:.2f}")
        print(f"Grade: {s.grade}")
