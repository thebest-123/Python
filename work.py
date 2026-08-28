student_name = input("Enter student name: ")
num_subjects = int(input("How many subjects? "))

grades = {}
total_gpa = 0

for i in range(num_subjects):
    subject = input(f"Enter subject #{i+1} name: ")
    score = float(input(f"Enter score for {subject}: "))
    