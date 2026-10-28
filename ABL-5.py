'''Traffic violation penality calculator'''
speed = int(input())

if speed <= 60:
    fine = 0
elif speed <= 80:
    fine = 500
else:
    fine = 1000

print("Traffic Fine:", fine)