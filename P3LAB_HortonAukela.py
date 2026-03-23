# Aukela Horton
# 03/22/2026
# P3LAB
# This program converts a money amount into the fewest number of dollars, quarters, dimes, nickels, and pennies.

amount = float(input("Enter the amount of money: "))

cents = int(amount * 100)

dollars = cents // 100
cents = cents - (dollars * 100)

quarters = cents // 25
cents = cents - (quarters * 25)

dimes = cents // 10
cents = cents - (dimes * 10)

nickels = cents // 5
cents = cents - (nickels * 5)

pennies = cents

if dollars > 0:
    if dollars == 1:
        print("1 Dollar")
    else:
        print(dollars, "Dollars")

if quarters > 0:
    if quarters == 1:
        print("1 Quarter")
    else:
        print(quarters, "Quarters")

if dimes > 0:
    if dimes == 1:
        print("1 Dime")
    else:
        print(dimes, "Dimes")

if nickels > 0:
    if nickels == 1:
        print("1 Nickel")
    else:
        print(nickels, "Nickels")

if pennies > 0:
    if pennies == 1:
        print("1 Penny")
    else:
        print(pennies, "Pennies")