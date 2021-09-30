import random

diamonds = ['AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD']
hand = []

while diamonds:
    user_input = input('\nPress enter to pick a card, or Q then enter to quit: ').upper()

    if user_input == 'Q':
        break
    elif user_input == '':
        '''
        random_card = random.choice(diamonds) # select random choice
        card_index = diamonds.index(random_card) # get the index of that random card

        diamonds.pop(card_index) # pop random card via index
        hand.append(random_card) # append random card to hand
        '''

        # or
        random_card = random.choice(diamonds) # select random choice
        diamonds.remove(random_card) # remove random card from diamonds
        hand.append(random_card) # append random card to hand


    print(f'\nYour hand: {hand}\
            \nRemaining cards: {diamonds}')


if not diamonds:
    print('There are no more cards to pick.\n')