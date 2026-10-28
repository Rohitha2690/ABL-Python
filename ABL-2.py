'''Atm translation sequence simulation'''
balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= 0:
    print("Invalid Withdrawal Amount")
elif withdraw > balance:
    print("Insufficient Balance")
else:
    balance = balance - withdraw
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)