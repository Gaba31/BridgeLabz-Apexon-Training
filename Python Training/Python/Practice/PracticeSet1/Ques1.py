# 1️. ATM Transaction Validator
# Problem Statement
# An ATM processes N withdrawal requests sequentially.
#  Each request has an amount. Rules:
# Withdrawal amount must be a multiple of 100
#
#
# Account balance must never go negative
#
#
# For each transaction, print SUCCESS or FAILED

account_balance = int(input("Enter your current balance: "))
no_of_withdrawal = int(input("Enter the number of withdrawals: "))

while no_of_withdrawal > 0:
    withdrawal_amount = int(input("Enter amount you want to withdraw: "))

    if withdrawal_amount % 100 != 0:
        print("FAILED")
    elif withdrawal_amount > account_balance:
        print("FAILED")
    else:
        account_balance -= withdrawal_amount
        print("SUCCESS")

    no_of_withdrawal -= 1

print(f"Final Balance : {account_balance}")