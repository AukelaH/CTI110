# Aukela Horton
# May 13, 2026
# Final Project
# A text-based treasure adventure game using loops, functions, dictionaries, random, and time.

import random
import time


def pause():
    time.sleep(1)


def show_intro():
    print("🏝️ Welcome to Treasure Island Adventure! 🏝️")
    pause()
    print("You are an explorer searching for hidden treasure.")
    pause()
    print("Choose wisely. Your energy, coins, and inventory will change as you play.")
    pause()


def show_status(player):
    print("\n--- Player Status ---")
    print(f"Name: {player['name']}")
    print(f"Energy: {player['energy']}")
    print(f"Coins: {player['coins']}")
    print(f"Inventory: {player['inventory']}")
    print("---------------------\n")


def explore_jungle(player):
    print("🌴 You walk into the jungle...")
    pause()

    event = random.choice(["coins", "snake", "map"])

    if event == "coins":
        coins_found = random.randint(5, 15)
        player["coins"] += coins_found
        print(f"Nice! You found {coins_found} coins!")

    elif event == "snake":
        energy_lost = random.randint(5, 15)
        player["energy"] -= energy_lost
        print(f"Oh no! A snake scared you and you lost {energy_lost} energy.")

    elif event == "map":
        if "map" not in player["inventory"]:
            player["inventory"].append("map")
            print("You found an old treasure map!")
        else:
            print("You found another old map, but you already have one.")

    pause()


def visit_beach(player):
    print("🏖️ You visit the beach...")
    pause()

    event = random.choice(["rest", "shells", "storm"])

    if event == "rest":
        energy_gained = random.randint(10, 20)
        player["energy"] += energy_gained
        print(f"You rested by the water and gained {energy_gained} energy.")

    elif event == "shells":
        coins_found = random.randint(3, 10)
        player["coins"] += coins_found
        print(f"You found shiny shells worth {coins_found} coins.")

    elif event == "storm":
        energy_lost = random.randint(5, 12)
        player["energy"] -= energy_lost
        print(f"A sudden storm hit! You lost {energy_lost} energy.")

    pause()


def enter_cave(player):
    print("🕯️ You enter a dark cave...")
    pause()

    if "map" in player["inventory"] and player["coins"] >= 20:
        print("Your map leads you to the treasure chest!")
        pause()
        print("You use 20 coins to unlock it...")
        player["coins"] -= 20
        player["inventory"].append("treasure")
        print("🎉 Congratulations! You found the hidden treasure!")
    else:
        print("You need a map and at least 20 coins to unlock the treasure chest.")
        energy_lost = random.randint(5, 10)
        player["energy"] -= energy_lost
        print(f"Searching the cave made you tired. You lost {energy_lost} energy.")

    pause()


def get_choice():
    print("What would you like to do?")
    print("1. Explore the jungle")
    print("2. Visit the beach")
    print("3. Enter the cave")
    print("4. Show player status")
    print("5. Quit game")

    choice = input("Enter your choice: ")
    return choice


def play_game():
    player = {
        "name": "Aukela",
        "energy": 50,
        "coins": 10,
        "inventory": []
    }

    show_intro()

    game_running = True

    while game_running:
        if player["energy"] <= 0:
            print("You ran out of energy. Game over!")
            break

        if "treasure" in player["inventory"]:
            print("You won the game! 🏆")
            break

        choice = get_choice()

        if choice == "1":
            explore_jungle(player)
        elif choice == "2":
            visit_beach(player)
        elif choice == "3":
            enter_cave(player)
        elif choice == "4":
            show_status(player)
        elif choice == "5":
            print("Thanks for playing!")
            game_running = False
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

    print("\nFinal Status:")
    show_status(player)


def main():
    play_game()


main()