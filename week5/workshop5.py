'''random'''
import random


def guess_random_number(tries, start, stop):
    '''Task 1: Guess the number through user input
'''
    target_number = random.randint(start, stop)

    while tries != 0:
        # print(target_number)
        print(f'Number of tries: {tries}')
        user_guess = int(input(f'Guess a number from {start} to {stop}: '))

        if user_guess == target_number:
            print('You guessed the correct number!')
            return
        if user_guess < target_number:
            print('Guess higher!')
        if user_guess > target_number:
            print('Guess lower!')

        tries = tries - 1

        if tries == 0:
            print(f'You have failed to guess the number: {target_number}')


# Test Task 1
# guess_random_number(5, 0, 10)


def guess_random_num_linear(tries, start, stop):
    '''Task 2: Guess the number programmatically through linear search'''

    target_number = random.randint(start, stop)
    print(f'The number for the program to guess is: {target_number}')

    for cpu_guess in range(start, stop + 1):
        # print(cpu_guess, target_number)
        print(
            f'Number of tries left: {tries}\
            \nThe program is guessing... {cpu_guess}'
        )

        if cpu_guess == target_number:
            print('The program has guessed the correct number!')
            return

        tries = tries - 1

        if tries == 0:
            print('The program has failed to guess the correct number.')
            return


# Test Task 2
# guess_random_num_linear(5, 0, 10)


def guess_random_num_binary(tries, start, stop):
    '''Task 3: Guess the number programmatically using binary search'''

    target_number = random.randint(start, stop)
    the_list = list(range(start, stop))
    lower_bound = start
    upper_bound = stop

    print(f'Random number to find: {target_number}')

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]

        if pivot_value == target_number:
            print(f'Found it! {pivot}')
            return pivot

        if pivot_value > target_number:
            upper_bound = pivot - 1
            print('Guessing lower!')
        else:
            lower_bound = pivot + 1
            print('Guessing higher!')

        tries = tries - 1

        if tries == 0:
            print('Your program failed to find the number.')
            return


guess_random_num_binary(5, 0, 100)
