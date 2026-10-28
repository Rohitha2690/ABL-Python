'''Courier charge automation'''
weight = float(input())

if weight <= 1:
    charge = 50
elif weight <= 5:
    charge = 100
else:
    charge = 100 + (weight - 5) * 20

print("Courier Charge:", charge)
