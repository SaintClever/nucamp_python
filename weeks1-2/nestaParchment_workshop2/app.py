from banking_pkg import account


def atm_menu(name):
    # print('          === Automated Teller Machine ===          ')
    # print('User: ' + name)
    # print('------------------------------------------')
    # print('| 1.    Balance     | 2.    Deposit      |')
    # print('------------------------------------------')
    # print('------------------------------------------')
    # print('| 3.    Withdraw    | 4.    Logout       |')
    # print('------------------------------------------')

    # Bonus Tasks Infinite: Utitlize \t and *
    print('\n\t\t=== Automated Teller Machine ===\t\t\n')
    print('User: ' + name)
    print(42 * '-')
    print('| 1.    Balance     | 2.    Deposit      |')
    print(42 * '-')
    print(42 * '-')
    print('| 3.    Withdraw    | 4.    Logout       |')
    print(42 * '-')


# Task 2: Registration
while True:
    print('\n\t\t=== Automated Teller Machine ===\t\t\n')
    name = input('Enter name to register: ')

    # Bonus Task 1
    if len(name) > 1 and len(name) < 11 and any(map(str.isdigit, name)) != True:
        break
    elif len(name) <= 1:
        print('You must enter a name.')
    elif len(name) >= 11:
        print('The maximum name length is 10 characters.')
    # Bonus Tasks Infinite: Check if any of the characters are digits within name
    elif any(map(str.isdigit, name)):
        print('Please use only letters.')


while True:
    # Bonus Task 2
    pin = input('Enter PIN: ')
    if len(pin) == 4 and any(map(str.isalpha, pin)) != True:
        balance = 0
        print(f'{name} has been registered with a starting balance of ${balance}')
        break
    # Bonus Tasks Infinite: Make pin length more descriptive
    elif len(pin) < 4 or len(pin) > 4:
        print('PIN must contain 4 numbers\n')
    # Bonus Tasks Infinite: Check if any of the charaacters are letters within pin
    elif any(map(str.isalpha, pin)):
        print('Please use only numbers.\n')


# Task 3: Log in and prompt for menu option
while True:
    print('\n\t\t=== Automated Teller Machine ===\t\t\n')
    print('\nLOGIN')
    name_to_validate = input('Enter name: ')
    pin_to_validate = input('Enter PIN: ')

    if name_to_validate == name and pin_to_validate == pin:
        print('Login successful!')
        break
    print('Invalid credentials!')


while True:
    atm_menu(name)
    option = input('\nChoose an option: ')

    if option == '1':
        account.show_balance(balance)
    elif option == '2':
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == '3':
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == '4':
        account.logout(name)
        break
    else:
        # Bonus Tasks Infinite: Option for user invalid inputs
        print('That option doesn\'t exist')
