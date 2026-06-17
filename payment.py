

class Payment:


    def __init__(self):
        self.method = ""

    def choose_payment(self):
        print("\nHow would you like to pay?")
        print("1. Card")
        print("2. Cash")

        choice = input("Choose 1 or 2: ")

        while choice != "1" and choice != "2":
            print("Wrong choice. Please try again.")
            choice = input("Choose 1 or 2: ")

        if choice == "1":
            self.method = "Card"
        elif choice == "2":
            self.method = "Cash"

    def show_payment(self):
        print("Payment method:", self.method)

    def get_method(self):
        return self.method

    def thank_customer(self):
        print("Thank U for visiting Jannu's Sweet Bakery")

    def paid(self):
        if self.method == "":
            return False
        else:
            return True