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
        print("4. Explore different locations")
        print("5. Quit the game")

        choice = input("Enter your choice (1-5): ")

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
            print("\nYou check your inventory and find:")
            if inventory:
                for item in inventory:
                    print("-", item)
            else:
                print("Your inventory is empty.")

        elif choice == "4":
            print("\nWhere would you like to explore?")
            print("1. Garden")
            print("2. Forest")
            print("3. Secret Cave")

            location_choice = input("Enter your choice (1-3): ")

            if location_choice == "1":
                print("\nYou venture into the beautiful garden.")
                print("Amidst the flowers and butterflies, you discover a hidden path.")

                if "key" in inventory:
                    print("You use the key you found earlier to unlock a dusty bread roll treasure chest!")
                    print("Inside, you find a legendary dusty bread roll!")
                    inventory.append("legendary dusty bread roll")
                else:
                    print("You notice a locked chest. It seems you need a key to open it.")

            elif location_choice == "2":
                print("\nYou make your way into the enchanting forest.")
                print("As you wander deeper, you come across a mischievous squirrel.")

                if "nuts" in inventory:
                    print("You offer the squirrel some nuts from your inventory.")
                    print("Grateful, the squirrel leads you to a hidden stash of dusty bread rolls!")
                    print("You add them to your inventory.")
                    inventory.append("hidden stash of dusty bread rolls")
                else:
                    print("The squirrel scurries away, leaving you wondering if it knows something about dusty bread rolls.")

            elif location_choice == "3":
                print("\nYou embark on an adventure into the mysterious secret cave.")
                print("With each step, the air becomes colder, and the echoes grow louder.")

                if "torch" in inventory:
                    print("Using the torch you found earlier, you navigate through the dark cave.")
                    print("Deep inside, you discover a forgotten dusty bread roll recipe!")
                    print("You add it to your inventory.")
                    inventory.append("forgotten dusty bread roll recipe")
                else:
                    print("It's too dark to explore further. You realize you need a source of light.")

            else:
                print("\nInvalid choice. Please enter a number from 1 to 3.")

        elif choice == "5":
            print("\nThank you for playing the Dusty Bread Roll Adventure!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")

game()
