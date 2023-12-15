import tkinter as tk
from tkinter import messagebox

class FoodOrderSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Order System")
        self.menu = {"Pizza": {"price": 670.00, "logo": "🍕"},
                     "Hamburger": {"price": 120.00, "logo": "🍔"},
                     "Ice Cream": {"price": 40.50, "logo": "🍦"},
                     "Empanada": {"price": 30.00, "logo": "🥟"},
                     "French-Fries": {"price": 95.00, "logo": "🍟"},
                     "Donut": {"price": 15.00, "logo": "🍩"},
                     "Drinks": {"price": 70.25, "logo": "🥤"}}
        self.order_items = []
        self.total = 0

        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg="black")  # Set background color to black

        # Entry with placeholder for name
        self.name_entry = tk.Entry(self.root, width=30, font=("Berlin Sans FB Demi", 12), foreground='grey')
        self.name_entry.insert(0, "Enter your name here")
        self.setup_placeholder(self.name_entry, "Enter your name here")
        self.name_entry.pack(pady=10)

        # Entry with placeholder for tip
        self.tip_entry = tk.Entry(self.root, width=30, font=("Berlin Sans FB Demi", 12), foreground='grey')
        self.tip_entry.insert(0, "Enter tip amount (optional)")
        self.setup_placeholder(self.tip_entry, "Enter tip amount (optional)")
        self.tip_entry.pack(pady=10)

        # Entry with placeholder
        self.order_button = tk.Button(self.root, text="Order", command=self.order, bg="teal", fg="white", font=("Century Gothic", 14), borderwidth=3, relief="ridge", cursor="hand2")
        self.order_button.pack(pady=10)

        self.display_button = tk.Button(self.root, text="Display Order", command=self.display_order, bg="tan", fg="white", font=("Century Gothic", 14), borderwidth=3, relief="ridge", cursor="hand2")
        self.display_button.pack(pady=10)

        self.state_var = tk.StringVar()
        self.state_var.set("Select State")

        self.state_menu = tk.OptionMenu(self.root, self.state_var, "Baao", "Nabua", "Iriga", "Bula", "Buhi", "Bato")
        self.state_menu.config(width=12, font=("Century Gothic", 12), bg="green", fg="white", cursor="hand2")
        self.state_menu.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_app, bg="red", fg="white", font=("Century Gothic", 14), borderwidth=3, relief="ridge", cursor="hand2")
        self.quit_button.pack(pady=10)

              # Display order details
        self.order_details_label = tk.Label(self.root, text="", font=("Courier New", 14), bg="black", fg="white")
        self.order_details_label.pack()


    def order(self):
        order_label = tk.Label(self.root, text="What would you like to order?", font=("Century Gothic", 14), bg="black", fg="pink")
        order_label.pack(pady=10)

        for item, details in self.menu.items():
            button = tk.Button(self.root,
                               text=f"{details['logo']} {item}: ₱{details['price']:.2f}",
                               command=lambda i=item, p=details['price']: self.add_to_order(i, p),
                               bg="orange", fg="black", font=("Century Gothic", 12),
                               borderwidth=3, relief="ridge", cursor="hand2")
            button.pack(pady=5)
    def display_order(self):
        name = self.name_entry.get()
        if name:
            # Update order details label in the main window
            order_details = f"{name}, your order details:\n"
            for item in self.order_items:
                order_details += f"{item}: ₱{self.menu[item]['price']:.2f}\n"
            order_details += f"Total amount: ₱{self.total:.2f}"

            self.order_details_label.config(text=order_details)
        else:
            # Show a warning if the user's name is not entered
            messagebox.showwarning("Warning", "Please enter your name before displaying the order.")
        tip = self.tip_entry.get()
        state = self.state_var.get()

        if not tip or not tip.replace('.', '').isdigit():
            tip = 0
        else:
            tip = float(tip)

        if state == "Select State":
            messagebox.showwarning("Warning", "Please select a state before placing an order.")
            return

        total_with_tip = self.total + tip

        order_details += f"\nTip: ₱{tip:.2f}"
        order_details += f"\nState: {state}"
        order_details += f"\nTotal amount with tip: ₱{total_with_tip:.2f}"

        self.order_details_label.config(text=order_details)


        order_details += f"\nTip: ₱{tip:.2f}"
        order_details += f"\nState: {state}"
        order_details += f"\nTotal amount with tip: ₱{total_with_tip:.2f}"

    def add_to_order(self, item, price):
        self.total += price
        self.order_items.append(item)
        messagebox.showinfo("Order Placed", f"{item} added to your order!")

    def quit_app(self):
        # Show a thank you message and close the application
        messagebox.showinfo("Thank You", "Thank you, come back again!")
        self.root.destroy()

    def on_enter(self, event, widget):
        widget.config(bg="dark green")

    def on_leave(self, event, widget):
        widget.config(bg="dark green")

    def setup_placeholder(self, entry, placeholder_text):
        entry.bind("<FocusIn>", lambda event, entry=entry, placeholder_text=placeholder_text: self.clear_placeholder(event, entry, placeholder_text))
        entry.bind("<FocusOut>", lambda event, entry=entry, placeholder_text=placeholder_text: self.restore_placeholder(event, entry, placeholder_text))

    def clear_placeholder(self, event, entry, placeholder_text):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.config(foreground='black')

    def restore_placeholder(self, event, entry, placeholder_text):
        if not entry.get():
            entry.insert(0, placeholder_text)
            entry.config(foreground='grey')

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodOrderSystem(root)
    root.mainloop()