# if statements!

keep_going = ""
while keep_going == "":

    like_coffee = input("do you like coffee? ").lower()

    if like_coffee == "yes" or like_coffee == "y":
        print ("i like coffee too")
    elif like_coffee == "no" or like_coffee =="n":
        print("you are missing out")
    else:
        print ("i don't understand")

    keep_going = input( "press <enter> to continue or any key to quit")
    print()
