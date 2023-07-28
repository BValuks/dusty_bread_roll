import random

def game():
    print("Welcome to the Dusty Bread Roll Adventure!")
    print("You are Lily, a girl with an undying love for dusty bread rolls.")
    print("Your mission is to find the ultimate dusty bread roll in a magical bakery.")

    inventory = []

    while True:
        print("\nWhat would you like to do?")
        print("1. Search for dusty bread rolls")
        print("2. Talk to the baker")
        print("3. Check your inventory")
        print("4. Quit the game")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nYou search the bakery shelves for the perfect dusty bread roll.")
            roll_found = random.choice(["plain roll", "cinnamon roll", "poppy seed roll"])
            print("You found a", roll_found, "covered in a delicate layer of dust!")
            inventory.append(roll_found)

        elif choice == "2":
            print("\nYou approach the baker and ask about the dusty bread rolls.")
            print("The baker smiles and says, 'Ah, the dusty bread rolls! Only a true connoisseur appreciates them.'")
            print("The baker offers you a special discount on your next dusty bread roll.")

        elif choice == "3":
            blank_list = []
            print("\nYou check your inventory and find:")
            if inventory:
                for item in inventory:
                    if item not in blank_list:
                        blank_list.append(item)
                        if inventory.count(item) > 1:
                            print (f"- {inventory.count(item)} x {item}")
                        else:
                            print("-", item)
            else:
                print("Your inventory is empty.")

        elif choice == "4":
            print("\nThank you for playing the Dusty Bread Roll Adventure!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")

game()
