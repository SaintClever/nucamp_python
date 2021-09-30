# Task 4: The banking package
# Bonus Tasks Infinite: {:.2f}'.format() to format float with two decimal places
def show_balance(balance):
    print(f'Current Balance: ${"{:.2f}".format(balance)}')


def deposit(balance):
    try:  # Bonus Tasks Infinite: try / except user invalid input and print ValueError
        amount = float(input('Enter amount to deposit: '))
        return balance + amount
    except ValueError:
        print('Please provide a valid number')
        return balance


# Bonus Tasks Infinite: Create overdraft fee
def overdraft(balance, amount):
    overdraft_fee = 35
    overdraft_approval = input(
        f'\n\n\t\t=== Overdraft Fee Notice ===\t\t\n\
          \nA ${overdraft_fee} overdraft will apply.\
          \nContinue withdrawal y/n: '
    ).lower()

    if overdraft_approval == 'y':
        return (balance - overdraft_fee) - amount
    else:
        print('Transaction cancelled')
        return balance


def withdraw(balance):
    # Bonus Task Infinite: Account minimum
    account_minimum = 1000

    try:  # Bonus Tasks Infinite: try / except user invalid input and print ValueError
        amount = float(input('Enter amount to withdraw: '))

        # Bonus Task Infinite: subtract withdraw amount from balance if balance is greater than or equal to amount, however if balance minus the amount is less than the account minimun invoke overdraft
        if balance >= amount:
            if balance - amount < account_minimum:
                return overdraft(balance, amount)
            return balance - amount

        # Cancel transaction: if the amount subtracted from the balance is below or equal to 0
        elif balance - amount <= 0:
            print('Where are you going to get that kind of money? Transaction denied.')
            return balance

        # # Appy overdraft fee: if the amount subtracted from the balance is less than the account minimum
        # elif balance - amount < account_minimum:
        #     return overdraft(balance, amount)

    except ValueError:
        print('Please provide a valid number')
        return balance


def logout(name):
    print(f'Goodbye {name}!\n')
