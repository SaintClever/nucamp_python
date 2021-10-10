class User:
    '''User'''

    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        ''' change name '''
        self.name = name

    def change_pin(self, pin):
        ''' change pin '''
        self.pin = pin

    def change_password(self, password):
        ''' change password '''
        self.password = password

    def __repr__(self):
        '''Driver repr'''
        rep = f'User({self.name}, {self.pin}, {self.password})'
        return rep


class BankUser(User):
    '''BankUser'''

    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = float(0)

    def show_balance(self):
        ''' show balance '''
        print(f'{self.name} has an account balance of: {self.balance}')

    def withdraw(self, withdraw_amount):
        ''' withdraw '''
        self.balance -= float(withdraw_amount)

    def deposit(self, deposit_amount):
        ''' deposit '''
        self.balance += float(deposit_amount)

    def transfer_money(self, transfer_amount, requestee):
        ''' transfer money '''
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
        return False

    def request_money(self, requestee_amount, transferor):
        ''' request money '''
        print(
            f'\nYou are requesting ${requestee_amount} from {transferor.name}\
            \nUser authentication is required...'
        )
        transferor_pin = int(input(f'Enter {transferor.name}\'s PIN: '))
        requestee_passord = input('Enter your password: ')

        if transferor_pin == transferor.pin and requestee_passord == self.password:
            self.balance += requestee_amount
            transferor.balance -= requestee_amount
            print(
                f'Request authorized\
                \n{transferor.name} sent ${requestee_amount}'
            )
            return True
        return False

    def __repr__(self):
        '''Driver repr'''
        rep = f'BankUser({self.name}, {self.pin}, {self.password}, {self.balance})'
        return rep


# ''' Driver Code for Task 1 '''
# account_holder = User('Bob', 1234, 'password')
# print(account_holder)


# ''' Driver Code for Task 2 '''
# account_holder.change_name('Bobby')
# account_holder.change_pin(4321)
# account_holder.change_password('newpassword')
# print(account_holder)


# ''' Driver Code for Task 3'''
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


''' Driver Code for Task 5'''
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
