name = "SUBHAS"
guess = input("I'm thinking a name. Try to guess it! >")
chances = 0

while guess.upper() != name and chances < 2:
    print(
        f"Nope, that's not right! Hint: letter {chances + 1} is {name[chances]}.")
    guess = input(f"You can guess {2-chances} more time(s):")
    chances += 1

if chances == 2 and guess != name:
    print(f"Not a good guess. The name was: {name}.")
elif chances == 0 and guess.upper() == name:
    print(f"Excellent! You did it in first guess.")
else:
    print(f"Excellent! You did it in {chances+1} guesses.")
