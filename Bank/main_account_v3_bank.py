from bank import Bank

# Create an instance of the Bank
oBank = Bank()

# Main code
# Create two test accounts
leon_account_number = oBank.create_account('Joe', 100, 'LeonPassword')
print("Joe's account number is:", leon_account_number)
marys_account_number = oBank.create_account('Mary', 12345, 'MarysPassword')
print("Mary's account number is:", marys_account_number)

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w ')
    print()
    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]  # grab the first letter
    print()

    if action == 'b':
        oBank.balance()
    elif action == 'c':
        oBank.close_account()
    elif action == 'd':
        oBank.deposit()
    elif action == 'o':
        oBank.open_account()
    elif action == 's':
        oBank.show()
    elif action == 'q':
        break
    elif action == 'w':
        oBank.withdraw()
    else:
        print('Sorry, that was not a valid action. Please try again.')

print('Done')
