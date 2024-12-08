def start_adventure():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest.")
    print("You can go 'left' or 'right'.")

    choice = input("> ")
    
    if choice == "left":
        print("foo")
        print("bar")
        choice = input("> ")
        if choice == "foo":
            print("You gain riches but lose your way.")
            print("Game over")("You gain riches but lose your way.")
        elif choice == "bar":
            print("foobar")
        else: 
            print("Invalid choice. Game over.")
    elif choice == "right":
        print("baz")
        print("foobaz")
        if choice == "baz":
            print("You defeat a fearsome troll.")
            print("You win")
        elif choice == "foobaz":
            print("foobarbaz")
            print("bazbarfoo")
        else:
            print("Invalid choice. Game over.")
    else:
        print("Invalid choice. Game over.")
start_adventure()





