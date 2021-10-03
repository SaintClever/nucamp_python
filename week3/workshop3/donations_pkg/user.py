def login(database, username, password):
    if username in database and database[username] == password:
        print(f'\nWelcome back {username}!')
        return username
    elif username in database and database[username] != password:
        print(f'\nIncorrect password for {username}!')
        return ''
    else:
        print('User not found. Please register.')
        return ''


def register(database, username):
    if username in database:
        print('\nUsername already registered.')
        return ''
    else:
        print(f'\nUsername {username} registered!')
        return ''
