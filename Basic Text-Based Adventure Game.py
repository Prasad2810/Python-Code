def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark room.")
    print("There are two doors: one to the left and one to the right.")
    print("Which door will you choose? (left/right)")

def left_room():
    print("\nYou enter the left room and find a treasure chest!")
    print("Do you want to open it? (yes/no)")
    choice = input("> ").lower()
    if choice == "yes":
        print("Congratulations! You found the treasure and won the game!")
    else:
        print("You leave the chest unopened and exit the room. Game over.")

def right_room():
    print("\nYou enter the right room and encounter a fierce dragon!")
    print("Do you want to fight the dragon or run away? (fight/run)")
    choice = input("> ").lower()
    if choice == "fight":
        print("You bravely fight the dragon and win! You are a hero!")
    else:
        print("You run away safely, but you missed out on the adventure. Game over.")

def main():
    intro()
    choice = input("> ").lower()
    if choice == "left":
        left_room()
    elif choice == "right":
        right_room()
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")

if __name__ == "__main__":
    main()