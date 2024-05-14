# Step 2: Define Inventory
inventory = {
    "water": 1000,
    "coffee_beans": 500,
    "milk": 300,
    }

# Step 3: Display Menu Options
menu = {
    "espresso": {"water": 50, "coffee_beans": 25, "milk": 0, "price": 1.5},
    "latte": {"water": 100, "coffee_beans": 30, "milk": 100, "price": 2.5},
    "cappuccino": {"water": 120, "coffee_beans": 30, "milk": 150, "price": 3.0},
}

# Step 4: Handle User Input
def process_order():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice in menu:
            return choice
        elif choice == "off":
            return "off"
        else:
            print("Invalid choice. Please try again.")

# Step 5: Check Resources
def check_resources(drink):
    for ingredient, quantity in menu[drink].items():
        if ingredient != "price" and inventory[ingredient] < quantity:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

# Step 6: Process Payments
def process_payment(drink):
    cost = menu[drink]["price"]
    print(f"The cost of {drink} is ${cost}.")
    total = 0
    while total < cost:
        total += float(input("Please insert coins (quarters: 0.25, dimes: 0.10, nickels: 0.05, pennies: 0.01): "))
    change = total - cost
    if change > 0:
        print(f"Here is ${change:.2f} in change.")
    print("Payment successful. Enjoy your drink!")

# Step 7: Dispense Drink
def dispense_drink(drink):
    print(f"Making {drink}...")
    for ingredient, quantity in menu[drink].items():
        if ingredient != "price":
            inventory[ingredient] -= quantity
    print(f"Here is your {drink}. Enjoy!")

# Step 8: Update Inventory
def update_inventory():
    print("Updating inventory...")
    print("Inventory updated successfully.")

# Step 9: Provide Exit Option
def exit_coffee_machine():
    print("Turning off the coffee machine. Goodbye!")

# Main Program Loop
while True:
    user_choice = process_order()
    if user_choice == "off":
        exit_coffee_machine()
        break
    elif check_resources(user_choice):
        process_payment(user_choice)
        dispense_drink(user_choice)
        update_inventory()
