#from sys import exit
choice = input("> ")
user_input = ["all", "All", "everything", "Everything"]
for string in user_input:
    print(string)
    break
    if choice == string:
        print("You greedy bastard!")
        #break


#for num in range(0, 10):
#    print(num, choice)
#    if choice == string in user_input:
#        print(choice)
#    elif str(num) in choice:
#        how_much = int(choice)
#        print("found!", how_much)
#        #exit(0) # exception error!
#        break
#    elif str(num) not in choice and num < 9:
#        print("will cont..")
    else:
        continue
print("Man, learn to type a good number.")