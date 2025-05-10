menu = {
    "pizza": 450,
    "coffee": 250,
    "burger": 300,
    "momo's": 160,
    "cold drinks": 80,
    "tea": 30        
}

# greetings
print("Welcome To Sano Restaurant!!!")
print("Menu:")
for item, price in menu.items():
    print(f"{item.title()} : Rs.{price}")

order_total = 0

# First item order
item_1 = input("Enter an item that you would like to order: ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Sorry, the item '{item_1}' is not available.")

# Asking for second order
another_order = input("Would you like to order anything else? (yes/no): ").lower()
if another_order == "yes":
    item_2 = input("Enter the item that you would like to order: ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' has been added to your order.")
    else:
        print(f"Sorry, the item '{item_2}' is not available.")

print(f"Your total amount to pay is Rs.{order_total}")
