print("Welcome to ATM Simulator")
print("Please insert your ATM Card")
pin = int(input("Enter your 4 digit ATM Pin"))
account_balance = 0000
if pin == 1234:
    while True:
        print("press 1 for Check balance")
        print("press 2 for Withdraw")
        print("press 3 for Deposit")
        print("press 4 for Exit")
        try:
            option = int(input("Enter your choice:"))
        except:
            print("Please choose the valid option")
        if option == 1:
            print(f'Your current balance is {account_balance}')
        if option == 2:
            withdrawal_amount = int(input('Enter the amount to Withdraw'))
            if withdrawal_amount < account_balance:
                account_balance = account_balance - withdrawal_amount
                print(f'{withdrawal_amount} is debited from your account')
                print(f'Your current balance is {account_balance}')
            else:
                print('Insufficient funds.')
        if option == 3:
            deposit_amount = int(input('Enter the amount to deposit: '))
            account_balance = account_balance + deposit_amount
            print(f'{deposit_amount} is credited to your account')
            print(f'Your current balance is {account_balance}')
        if option == 4:
            print('Thank you for using our ATM simulator.')
            break

else:
    print('You entered the wrong pin...Try Again')