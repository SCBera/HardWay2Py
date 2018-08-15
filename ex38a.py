ten_things = "Apples Orages Cows Telephone Light Suger"

print("Things:", ten_things)
# splits in a list of items from a string
stuff = ten_things.split()
print("Stuffs in things:", stuff)
# sorts alphabatically but doesn't save it!
print("Stuffs in things in order:", sorted(stuff))
stuff = sorted(stuff)
print("Wait, there are {} things instead of 10 things in that list. Let's fix that.".format(len(stuff)))
print("Stuffs in things again:", stuff)
# pop() retuns and remove the last item in a list, pop([i]) or simply pop(i) return and remove the i-th item
print("pop last item from stuff:", stuff.pop())
print("poped stuff:", stuff)
print("pop fast item from stuff:", stuff.pop(0))
print("poped stuff again:", stuff)

more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

# while len(stuff) != 10:
for things in stuff:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
    if len(stuff) == 10:
        break

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print("The 2nd element:", stuff[1])  # prints 2nd (0, 1) element from a list
print("The last element:", stuff[-1])  # prints last element from a list
# print("pop:", stuff.pop(), stuff)
print("join stuff:", ' '.join(stuff))  # joins elements from a list with space
print('#'.join(stuff[3:5]))  # joins 4th and 6th elements with
