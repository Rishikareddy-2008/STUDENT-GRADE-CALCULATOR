# Student Grade Calculator

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


print("----- Student Grade Calculator -----")

# input: student name
name = input("Enter Student Name: ")

total = 0
subjects = 5

for i in range(1, subjects + 1):
    while True:
        try:
            marks = float(input(f"Enter marks for Subject {i} (0-100): "))

            if 0 <= marks <= 100:
                total += marks
                break
            else:
                print("Marks should be between 0 and 100. Please Try again.")

        except ValueError:
            print("Invalid input! Please enter numeric value.")

# Calculations
percentage = total / subjects
student_grade = calculate_grade(percentage)

# Pass/Fail Status
status = "Pass" if percentage >= 50 else "Fail"

# Display the Result
print("\n----- Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2))
print("Grade:", student_grade)
print("Status:", status)