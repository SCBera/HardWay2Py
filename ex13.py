from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
fourth = input('Your name:')

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print(f"My name is {fourth}")