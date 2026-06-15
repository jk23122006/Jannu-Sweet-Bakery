

class Menu:
    """This class stores one bakery menu item."""

    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def show_item(self):
        print(self.id + ".", self.name, "-", self.price, "euro")

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_category(self):
        return self.category