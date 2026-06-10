from customer import Customer
from menu import Menu
from order import Order
from payment import Payment


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("------ WELCOME TO JANNU's Sweet Bakeryyyyy ------")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\nNow we'll ask u few questionsssss......")


name = input("\nWhat is ur NAME? ")


while True:
    try:
        age = int(input("\nWhat is ur AGE? "))
        break
    except ValueError:
        print("Please enter ur age as a number.")


print("\nChoose ur gender:")
print("1. Male")
print("2. Femalee")
print("3. Prefer not to say")

gender_choice = input("Enter 1, 2, 3- ")

if gender_choice == "1":
    gender = "Male"
elif gender_choice == "2":
    gender = "Female"
else:
    gender = "Prefer not to say"


customer = Customer(name, age, gender)
order = Order()
payment = Payment()

menu = [
    Menu("1", "Red Velvet ChesseCake ", 60, "Dessert"),
    Menu("2", "Glazed Donut          ", 4.99, "Dessert"),
    Menu("3", "Fresh Mango Ice-Cream ", 30, "Dessert"),
    Menu("4", "Oreo Cupcake          ", 7, "Dessert"),
    Menu("5", "Nutella Brownie       ", 5.99, "Dessert"),
    Menu("6", "Coffee                ", 15, "Drink"),
    Menu("7", "Tea                   ", 13, "Drink"),
    Menu("8", "Cookie & Cream        ", 9.99, "Dessert")
]


while True:
    print("\n~~ MAIN OPTIONS ~~")
    print("1. See MENU")
    print("2. View MY orders")
    print("3. Show SUM Total")
    print("4. EXIT")

    choice = input("Choose one option: ")

    if choice == "1":
        while True:
        
            print("\n~~~ MENU ~~~")

            for item in menu:
                item.show_item()

            
            print("\nType Done when you are finish ordering....")
            

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
        order.show_bill(customer)
        payment.choose_payment()
        payment.show_payment()
        order.save_order(customer, payment)
        payment.thank_customer()

    elif choice == "4":
        payment.thank_customer()
        break

    else:
        print("Invalid option, please choose again.")