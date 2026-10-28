'''Student email identifier validation'''
email = input()
student_id = input()

if "@" in email and "." in email and student_id.isalnum():
    print("Valid Details")
else:
    print("Invalid Details")
