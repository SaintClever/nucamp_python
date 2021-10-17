'''
Workshop 4
'''


class User:
    '''
    User Class
    ----------
    Returns:
        User(name, pin, password)

    functions:
        change_name(self, name)
        change_pin(self, pin)
        change_password(self, password)
    '''

    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        '''change name'''
        if len(name) >= 2 and len(name) <= 10:  # Bonus Task 3
            self.name = name
        else:
            print('Invalid username')

    def change_pin(self, pin):
        '''change pin'''
        if len(str(pin)) == 4 and isinstance(pin, int):  # Bonus Task 3
            self.pin = pin
        else:
            print('Invalid PIN')

    def change_password(self, password):
        '''change password'''
        if len(password) >= 5:
            self.password = password  # Bonus Task 3
        else:
            print('Invalid password')

    def __repr__(self):
        '''Driver repr'''
        rep = f'User({self.name}, {self.pin}, {self.password})'
        return rep


class BankUser(User):
    '''
    BankUser subclass:
    ------------------
        Subclass of User class

    Returns:
        show_balance(self)
        withdraw(self, withdraw_amount)
        deposit(self, deposit_amount)
        transfer_money(self, transfer_amount, requestee)
        request_money(self, requestee_amount, transferor)
    '''

    def __init__(self, name, pin, password, on_hold=False):
        # def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = float(0)

        '''TODO: Toggle'''
        self.on_hold = on_hold

    def show_balance(self):
        '''show balance'''
        print(f'{self.name} has an account balance of: ${self.balance:.2f}')

    def withdraw(self, withdraw_amount):
        '''withdraw'''
        # Bonus Task 1 && 2
        try:
            if self.balance >= withdraw_amount and self.balance > 0:
                self.balance -= float(withdraw_amount)
            else:
                print('Insufficient funds, withdrawal canceled.')
        except TypeError:
            print('Invalid withdraw')

    def deposit(self, deposit_amount):
        '''deposit'''
        # Bonus Task 1 && 2
        try:
            if deposit_amount > 0 and float or deposit_amount > 0 and int:
                self.balance += float(deposit_amount)
            else:
                print('Insufficient deposit, deposit canceled.')
        except TypeError:
            print('Invalid deposit')

    def transfer_money(self, transfer_amount, requestee):
        '''transfer money'''
        print(
            f'\nYou are transferring ${transfer_amount} to {requestee.name}\
            \nAuthentication required'
        )
        transferor_pin = int(input('Enter your PIN: '))
        if transferor_pin == self.pin:
            # new balance after successful transfer
            self.balance -= transfer_amount
            requestee.balance += transfer_amount
            print(f'Transferring ${transfer_amount} to {requestee.name}')
            return True
        print('Invalid PIN. Transaction canceled.')
        return False

    def request_money(self, requestee_amount, transferor):
        '''request money'''
        print(
            f'\nYou are requesting ${requestee_amount} from {transferor.name}\
            \nUser authentication is required...'
        )
        transferor_pin = int(input(f'Enter {transferor.name}\'s PIN: '))

        if transferor_pin == transferor.pin:
            requestee_passord = input('Enter your password: ')
            if requestee_passord == self.password:
                self.balance += requestee_amount
                transferor.balance -= requestee_amount
                print(
                    f'Request authorized\
                    \n{transferor.name} sent ${requestee_amount}'
                )
                return True
            print('Invalid password. Transaction canceled.')
            return False
        print('Invalid PIN. Transaction canceled.')
        return False

    def __repr__(self):
        '''Driver repr'''
        rep = f'BankUser({self.name}, {self.pin}, {self.password}, {self.balance})'
        return rep


# # ''' Driver Code for Task 1 '''
# account_holder = User('Bob', 1234, 'password')
# print(account_holder)


# # ''' Driver Code for Task 2 '''
# account_holder.change_name('Bobby')
# account_holder.change_pin(4321)
# account_holder.change_password('newpassword')
# print(account_holder)


# # ''' Driver Code for Task 3'''
# account_holder = BankUser('Bob', 1234, 'password')
# print(account_holder)
# print()


# ''' Driver Code for Task 4'''
# account_holder = BankUser('Bob', 1234, 'password')
# account_holder.show_balance()

# # deposit()
# account_holder.deposit(1000)
# account_holder.show_balance()

# # withdraw()
# account_holder.withdraw(500)
# account_holder.show_balance()


# ''' Driver Code for Task 5'''
bob = BankUser('Bob', 1234, 'password')
alice = BankUser('Alice', 5678, 'alicepassword')

alice.deposit(5000)
alice.show_balance()
bob.show_balance()

alice.transfer_money(500, bob)
alice.show_balance()
bob.show_balance()

alice.request_money(250, bob)
alice.show_balance()
bob.show_balance()
print()
