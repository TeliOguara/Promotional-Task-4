# main.py

from utils import add_student, view_students, load_students, save_students

def main():
    students = load_students()

    while True:
        print("\nStudent Report Card App:")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Save & Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            student = add_student()
            students.append(student)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            save_students(students)
            print("Data saved. Exiting.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
