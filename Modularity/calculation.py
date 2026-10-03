# calculation.py

def calculate_subtotal(customer_order, menu):
    subtotal = 0

    for food_number, quantity in customer_order.items():
        price = menu[food_number]["price"]
        subtotal += price * quantity

    return subtotal


def calculate_discount(subtotal):

    if subtotal >= 2500:
        discount_rate = 0.15

    elif subtotal >= 1500:
        discount_rate = 0.10

    elif subtotal >= 1000:
        discount_rate = 0.05

    else:
        discount_rate = 0

    return subtotal * discount_rate


def calculate_final_bill(subtotal, discount):
    return subtotal - discount