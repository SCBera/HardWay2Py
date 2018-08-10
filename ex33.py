i = 0
numbers = [] # used to make a list of things

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i) # appends no. in the list

    i += 1 # this is nothing but i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")
# to read the elements in a list
for num in numbers:
    print(num)