from sys import argv
from sys import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()
# we could do these two on one line...
#indata = open(from_file, 'r')?

print(f"The input file is {len(indata)} bytes long")

print(f"Does the input file exists? {exists(to_file)}")
