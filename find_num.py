import re

s = input("> ")
m = re.match(r"([a-zA-Z]+)([0-9]+)",s) or re.match(r"([0-9]+)([a-zA-Z]+)",s) # not working with operator sign e.g., +/-/* etc.
print(m.group(0))
print(m.group(1))
print(m.group(2))


strings = [input("> ")]
#strings = ['foofo21', 'bar432', 'foobar12345']
[re.findall(r'(\w+?)(\d+)', s)[0] for s in strings]