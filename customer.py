"""Stores Customer info"""


class Customer:


    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    

    def get_title(self):
        if self.gender == "Male":
            return "sir"
        elif self.gender == "Female":
            return "maam"
        else:
            return "dear customer"
        
    def say_hi(self):
        print("\nHiii", self.name, "welcome to our bakery!")

    
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

    def get_name(self):
        return self.name

   