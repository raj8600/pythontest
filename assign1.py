
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_marksheet(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:")
        for subject, marks in self.marks.items():
            print(f"\t{subject}: {marks}")

students = []
num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    name = input("Enter the name of student: ")
    roll_number = input("Enter the roll number: ")

    marks = {}
    while True:
     try:
        num_subjects = int(input("Enter the number of subjects: "))
        break
     except ValueError:
        print("Invalid input. Please enter a valid integer.")

    for j in range(num_subjects):
        subject = input(f"Enter the name of subject {j+1}: ")
        subject_marks = float(input(f"Enter the marks obtained in {subject}: "))
        marks[subject] = subject_marks

    student = Student(name, roll_number, marks)
    students.append(student)

print("\n\n*********MARK SHEET*********\n\n")
for student in students:
    student.display_marksheet()
    print("\n\n")
