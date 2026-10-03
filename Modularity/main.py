# main.py

from menu import get_menu
from display import (
    restaurant_title,
    display_food_menu,
    confirm_order,
    display_discount
)
from order import create_order
from calculation import (
    calculate_subtotal,
    calculate_discount,
    calculate_final_bill
)
from receipt import print_receipt


def main():

    # Get menu
    menu = get_menu()

    # Display restaurant title
    restaurant_title()

    # Display food menu
    display_food_menu(menu)

    # Ask if customer wants to order
    if not confirm_order():

        print("\n" + "-" * 60)
        print("Thank you for visiting Crispy Corner!")
        print("Have a wonderful day!")
        print("-" * 60)

        return

    # Create customer order
    customer_order = create_order(menu)

    # Calculate subtotal
    subtotal = calculate_subtotal(
        customer_order,
        menu
    )

    # Calculate discount
    discount = calculate_discount(subtotal)

    # Calculate final bill
    final_bill = calculate_final_bill(
        subtotal,
        discount
    )

    # Display discount
    display_discount(
        subtotal,
        discount
    )

    # Print receipt
    print_receipt(
        customer_order,
        menu,
        subtotal,
        discount,
        final_bill
    )


if __name__ == "__main__":
    main()