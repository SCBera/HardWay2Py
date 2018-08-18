import random

names = ["Subhas", "Banka", "Nibedita", "Reynna"]

name = random.choice(names)

guess = input("I'm thinking a name. Try to guess it! >")
chances = 0

while guess.upper() != name.upper() and chances < 3:
    print(
        f"Nope, that's not right! Hint: It's a {len(name)} letter word with letter {chances + 1} is {name[chances]}.")
    guess = input(f"You can guess {3-chances} more time(s):")
    chances += 1

if chances == 3 and guess != name:
    print(f"Not a good guess. The name was: {name}.")
elif chances == 0 and guess.upper() == name:
    print(f"Excellent! You did it in first guess.")
else:
    print(f"Great! You did it in {chances+1} guesses.")
