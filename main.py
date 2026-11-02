print(
"================================\n"
"       THE LOST LIGHTHOUSE\n"
"================================\n"
"Welcome to Mystery Island!\n"
"You wake up on a mysterious beach.\n"
"The lighthouse is dark, and you need to find a way to escape.\n"
"1. Explore\n"
"2. Check inventory\n"
"3. Quit\n"
)

player_name = input("What is your name?: ")
print(f"Welcome, {player_name}!")
choice = input("Choose an option: ")

if choice == "1":
    print("Exploring the island...")

elif choice == "2":
    print("Inventory is empty!")

elif choice == "3":
    print("Goodbye, adventurer!")

else:
    print("Invalid choice. Try again")