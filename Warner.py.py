def main():
    print("You enter a dark room with two doors.")

    answer = input("Do you enter Door #1 or Door #2?")
    if answer == "1":
        print("There is a giant bear eating a cheese cake.")
        print("What do you do?")
        print("1. Take the cake.")
        print("2. Scream at the bear.")
        answer = input("")
        if answer == "1":
            print("Bear eats your arms off.")

        elif answer == "2":
            print("Bear eats your legs off.")

    elif answer == "2":
        print("There's a sleeping cat sitting by the fireplace.")
        print("what do you do?")
        print("1. Throw a fish.")
        print("2. Put out the fire.")
        answer = input("")
        if answer == "1":
            print("Cat wakes up and eats fish.")

        elif answer == "2":
            print("Cat wakes up and claws off your face.")


    restart=input("Do you want to play again? [y/n]")
    if restart == "y":
        main()
    else:
        exit()

main()
