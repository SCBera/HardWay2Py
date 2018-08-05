types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}" # {} keeps the space for variable
# that can be called by .format

print(joke_evaluation.format(hilarious))
# for my own interest
print(f"{joke_evaluation} {hilarious}")
print(f"{joke_evaluation}".format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w+e) # it will add the strings without any space