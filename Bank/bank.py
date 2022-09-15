from AccountOOP import Account, AbortTransaction


class Bank:
    def __init__(self, hours, address, phone):
        self.accounts_dict = {}
        self.next_account_number = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def ask_for_valid_account_number(self):
        account_number = input('What is your account number? ')
        try:
            account_number = int(account_number)
        except ValueError:
            raise AbortTransaction('The account number must be an integer')
        if account_number not in self.accounts_dict:
            raise AbortTransaction('There is no account ' + str(account_number))
        return account_number

    def get_users_account(self):
        account_number = self.ask_for_valid_account_number()
        o_account = self.accounts_dict[account_number]
        # self.ask_for_valid_password(o_account)
        self.ask_for_valid_password(o_account)
        return o_account

    def ask_for_valid_password(self, o_account):
        password = input('Please enter your password: ')
        o_account.checkPasswordMatch(password)

    def create_account(self, the_name, the_starting_amount, the_password):
        o_account = Account(the_name, the_starting_amount, the_password)
        new_account_number = self.next_account_number
        self.accounts_dict[new_account_number] = o_account

        # Increment to prepare for next account to be created
        self.next_account_number = self.next_account_number + 1
        return new_account_number

    def open_account(self):
        print('*** Open Account ***')
        user_name = input('What is the name for the new user account? ')
        user_starting_amount = input('What is the starting balance for this account? ')
        user_starting_amount = int(user_starting_amount)
        user_password = input('What is the password you want to use for this account? ')
        user_account_number = self.create_account(user_name, user_starting_amount, user_password)
        print('Your new account number is:', user_account_number)
        print()

    def close_account(self):
        print('*** Close Account ***')
        user_account_number = input('What is your account number? ')
        user_account_number = int(user_account_number)
        user_password = input('What is your password? ')
        o_account = self.accounts_dict[user_account_number]
        the_balance = o_account.get_balance(user_password)

        if the_balance is not None:
            print('You had', the_balance, 'in your account, which is being returned to you.')

            # Remove user's account from the dictionary of accounts
            del self.accounts_dict[user_account_number]
            print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        user_account_number = input('Please enter your account number: ')
        user_account_number = int(user_account_number)
        user_account_password = input('Please enter the password: ')
        o_account = self.accounts_dict[user_account_number]
        the_balance = o_account.get_balance(user_account_password)
        if the_balance is not None:
            print('Your balance is:', the_balance)

    def deposit(self):
        print('*** Deposit ***')
        o_account = self.get_users_account()
        deposit_amount = input('Please enter amount to deposit: ')
        the_balance = o_account.deposit(deposit_amount)
        print('Deposited:', deposit_amount)
        print('Your new balance is:', the_balance)

    def show(self):
        print('*** Show ***')
        print('(This would typically require an admin password)')
        for user_account_number in self.accounts_dict:
            o_account = self.accounts_dict[user_account_number]
            print('Account:', user_account_number)
            o_account.show()
            print()

    def withdraw(self):
        print('*** Withdraw ***')
        o_account = self.get_users_account()
        user_amount = input('Please enter the amount to withdraw: ')
        the_balance = o_account.withdraw(user_amount)
        print('Withdrew:', user_amount)
        print('Your new balance is:', the_balance)

    def get_info(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print('We currently have', len(self.accounts_dict), 'account(s) open.')
