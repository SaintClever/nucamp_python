import random
import os

high_score = 0


def dice_game():
    play_game = True
    global high_score

    while play_game:
        print(f'\nCurrent High Score: {high_score}\
                \n1) Roll Dice\
                \n2) Leave Game')

        # Create the dice and user_input
        dice = [random.randint(1, 6), random.randint(1, 6)]
        user_input = input('Enter your choice: ')

        # Print rolled dice and dice total
        if user_input == '1':
            os.system('cls||clear')  # Clear the terminal
            print(f'\nYou roll a... {dice[0]}\
                    \nYou roll a... {dice[1]}\
                    \n\nYou have rolled a total of: {dice[0] + dice[1]}')

            # Present new high_score if dice[0] and dice[1] is greater than current high_score
            if dice[0] + dice[1] > high_score:
                high_score = dice[0] + dice[1]
                print('\nNew high score!')

        elif user_input == '2':
            play_game = False
            print('Goodbye!\n')
        else:
            print('Invalid input. Try 1 or 2')


dice_game()
