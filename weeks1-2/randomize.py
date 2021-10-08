import random


# randint()
pips = random.randint(1, 6)

print("You roll the die... it lands with", pips, "pips showing.")


# choice()
prizes = ["a car", "$10000", "a pony", "$500000"]
prize_won = random.choice(prizes)

print("You turn the wheel of fortune... It lands on a prize of", prize_won + "!!")


# shuffle()
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(cards)
print(cards)

# randomize a dict
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
l = list(d.items())
random.shuffle(l)
d = dict(l)
print(d)
