'''Campus transport allocation'''
name = input("Enter student name: ")
distance = float(input("Enter distance from campus in km: "))

if distance > 20:
    bus = "Long-Distance Bus"
elif distance > 10:
    bus = "Medium-Distance Bus"
else:
    bus = "Short-Distance Bus"

print("Student Name:", name)
print("Distance:", distance, "km")
print("Allocated Transport:", bus)