# Student Details Program

# Input student details
name = input("Enter Student Name: ")
dob = input("Enter Date of Birth (DD/MM/YYYY): ")
usn = input("Enter USN (Reg No): ")
department = input("Enter Department: ")

# Input marks for 5 subjects
marks = []
Sss    marks.append(mark)

# Calculate total and percentage
total = sum(marks)
percentage = total / 5

# Display student details
print("\n----- STUDENT DETAILS -----")
print("Name:", name)
print("DOB:", dob)
print("USN:", usn)
print("Department:", department)

print("\nMarks in 5 Subjects:", marks)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

# Further continuation (Grade Calculation)
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)
