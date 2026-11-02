print(
    "================================\n"
    "       THE LOST LIGHTHOUSE\n"
    "================================\n"
    "Welcome to Mystery Island!\n"
    "You wake up on a mysterious beach.\n"
    "The lighthouse is dark, and you need to find a way to escape.\n"
)

player_name = input("What is your name?: ")
print(f"Welcome, {player_name}!")

energy = 5
current_location = "Beach"
inventory = []

choice = ""

while choice != "3":
    print(
        "\n========== GAME MENU ==========\n"
        "1. Explore\n"
        "2. Check inventory\n"
        "3. Quit\n"
    )

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"You are exploring the {current_location}.")

    elif choice == "2":
        if inventory:
            print(f"Your inventory: {inventory}")
        else:
            print("Your inventory is empty!")

    elif choice == "3":
        print("Goodbye, adventurer!")

    else:
        print("Invalid choice. Try again.")