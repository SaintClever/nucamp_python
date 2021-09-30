# Used to terminate application without Traceback / NameError error
import sys
import os

play_game = True

# Assign the variables within the loop to have the same starting state
while play_game:
    wizard = 'Wizard'
    elf = 'Elf'
    human = 'Human'
    orc = 'Orc'

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 200

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 175

    dragon_hp = 300
    dragon_damage = 50

    while True:
        print('\n1) Wizard\
                \n2) Elf\
                \n3) Human\
                \n4) Orc\
                \n5) Exit'
              )

        choose_your_character = input('\nChoose your character: ').lower()

        if choose_your_character == '1' or choose_your_character == 'wizard':
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif choose_your_character == '2' or choose_your_character == 'elf':
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif choose_your_character == '3' or choose_your_character == 'human':
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif choose_your_character == '4' or choose_your_character == 'orc':
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        elif choose_your_character == '5' or choose_your_character == 'exit':
            print('Goodbye!\n')
            # Used to prevent Traceback / NameError error
            sys.exit()
        else:
            print('Unknown character')

    print(
        f'\nYou have chosen the character: {character}\
          \nHealth: {my_hp}\
          \nDamage: {my_damage}'
    )

    while True:
        dragon_hp -= my_damage
        print(
            f'\nThe {character} damaged the Dragon!\
              \nThe Dragon\'s hitpoints are now: {dragon_hp}'
        )

        if dragon_hp <= 0:
            print('\nThe Dragon has lost the battle.')
            break

        my_hp -= dragon_damage
        print(
            f'\nThe Dragon strikes back at {character}\
              \nThe {character}\'s hitpoints are now: {my_hp}'
        )

        if my_hp <= 0:
            print(f'\nThe {character} has lost the battle.')
            break

    # Ask the user if they want to play again
    play_game = input('\nDo you want to play again y/n: ').lower()
    os.system('cls||clear')  # Clear the terminal

    if play_game == 'n':
        print('Goodbye!')
        play_game = False
    elif play_game == 'y':
        play_game = True
    else:
        # If they don't provide y or n exit the game
        print('Invalid input. Goodbye!\n')
        sys.exit()
