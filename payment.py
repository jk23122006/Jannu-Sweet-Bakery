class Payment:
    """This class stores payment details."""

    def __init__(self):
        self.method = ""

    def choose_payment(self):
        print("\nHow would you like to pay?")
        print("1. Card")
        print("2. Cash")

        choice = input("Choose 1 or 2: ")

        if choice == "1":
            self.method = "Card"
        elif choice == "2":
            self.method = "Cash"
        else:
            self.method = "Unknown"

    def show_payment(self):
        print("Payment method:", self.method)

    def get_method(self):
        return self.method

    def thank_customer(self):
        print("Thank you so much for visiting Jannu's Sweet Bakery!")