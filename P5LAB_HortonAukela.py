# Aukela Horton
# 04/26/2026
# P5LAB
# Self-checkout program that calculates and disperses change using functions

import random

def disperse_change(change):
    change = round(change, 2)
    cents = int(change * 100)

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    print("\nChange to be given:")
    print("Dollars:", dollars)
    print("Quarters:", quarters)
    print("Dimes:", dimes)
    print("Nickels:", nickels)
    print("Pennies:", pennies)

def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print("Total owed: $", total_owed)

    cash = float(input("Enter amount of cash provided: $"))

    change = cash - total_owed

    if change < 0:
        print("Not enough money provided.")
    else:
        print("Change owed: $", round(change, 2))
        disperse_change(change)

main()