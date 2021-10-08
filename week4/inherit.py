# parent class / super class or base class
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print('Your password has been changed to', self.password)


# child class / sub class
class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0

    def check_balance(self):
        print(self.name, 'has an account balance of:', self.balance)


bankuser1 = BankUser("Jane", "Jane@nucamp.com", "bestpassword")
