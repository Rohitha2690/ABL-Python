'''Nested loop calender'''
days = int(input())

print("Mon Tue Wed Thu Fri Sat Sun")

for i in range(1, days + 1):
    print(i, end=" ")
    if i % 7 == 0:
        print()
