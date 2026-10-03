# ==========================================
#      CRISPY CORNER - PYTHON OOP
# ==========================================

from Modularity.menu import get_menu
from Modularity.display import (
    restaurant_title,
    display_food_menu,
    confirm_order,
    display_discount
)
from Modularity.order import create_order
from Modularity.calculation import (
    calculate_subtotal,
    calculate_discount,
    calculate_final_bill
)
from Modularity.receipt import print_receipt


# ==========================================
#           RESTAURANT CLASS
# ==========================================

class Restaurant:

    def __init__(self):
        self.menu = get_menu()
        self.customer_order = {}
        self.subtotal = 0
        self.discount = 0
        self.final_bill = 0

    def show_restaurant(self):
        restaurant_title()

    def show_menu(self):
        display_food_menu(self.menu)

    def place_order(self):
        self.customer_order = create_order(self.menu)

    def calculate_bill(self):

        self.subtotal = calculate_subtotal(
            self.customer_order,
            self.menu
        )

        self.discount = calculate_discount(
            self.subtotal
        )

        self.final_bill = calculate_final_bill(
            self.subtotal,
            self.discount
        )

    def show_discount(self):
        display_discount(
            self.subtotal,
            self.discount
        )

    def show_receipt(self):
        print_receipt(
            self.customer_order,
            self.menu,
            self.subtotal,
            self.discount,
            self.final_bill
        )

    def run(self):

        self.show_restaurant()

        self.show_menu()

        if not confirm_order():

            print("\n" + "-" * 60)
            print("Thank you for visiting Crispy Corner!")
            print("Have a wonderful day!")
            print("-" * 60)

            return

        self.place_order()

        self.calculate_bill()

        self.show_discount()

        self.show_receipt()


# ==========================================
#              RUN PROGRAM
# ==========================================

restaurant = Restaurant()
restaurant.run()