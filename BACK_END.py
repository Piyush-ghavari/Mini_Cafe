import mysql.connector

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="caffee"
)
print(connection)
mycursor = connection.cursor()

def menu():
    print("-- Welcome to Piyush Cafe --")
    print("MENU")
    print("1. Maggie = 50 Rs")
    print("2. Sandwich = 70 Rs")
    print("3. Pasta = 90 Rs")
    print("4. Pizza = 120 Rs")
    print("5. Paneer Tacos = 140 Rs")
    print("6. Exit")
    print()

def Take_order():
    # Menu prices remain unchanged
    menu_price = {
        1: ('Maggie', 50),
        2: ('Sandwich', 70),
        3: ('Pasta', 90),
        4: ('Pizza', 120),
        5: ('Paneer Tacos', 140)
    }

    # Collect customer details once
    Your_name = input("Enter your name: ").strip()
    your_age = int(input("Enter your age: ").strip())

    total_bill = 0  # Total bill for the customer
    while True:
        menu()
        
        # Ask for item selection
        n = int(input("Enter item number to order: "))
        if n in menu_price:
            item_name, item_price = menu_price[n]
            qty = int(input(f"Enter quantity for {item_name}: "))
            item_total = item_price * qty
            total_bill += item_total

            # Display current item details
            print(f"\nItem added: {item_name}")
            print(f"Quantity: {qty}")
            print(f"Subtotal for {item_name}: {item_total} Rs")
            print(f"Current total bill: {total_bill} Rs")

            # Save item to database
            mycursor.execute(
                "INSERT INTO o_details (Name, Age, food, Quantity, Bill) VALUES (%s, %s, %s, %s, %s);",
                (Your_name, your_age, item_name, qty, item_total)
            )

            # Ask if the user wants to continue
            a = input("Do you want to order another item? (yes/no): ").lower()
            if a == 'no':
                print("\n-- Final Bill Summary --")
                print(f"Total Bill for {Your_name}: {total_bill} Rs")
                connection.commit()  # Commit all orders to the database
                print("Thank you for your order!")
                break
            elif a != 'yes':
                print("Invalid input. Exiting order process.")
                break
        elif n == 6:  # Exit optionh
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please select a valid menu item.")

# Call the order function
Take_order()
