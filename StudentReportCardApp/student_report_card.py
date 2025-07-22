import json
import os

DATA_FILE = "students.json"

def load_students():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_students(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    name = input("Enter student name: ").strip()
    subjects = {}
    while True:
        subject = input("Enter subject (or 'done' to finish): ").strip()
        if subject.lower() == "done":
            break
        score = input(f"Enter score for {subject}: ").strip()
        subjects[subject] = score

    data = load_students()
    data[name] = subjects
    save_students(data)
    print(f"\n Record saved for {name}\n")

def view_students():
    data = load_students()
    if not data:
        print("\nNo student records found.\n")
        return
    for name, subjects in data.items():
        print(f"\n{name}'s Scores:")
        for subject, score in subjects.items():
            print(f" - {subject}: {score}")
    print()

def main():
    while True:
        print("1. Add Student Record")
        print("2. View All Records")
        print("3. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
