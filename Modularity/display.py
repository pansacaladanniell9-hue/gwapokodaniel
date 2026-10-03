# display.py

def restaurant_title():
    print("\n" + "=" * 60)
    print("|" + " " * 58 + "|")
    print("|" + "CRISPY CORNER FAST FOOD".center(58) + "|")
    print("|" + "ORDERING SYSTEM".center(58) + "|")
    print("|" + " " * 58 + "|")
    print("=" * 60)


def display_food_menu(menu):
    print("\n" + "-" * 60)
    print("FOOD MENU".center(60))
    print("-" * 60)

    print(f"{'NO.':<8}{'FOOD':<32}{'PRICE':>12}")
    print("-" * 60)

    for number, food in menu.items():
        print(
            f"{number:<8}"
            f"{food['name']:<32}"
            f"PHP {food['price']:>7.2f}"
        )

    print("-" * 60)


def confirm_order():
    while True:
        response = input(
            "\nWould you like to place an order? [Y/N]: "
        ).strip().lower()

        if response == "y":
            return True

        if response == "n":
            return False

        print("Invalid response. Please type Y or N.")


def display_discount(subtotal, discount):
    if discount > 0:
        print(f"\nDiscount applied: PHP {discount:.2f}")
    else:
        print("\nNo discount applied.")