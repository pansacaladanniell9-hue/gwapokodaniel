# receipt.py

def print_receipt(
    customer_order,
    menu,
    subtotal,
    discount,
    final_bill
):

    print("\n\n" + "=" * 64)
    print("CRISPY CORNER".center(64))
    print("FAST FOOD SHOP".center(64))
    print("=" * 64)

    print("SALES RECEIPT".center(64))
    print("-" * 64)

    print(
        f"{'ITEM':<27}"
        f"{'QTY':>6}"
        f"{'UNIT':>13}"
        f"{'TOTAL':>14}"
    )

    print("-" * 64)

    for food_number, quantity in customer_order.items():

        food_name = menu[food_number]["name"]
        unit_price = menu[food_number]["price"]
        item_total = unit_price * quantity

        print(
            f"{food_name:<27}"
            f"{quantity:>6}"
            f"PHP {unit_price:>8.2f}"
            f"PHP {item_total:>9.2f}"
        )

    print("-" * 64)

    print(
        f"{'SUBTOTAL':>50}"
        f" PHP {subtotal:>9.2f}"
    )

    print(
        f"{'DISCOUNT':>50}"
        f" PHP {discount:>9.2f}"
    )

    print("-" * 64)

    print(
        f"{'AMOUNT DUE':>50}"
        f" PHP {final_bill:>9.2f}"
    )

    print("=" * 64)
    print("THANK YOU!".center(64))
    print("COME BACK SOON!".center(64))
    print("=" * 64)