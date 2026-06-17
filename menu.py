

class Menu:


    def __init__(self, item_id, item_name, price, category):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price
        self.category = category

    def show_item(self):
        print(self.item_id + ".", self.item_name, "-", self.price, "euro")

    def get_name(self):
        return self.item_name

    def get_price(self):
        return self.price

    def get_category(self):
        return self.category