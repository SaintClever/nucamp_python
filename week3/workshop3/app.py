from donations_pkg import homepage, user


database = {'admin': 'password123'}
donations = []
authorized_user = ''


while True:
    # inovke show_homepage imported from homepage
    homepage.show_homepage()

    # check user authorization
    if authorized_user == '':
        print('You must be logged in to donate.')
    elif authorized_user != '':
        print(f'Logged in as: {authorized_user}')

    # check user option
    user_option = input('Please choose and option: ')
    if user_option == '1':
        username = input('\nusername: ')
        password = input('password: ')
        authorized_user = user.login(database, username, password)

    elif user_option == '2':
        username = input('\nusername: ')
        password = input('password: ')
        authorized_user = user.register(database, username)

        if authorized_user != ' ':  # MUST not be an EMPTY string TODO: add authorized_user != 0
            database[username] = password

    elif user_option == '3':
        if authorized_user == '':
            print('You are not logged in.')
        else:
            donation = homepage.donate(authorized_user)
            donations.append(donation)

    elif user_option == '4':
        homepage.show_donations(donations)

    elif user_option == '5':
        print('\nLeaving DonateMe...\n')
        break
