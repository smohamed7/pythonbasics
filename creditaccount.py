#a system that can calculate your account balance

balance = 500
spend = int(input("enter amount:"))


if spend>balance:
    print("amount you want to spend")
elif spend >0 and spend <=50:
    print("purchaase successful")
acc_balance=balance-spend
print("your balance is",acc_balance)









