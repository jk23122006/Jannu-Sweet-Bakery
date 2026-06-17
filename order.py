

class Order:


    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)
        print(menu_item.get_name(), "added to your order!!!!")

    def view_order(self, customer):
        if len(self.items) == 0:
            print("You haven't ordered anything yet....")
        else:
            print("\nHiii", customer.get_name(), "you ordered:-")

            for item in self.items:
                print("-", item.get_name())

    def calculate_total(self):
        total = 0

        for item in self.items:
            total = total + item.get_price()

        return total

    def show_bill(self, customer, mood_msg):
        print("\nHere is ur bill", customer.get_title())
        print("-------------------------")
        customer.show_details()
        print("-------------------------")

        number = 1

        for item in self.items:
            print(number, item.get_name(), "-", item.get_price(), "euro")
            number = number + 1

        print("-------------------------")
        print("Total:", self.calculate_total(), "euro")
        print("-------------------------")

        print("\n A little note for you:")
        print(mood_msg)

    def save_order(self, customer, payment):
            file = open("orders.txt", "a")

            file.write("Customer: " + customer.name + "\n")
            file.write("Age: " + str(customer.age) + "\n")
            file.write("Gender: " + customer.gender + "\n")

            for item in self.items:
                file.write(
                    item.get_name() + " - " + str(item.get_price()) + " euro\n"
                )

            file.write("Total: " + str(self.calculate_total()) + " euro\n")
            file.write("Payment: " + payment.get_method() + "\n")
            file.write("-------------------------\n")

            file.close()


    def empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False