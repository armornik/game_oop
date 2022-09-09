from AccountOOP import Account

oAccount = Account('Joe Schmoe', 1000, 'magic')
newBalance = oAccount.deposit(500, 'magic')
oAccount.withdraw(250, 'magic')
currentBalance = oAccount.get_balance('magic')

oJoesAccount = Account('Joe', 100, 'JoesPassword')
print("Created an account for Joe")

oMarysAccount = Account('Mary', 12345, 'MarysPassword')
print("Created an account for Mary")

oJoesAccount.show()
oMarysAccount.show()
print()

# Call some methods on the different accounts
print('Calling methods of the two accounts ...')
oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')

# Show the accounts
oJoesAccount.show()
oMarysAccount.show()

# Create another account with information from the user
print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oNewAccount = Account(userName, userBalance, userPassword)
# Show the newly created user account
oNewAccount.show()
# Let's deposit 100 into the new account
oNewAccount.deposit(100, userPassword)
usersBalance = oNewAccount.get_balance(userPassword)
print()
print("After depositing 100, the user's balance is:", usersBalance)
# Show the new account
oNewAccount.show()

# Start off with an empty list of accounts
accountsList = []
# Create two accounts
oAccount = Account('Joe', 100, 'JoesPassword')
accountsList.append(oAccount)
print("Joe's account number is 0")
oAccount = Account('Mary', 12345, 'MarysPassword')
accountsList.append(oAccount)
print("Mary's account number is 1")
accountsList[0].show()
accountsList[1].show()
print()
# Call some methods on the different accounts
print('Calling methods of the two accounts ...')
accountsList[0].deposit(50, 'JoesPassword')
accountsList[1].withdraw(345, 'MarysPassword')
accountsList[1].deposit(100, 'MarysPassword')
# Show the accounts
accountsList[0].show()
accountsList[1].show()
# Create another account with information from the user
print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)  # append to list of accounts
# Show the newly created user account
print('Created new account, account number is 2')
accountsList[2].show()
# Let's deposit 100 into the new account
accountsList[2].deposit(100, userPassword)
usersBalance = accountsList[2].get_balance(userPassword)
print()
print("After depositing 100, the user's balance is:", usersBalance)
# Show the new account
accountsList[2].show()


accountsDict = {}
nextAccountNumber = 0
# Create two accounts:
oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = oAccount
print('Account number for Joe is:', joesAccountNumber)
nextAccountNumber = nextAccountNumber + 1
oAccount = Account('Mary', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = oAccount
print('Account number for Mary is:', marysAccountNumber)
nextAccountNumber = nextAccountNumber + 1
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
print()
# Call some methods on the different accounts
print('Calling methods of the two accounts ...')
accountsDict[joesAccountNumber].deposit(50, 'JoesPassword')
accountsDict[marysAccountNumber].withdraw(345, 'MarysPassword')
accountsDict[marysAccountNumber].deposit(100, 'MarysPassword')
# Show the accounts
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
# Create another account with information from the user
print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = oAccount
print('Account number for new account is:', newAccountNumber)
nextAccountNumber = nextAccountNumber + 1
# Show the newly created user account
accountsDict[newAccountNumber].show()
# Let's deposit 100 into the new account
accountsDict[newAccountNumber].deposit(100, userPassword)
usersBalance = accountsDict[newAccountNumber].get_balance(userPassword)
print()
print("After depositing 100, the user's balance is:", usersBalance)
# Show the new account
accountsDict[newAccountNumber].show()
