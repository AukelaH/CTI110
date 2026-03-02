# Aukela Horton
# 03/02/2026
# P1HW2 - Travel Budget Calculator
# This program collects a user's travel budget and expenses, calculates total expenses, and displays remaining balance.

# Pseudocode:
# 1. Ask the user for their travel budget
# 2. Ask the user for their travel destination
# 3. Ask for gas expenses
# 4. Ask for accommodation expenses
# 5. Ask for food expenses
# 6. Add all expenses together
# 7. Subtract total expenses from the budget
# 8. Display destination, budget, expenses, and remaining balance

def main():
	print("This program calculates and displays travel expenses\n")

	try:
		budget = float(input("Enter Budget: "))
	except ValueError:
		print("Invalid budget. Please enter a number.")
		return

	destination = input("Enter your travel destination: ")

	try:
		gas = float(input("How much will you spend on gas? "))
		hotel = float(input("How much will you spend on accommodation? "))
		food = float(input("How much will you spend on food? "))
	except ValueError:
		print("Invalid expense. Please enter numeric values.")
		return

	total_expenses = gas + hotel + food
	remaining_balance = budget - total_expenses

	print("\n------------Travel Expenses------------")
	print("Location:", destination)
	print("Initial Budget: ${:.2f}".format(budget))
	print("\nFuel: ${:.2f}".format(gas))
	print("Accommodation: ${:.2f}".format(hotel))
	print("Food: ${:.2f}".format(food))
	print("\nTotal Expenses: ${:.2f}".format(total_expenses))
	print("Remaining Balance: ${:.2f}".format(remaining_balance))

if __name__ == "__main__":
	main()

