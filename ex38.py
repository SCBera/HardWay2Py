ten_things = "Apples Orages Cows Telephone Light Suger"

print("Things:", ten_things)
print("Wait, there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # for len(stuff) < 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print("The 2nd element:", stuff[1])  # prints 2nd (0, 1) element from a list
print("The last element:", stuff[-1])  # prints last element from a list
print("pop:", stuff.pop(), stuff)
print("join stuff:", ' '.join(stuff))  # joins elements from a list with space
print('#'.join(stuff[3:5]))  # joins 4th and 6th elements with #
