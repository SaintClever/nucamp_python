def show_homepage():
    print(f'''
        \n\t\t=== DonateMe HomePage ===\t
        {'-' * 42}
        | 1.    Login     | 2.   Register        |
        {'-' * 42}
        | 3.    Donate    | 4.   Show Donations  |
        {'-' * 42}
        |                5. Exit                 |
        {'-' * 42}
        ''')


def donate(username):
    donation_amt = float(input('\nEnter amount to donate: '))
    donation = f'{username} donated ${donation_amt}'
    print('Thank you for your donation!')
    return donation


def show_donations(donations):
    print('\n--- All Donations ---')
    if donations == []:
        print('Currently, there are no donations.')
    else:
        for donation in donations:
            print(donation)
