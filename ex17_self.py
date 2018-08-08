from sys import argv
from os.path import exists

scipt, in_file, out_file = argv

indata = (open(in_file)).read() #defaut open mode is read or 'r'

print(f"Exists out_file? {exists(out_file)}.\nInput file {len(indata)} bytes long.")

(open(out_file, 'w')).write(indata)

#in_file.close() # close() not working in this way.
#out_file.close()

print("All done.")