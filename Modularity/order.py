# order.py

def select_food(menu):
    while True:
        choice = input("\nSelect food number: ").strip()

        if choice in menu:
            return choice

        print("That food number is not available.")
        print("Please choose a number shown on the menu.")


def select_quantity():
    while True:
        try:
            amount = int(input("Enter quantity: "))

            if amount > 0:
                return amount

            print("Please enter a quantity greater than 0.")

        except ValueError:
            print("Invalid input. Enter a whole number.")


def create_order(menu):
    customer_order = {}

    while True:

        food_number = select_food(menu)
        quantity = select_quantity()

        if food_number not in customer_order:
            customer_order[food_number] = quantity
        else:
            customer_order[food_number] += quantity

        food_name = menu[food_number]["name"]

        print(
            f"\nAdded {quantity} x {food_name} "
            "to your order."
        )

        while True:
            continue_order = input(
                "\nAdd another food item? [Y/N]: "
            ).strip().lower()

            if continue_order == "y":
                break

            if continue_order == "n":
                return customer_order

            print("Invalid response. Please enter Y or N.")