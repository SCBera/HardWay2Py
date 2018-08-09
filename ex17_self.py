from sys import argv
from os.path import exists

scipt, from_file, to_file = argv

in_file = open(from_file) #default open mode is read or 'r'
indata = in_file.read() 

print(f"Exists out_file? {exists(to_file)}.\nInput file {len(indata)} bytes long.")

new_file = open(to_file, 'w')
new_file.write(indata)

in_file.close()
new_file.close()

print("All done.")