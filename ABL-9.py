'''university scholarship allocation'''
name = input("Enter student name: ")
marks = int(input("Enter marks: "))
income = int(input("Enter family income: "))

if marks >= 90 and income <= 200000:
    scholarship = "100% Scholarship"
elif marks >= 80 and income <= 300000:
    scholarship = "50% Scholarship"
else:
    scholarship = "No Scholarship"

print("Student Name:", name)
print("Marks:", marks)
print("Family Income:", income)
print("Scholarship:", scholarship)