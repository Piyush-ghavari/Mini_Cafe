import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="caffee"
        )
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to the database: {err}")
        return None

connection = connect_db()
if connection:
    mycursor = connection.cursor()

# Global variables
menu_price = {
    1: ('Maggie', 50),
    2: ('Sandwich', 70),
    3: ('Pasta', 90),
    4: ('Pizza', 120),
    5: ('Paneer Tacos', 140)
}
total_bill = 0
order_details = []  # Stores item details for the current order

def menu_item_selected(item_number, qty):
    global total_bill
    if item_number in menu_price and qty > 0:
        item_name, item_price = menu_price[item_number]
        item_total = item_price * qty
        total_bill += item_total
        order_details.append((item_name, qty, item_total))
        update_order_display()

        # Ask if the user wants to continue ordering
        continue_order = messagebox.askquestion("Continue Order", "Do you want to continue ordering?")
        if continue_order == 'no':
            # If 'No', simply return and let them place the order
            return

def update_order_display():
    order_display.delete('1.0', tk.END)
    order_display.insert(tk.END, "Order Details:\n")
    for item_name, qty, item_total in order_details:
        order_display.insert(tk.END, f"{item_name} x {qty} = {item_total} Rs\n")
    order_display.insert(tk.END, f"\nTotal Bill: {total_bill} Rs")

def place_order():
    if not order_details:
        messagebox.showerror("Error", "No items in the order!")
        return

    Your_name = name_entry.get().strip()
    your_age = age_entry.get().strip()

    if not Your_name or not your_age.isdigit():
        messagebox.showerror("Error", "Please enter valid Name and Age!")
        return

    # Insert each item into the database
    for item_name, qty, item_total in order_details:
        mycursor.execute(
            "INSERT INTO o_details (Name, Age, food, Quantity, Bill) VALUES (%s, %s, %s, %s, %s);",
            (Your_name, int(your_age), item_name, qty, item_total)
        )
    connection.commit()

    # Show thank you message
    messagebox.showinfo("Order Placed", f"Thank you, {Your_name}, for your order!\nTotal Bill: {total_bill} Rs")
    reset_order()

def reset_order():
    global total_bill, order_details
    total_bill = 0
    order_details = []
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    update_order_display()

def exit_app():
    if connection:
        connection.close()
    root.destroy()

# Tkinter GUI
root = tk.Tk()
root.title("Piyush Cafe Order System")
root.geometry("1920x1080")
root.configure(bg="#ffe4b5")

# Header
header_label = tk.Label(root, text="Welcome to Piyush Cafe", font=("Arial", 24, "bold"), bg="#8b4513", fg="white")
header_label.pack(fill=tk.X, pady=10)

# Name and Age Entry
details_frame = tk.Frame(root, bg="#ffe4b5")
details_frame.pack(pady=20)

name_label = tk.Label(details_frame, text="Name:", font=("Arial", 16), bg="#ffe4b5")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(details_frame, font=("Arial", 16))
name_entry.grid(row=0, column=1, padx=10, pady=10)

age_label = tk.Label(details_frame, text="Age:", font=("Arial", 16), bg="#ffe4b5")
age_label.grid(row=0, column=2, padx=10, pady=10)
age_entry = tk.Entry(details_frame, font=("Arial", 16))
age_entry.grid(row=0, column=3, padx=10, pady=10)

# Menu Section
menu_frame = tk.Frame(root, bg="#ffe4b5")
menu_frame.pack(pady=20)

menu_title = tk.Label(menu_frame, text="Menu", font=("Arial", 20, "bold"), bg="#ffe4b5")
menu_title.grid(row=0, column=0, columnspan=4, pady=10)

for idx, (item_number, (item_name, item_price)) in enumerate(menu_price.items(), start=1):
    item_label = tk.Label(menu_frame, text=f"{item_name} - {item_price} Rs", font=("Arial", 14), bg="#ffe4b5")
    item_label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")
    qty_spinbox = tk.Spinbox(menu_frame, from_=1, to=10, font=("Arial", 14), width=5)
    qty_spinbox.grid(row=idx, column=1, padx=10, pady=5)
    add_button = tk.Button(
        menu_frame,
        text="Add",
        font=("Arial", 14),
        bg="#8b4513",
        fg="white",
        command=lambda item_number=item_number, qty_spinbox=qty_spinbox: menu_item_selected(item_number, int(qty_spinbox.get()))
    )
    add_button.grid(row=idx, column=2, padx=10, pady=5)

# Order Details Section
order_frame = tk.Frame(root, bg="#ffe4b5")
order_frame.pack(side=tk.RIGHT, padx=20, pady=20)

order_label = tk.Label(order_frame, text="Order Details", font=("Arial", 18, "bold"), bg="#8b4513", fg="white")
order_label.pack(fill=tk.X, pady=5)
order_display = tk.Text(order_frame, height=20, width=40, font=("Arial", 14), bg="#ffe4b5", state="normal")
order_display.pack()

# Action Buttons
action_frame = tk.Frame(root, bg="#ffe4b5")
action_frame.pack(pady=20)

place_order_button = tk.Button(action_frame, text="Place Order", font=("Arial", 16), bg="#32cd32", fg="white", command=place_order)
place_order_button.grid(row=0, column=0, padx=20, pady=10)

exit_button = tk.Button(action_frame, text="Exit", font=("Arial", 16), bg="#ff4500", fg="white", command=exit_app)
exit_button.grid(row=0, column=1, padx=20, pady=10)

# Run Tkinter main loop
root.mainloop()
