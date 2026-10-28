'''multiple stage calculation'''
n=int(input())
for i in range(1, n + 1):
    attendance = int(input())
    marks = int(input())

    if attendance >= 75:
        if marks >= 40:
            print("Eligible for Examination")
        else:
            print("Failed in Internal Marks")
    else:
        print("Insufficient Attendance")