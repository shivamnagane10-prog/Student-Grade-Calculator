print("Student Grade Calculator")
print("-------------------------")

name = input("Enter your name: ")

physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
maths = float(input("Enter Maths marks: "))
computer = float(input("Enter Computer Science marks: "))
english = float(input("Enter English marks: "))

total = physics + chemistry + maths + computer + english
percentage = total / 5

print("\nName:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)