from sys import argv

script, filename = argv

txt = open(filename) #opens the file given in filename and
# saves in variable txt.

print(f"Here's your file {filename}:")
print(txt.read()) #reads and prints the content given in the file

print("Type the filename again:")
file_again = input("> ") # can take another/same file as input

txt_again = open(file_again)

print(txt_again.read())