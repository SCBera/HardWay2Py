from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit RETURN.")

input("?")

print(f"Opening the file...{filename}")
target = open(filename, 'w') # 'w' opens the file for writing

print("Truncating the file. Goodbye!")
#target.truncate() # Deletes everything from the file, same does in 'w' mode.

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#target.write(line1) # write() takes exactly one argument!
#target.write("\n")
#target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
target.close()