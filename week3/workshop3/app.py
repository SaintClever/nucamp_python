from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

'''
or
from donations_pkg import homepage, user
homepage.show_hompage, homepage.donate, show_donations.homepage
user.login, user.register
'''

database = {'admin': 'password123'}
donations = []
authorized_user = ''


while True:
    # inovke show_homepage imported from homepage
    show_homepage()

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
        authorized_user = login(database, username, password)

    elif user_option == '2':
        username = input('\nusername: ')
        password = input('password: ')
        authorized_user = register(database, username)

        # MUST not be an EMPTY string TODO: add len(authorized_user) >= 0
        if authorized_user != ' ':
            database[username] = password

    elif user_option == '3':
        if authorized_user == '':
            print('You are not logged in.')
        else:
            donation = donate(authorized_user)
            donations.append(donation)

    elif user_option == '4':
        show_donations(donations)

    elif user_option == '5':
        print('\nLeaving DonateMe...\n')
        break
