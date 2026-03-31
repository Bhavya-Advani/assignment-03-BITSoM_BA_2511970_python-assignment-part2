## Part 1: Menu exploration
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

print("\nTask 1 — Explore the Menu")

categories = sorted({data['category'] for data in menu.values()})
for cat in categories:
    print(f"===== {cat} =====")
    for item, data in menu.items():
        if data['category'] == cat:
            avail = "[Available]" if data['available'] else "[Unavailable]"
            print(f"{item:<15} ₹{data['price']:6.2f}   {avail}")
    print()

total_items = len(menu)
available_items = sum(1 for data in menu.values() if data['available'])
most_expensive = max(menu.items(), key=lambda kv: kv[1]['price'])
under_150 = [(item, data['price']) for item, data in menu.items() if data['price'] < 150]

print(f"Total menu items: {total_items}")
print(f"Total available items: {available_items}")
print(f"Most expensive item: {most_expensive[0]} (₹{most_expensive[1]['price']:.2f})")
print("Items under ₹150:")
for item, price in under_150:
    print(f"- {item} (₹{price:.2f})")


cart = []

def add_to_cart(item, quantity):
    if item not in menu:
        print(f"Error: '{item}' does not exist in the menu.")
        return
    if not menu[item]['available']:
        print(f"Error: '{item}' is currently unavailable.")
        return
    for entry in cart:
        if entry['item'] == item:
            entry['quantity'] += quantity
            print(f"Updated {item} quantity to {entry['quantity']}.")
            return
    cart.append({"item": item, "quantity": quantity, "price": menu[item]['price']})
    print(f"Added {item} x{quantity} to cart.")

def remove_from_cart(item):
    for i, entry in enumerate(cart):
        if entry['item'] == item:
            cart.pop(i)
            print(f"Removed {item} from cart.")
            return
    print(f"Error: '{item}' is not in the cart.")

def update_quantity(item, new_quantity):
    for entry in cart:
        if entry['item'] == item:
            entry['quantity'] = new_quantity
            print(f"Updated {item} quantity to {new_quantity}.")
            return
    print(f"Error: '{item}' is not in the cart.")

def print_cart():
    if not cart:
        print("Cart is empty.")
    else:
        print("Current cart:")
        for entry in cart:
            print(f"- {entry['item']} x{entry['quantity']} @ ₹{entry['price']:.2f}")
    print()

# Part 2: Cart Operations
print("\nSimulate Customer Order")
print("Step 1: Add Paneer Tikka x2")
add_to_cart("Paneer Tikka", 2)
print_cart()

print("Step 2: Add Gulab Jamun x1")
add_to_cart("Gulab Jamun", 1)
print_cart()

print("Step 3: Add Paneer Tikka x1 (should update to 3)")
add_to_cart("Paneer Tikka", 1)
print_cart()

print("Step 4: Try to add Mystery Burger")
add_to_cart("Mystery Burger", 1)
print_cart()

print("Step 5: Try to add Chicken Wings")
add_to_cart("Chicken Wings", 1)
print_cart()

print("Step 6: Remove Gulab Jamun")
remove_from_cart("Gulab Jamun")
print_cart()

# Order Summary
print("========== Order Summary ==========")
subtotal = 0
for entry in cart:
    item_total = entry['quantity'] * entry['price']
    subtotal += item_total
    print(f"{entry['item']:<15} x{entry['quantity']:<2} ₹{item_total:6.2f}")

gst = subtotal * 0.05
total = subtotal + gst

print("------------------------------------")
print(f"Subtotal:              ₹{subtotal:6.2f}")
print(f"GST (5%):             ₹{gst:6.2f}")
print(f"Total Payable:        ₹{total:6.2f}")
print("====================================")

## Inventory Tracker with Deep Copy
import copy

inventory_backup = copy.deepcopy(inventory)

# Manually change one stock value
inventory["Paneer Tikka"]["stock"] = 5
print("\nAfter manual change:")
print("Inventory:", inventory["Paneer Tikka"])
print("Inventory Backup:", inventory_backup["Paneer Tikka"])

# Restore inventory
inventory = copy.deepcopy(inventory_backup)
print("\nRestored inventory to original.")

# Simulate order fulfillment from cart
print("\nSimulating order fulfillment:")
for entry in cart:
    item = entry["item"]
    qty = entry["quantity"]
    if item in inventory:
        available = inventory[item]["stock"]
        if qty > available:
            print(f"Warning: Insufficient stock for {item}. Deducting only {available} instead of {qty}.")
            inventory[item]["stock"] = 0
        else:
            inventory[item]["stock"] -= qty
            print(f"Deducted {qty} from {item}. Remaining stock: {inventory[item]['stock']}")
    else:
        print(f"Error: {item} not in inventory.")

# Reorder alerts
print("\nReorder Alerts:")
for item, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print(f"⚠ Reorder Alert: {item} — Only {data['stock']} unit(s) left (reorder level: {data['reorder_level']})")

# Print both at the end
print("\nFinal Inventory:")
for item, data in inventory.items():
    print(f"{item}: {data}")

print("\nInventory Backup (unchanged):")
for item, data in inventory_backup.items():
    print(f"{item}: {data}")


## Daily Sales Log Analysis
    
sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# Task 8 — Daily Sales Log Analysis
print("\nTask 8 — Daily Sales Log Analysis")

# Total revenue per day
revenue_per_day = {}
for date, orders in sales_log.items():
    revenue_per_day[date] = sum(order['total'] for order in orders)

print("Total revenue per day:")
for date, rev in revenue_per_day.items():
    print(f"{date}: ₹{rev:.2f}")

# Best-selling day
best_day = max(revenue_per_day, key=revenue_per_day.get)
print(f"\nBest-selling day: {best_day} (₹{revenue_per_day[best_day]:.2f})")

# Most ordered item
item_counts = {}
for orders in sales_log.values():
    for order in orders:
        for item in order['items']:
            item_counts[item] = item_counts.get(item, 0) + 1

most_ordered = max(item_counts, key=item_counts.get)
print(f"\nMost ordered item: {most_ordered} (appears in {item_counts[most_ordered]} orders)")

# Add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

# Reprint revenue per day and best-selling
revenue_per_day = {}
for date, orders in sales_log.items():
    revenue_per_day[date] = sum(order['total'] for order in orders)

print("\nUpdated total revenue per day:")
for date, rev in revenue_per_day.items():
    print(f"{date}: ₹{rev:.2f}")

best_day = max(revenue_per_day, key=revenue_per_day.get)
print(f"\nUpdated best-selling day: {best_day} (₹{revenue_per_day[best_day]:.2f})")

# Numbered list of all orders
print("\nAll orders:")
order_num = 1
for date in sorted(sales_log.keys()):
    for order in sales_log[date]:
        items_str = ", ".join(order['items'])
        print(f"{order_num}. [{date}] Order #{order['order_id']} — ₹{order['total']:.2f} — Items: {items_str}")
        order_num += 1

