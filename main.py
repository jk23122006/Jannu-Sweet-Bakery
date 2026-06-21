"""Jannu's Sweet Bakery Ordering System"""
"""Main bakery odereing program"""

from customer import Customer
from menu import Menu
from order import Order
from payment import Payment


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("------ WELCOME TO JANNU's Sweet Bakeryyyyy ------")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\nNow we'll ask u few questionsssss......")


name = input("\nWhat is your NAME? ")

#keep asking until the customer enters age as a number
while True:
    try:
        age = int(input("\nWhat is your AGE? "))
        break
    except ValueError:
        print("Please enter ur age as a number.")


print("\nChoose your gender:")
print("1. Male")
print("2. Female")
print("3. Prefer not to say")

gender_choice = input("Enter 1, 2, or 3:- ")

if gender_choice == "1":
    gender = "Male"
elif gender_choice == "2":
    gender = "Female"
else:
    gender = "Prefer not to say"


customer = Customer(name, age, gender)
order = Order()
payment = Payment()

customer.say_hi()


#menu items are categoriezed
menu = [


    Menu("1", "Red Velvet Cake                    ", 30, "Cakes"),
    Menu("2", "Chocolate Fudge Cake               ", 10, "Cakes"),
    Menu("3", "Tiramisu Cake                      ", 35, "Cakes"),
    Menu("4", "Pistachio Cake                     ", 30, "Cakes"),
    Menu("5", "Cookies & Cream Cake               ", 15, "Cakes"),
    Menu("6", "Nutella Brownie                    ", 8, "Cakes"),
    Menu("7", "Butterscotch Cake                  ", 15, "Cakes"),

    Menu("8", "Vanilla Bean                       ", 5, "Ice Creams"),
    Menu("9", "Belgian Chocolate                  ", 10, "Ice Creams"),
    Menu("10", "Kulfi Ice Cream                    ", 9, "Ice Creams"),
    Menu("11", "Coffee Toffee Ice Cream           ", 10, "Ice Creams"),
    Menu("12", "Cookies & Cream Ice Cream         ", 10, "Ice Creams"),

    Menu("13", "Espresso                          ", 4, "Drinks"),
    Menu("14", "Cappuccino                        ", 5, "Drinks"),
    Menu("15", "Latte                             ", 6, "Drinks"),
    Menu("16", "Masala Chai                       ", 5, "Drinks"),
    Menu("17", "Vanilla Latte                     ", 8, "Drinks"),
    Menu("18", "Iced Mocha                        ", 10, "Drinks"),

    Menu("19", "Nutella Brownie + Vanilla Latte   ", 15, "Combos"),
    Menu("20", "Tiramisu Cake + Cappuccino        ", 29, "Combos"),
    Menu("21", "Pistachio Cake + Vanilla Latte    ", 36, "Combos"),
    Menu("22", "Chocolate Fudge Cake + Iced Mocha ", 20, "Combos"),
    Menu("23", "Cookies & Cream Cake + Latte      ", 20, "Combos"),



    Menu("24", "Monday : Nutella Brownie          ", 8, "Day"),
    Menu("25", "Tuesday : Red Velvet Cake         ", 25, "Day"),
    Menu("26", "Wednesday : Tiramisu Cake         ", 30, "Day"),
    Menu("27", "Thursday : Cookies & Cream Cake   ", 12, "Day"),
    Menu("28", "Friday : Chocolate Fudge Cake     ", 8, "Day"),
    Menu("29", "Saturday : Butterscotch Cake      ", 12, "Day"),
    Menu("30", "Sunday : Pistachio Cake           ", 25, "Day")
]


#added weather and mood questions to make the code more interactive
print("\nHow is the weather like in Berlin today?")
print("1. Sunny")
print("2. Cold")
print("3. Raining")
print("4. I don't know")

weather = input("Choose 1, 2, 3, or 4: ")
#Giving them recommendations based on the weather
if weather == "1":
    print("\n \n |||| WOWWWW!! SUN in Berlin... Lets get ice cream... ||||")
elif weather == "2":
    print("\n \n |||| Uhhhh:( usual a Berlin day Hot coffee will save us!!! ||||")
elif weather == "3":
    print("\n\n |||| Rainy days = cake + bed ||||")
else:
    print("\n\n |||| Okhhhh if we dont know, coffee is always the safest option ||||")



print("\nHow is ur mood today?")
print("1. Super happy")
print("2. Joyful")
print("3. Okay okay")
print("4. Tired")
print("5. Sad")
print("6. I dont know")


mood = input("Choose 1, 2, 3, 4, 5 or 6: ")

#This message will be shown with the bill in the end
if mood == "1":
    mood_msg = "You are absolutely glowing today... Keep spreading that energy!!!! "

elif mood == "2":
    mood_msg = "Looks like today treated you well:) We hope this was the cherry on top!! "

elif mood == "3":
    mood_msg = "Okay-okay days count too. U r doing GREAT!! "

elif mood == "4":
    mood_msg = "You made it through today. REST UP !!!"

elif mood == "5":
    mood_msg = "Some days are heavier than others.I hope this makes ur day Better. "

else:
    mood_msg = "Whatever your mood is, I hope something nice happens today. "


while True:
    print("\n~~ MAIN OPTIONS ~~")
    print("1. See MENU")
    print("2. View MY order")
    print("3. Lets PAY")
    print("4. EXIT")

    choice = input("Choose one option: ")

    if choice == "1":

        print("\n--- CAKES ---")
        for item in menu:
            if item.get_category() == "Cakes":
                item.show_item()

        print("\n--- ICE CREAMS ---")
        for item in menu:
            if item.get_category() == "Ice Creams":
                item.show_item()

        print("\n--- TEA COFFEE ---")
        for item in menu:
            if item.get_category() == "Drinks":
                item.show_item()

        print("\n--- COMBOS ---")
        for item in menu:
            if item.get_category() == "Combos":
                item.show_item()

        print("\n--- CAKE OF THE DAY ---")
        for item in menu:
            if item.get_category() == "Day":
                item.show_item()

        print("\nType Done when you are finished ordering.")

        while True:
            order_choice = input("\nWhat would you like to order? ")

            if order_choice.lower() == "done":
                break

            found = False

            for item in menu:
                if order_choice == item.item_id:
                    order.add_item(item)
                    found = True

            if found is False:
                print("Invalid choice, please try again.")


    elif choice == "2":
        order.view_order(customer)

    elif choice == "3":

        if order.empty():
            print("You didn't order anything yet.")
        else:
            order.show_bill(customer, mood_msg)
            payment.choose_payment()
            payment.show_payment()
            order.save_order(customer, payment)
            payment.thank_customer()

    elif choice == "4":
        print("Looking forward to your next visit.")
        break

    else:
        print("Invalid option, please choose again.")

