from sys import exit


def gold_room():
	print("This room is full of gold. How much do you take?")

	choice = input("> ")

	if choice.lower() in ["all", "everything", "too much"]:
		dead("You are greedy bastard!")
	else:
		try:
			how_much = float(choice)  # only work for number input
			if how_much < 50.0:
				print("Nice, you're not greedy, you win!")
				exit(0)
			else:
				dead("You greedy bastard!")
		except:
			dead("Man, learn to type properly.")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("(You can try to: take honey/taunt bear/open the door/...)> ")

        if choice == "open the door" and not bear_moved:
            print("You need to move the bear to open the door!")
        elif choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can 'open the door' and go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open the door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you 'flee' for your life or eat your 'head'?")

    choice = input("> ")

    if "flee" in choice:
        print("You can't flee from Cthulhu's room")
        start()  # goes to the bottom of the code
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good try! Better luck next time!")
    exit(0)


def start():
    print("You are in dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("(right/left/..?)>")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
