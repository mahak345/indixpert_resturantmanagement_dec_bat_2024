class MenuItem:
    def __init__(self, id, name, half_price, full_price, category):
        self.id = id
        self.name = name
        self.half_price = half_price
        self.full_price = full_price
        self.category = category

    def __str__(self):
        return f"{self.id}. {self.name} ({self.category}) - Half: ₹{self.half_price}, Full: ₹{self.full_price}"


class Menu:
    def __init__(self):
        self.items = {}

    def load_items(self, items_list):
        for item in items_list:
            self.items[item['id']] = MenuItem(**item)

    def show_menu(self):
        print("\n--- Menu ---")
        for item in self.items.values():
            print(item)
        print("------------")

    def get_item(self, item_id):
        return self.items.get(item_id, None)

class Order:
    def __init__(self, menu):
        self.menu = menu
        self.ordered_items = []

    def add_to_order(self, item_id, portion, quantity):
        item = self.menu.get_item(item_id)
        if not item:
            print(f" Item ID {item_id} not found.")
            return
        price = item.half_price if portion == "half" else item.full_price
        self.ordered_items.append((item, portion, quantity, price))

    def print_bill(self):
        print("\n======== Bill Summary ========")
        total = 0
        print("{:<25} {:<10} {:<10} {:<10}".format("Item", "Portion", "Qty", "Total"))
        print("-" * 55)
        for item, portion, qty, price in self.ordered_items:
            line_total = qty * price
            print("{:<25} {:<10} {:<10} ₹{:<10}".format(item.name, portion.capitalize(), qty, line_total))
            total += line_total
        print("-" * 55)
        print(f"{'Grand Total':<47} ₹{total}")
        print("========================")
menu_items = [
    {"id": 1, "name": "Paneer Tikka", "half_price": 140, "full_price": 190, "category": "Lunch"},
    {"id": 2, "name": "Vegetable Biryani", "half_price": 140, "full_price": 225, "category": "Dinner"},
    {"id": 3, "name": "Masala Dosa", "half_price": 100, "full_price": 170, "category": "Lunch"},
    {"id": 4, "name": "Chole Bhature", "half_price": 80, "full_price": 150, "category": "Lunch"},
    {"id": 5, "name": "Paneer Butter Masala", "half_price": 140, "full_price": 200, "category": "Lunch"},
    {"id": 6, "name": "Egg Curry", "half_price": 120, "full_price": 180, "category": "Dinner"},
    {"id": 8, "name": "Dal Makhani", "half_price": 100, "full_price": 160, "category": "Lunch"},
    {"id": 9, "name": "Hyderabadi Biryani", "half_price": 160, "full_price": 250, "category": "Dinner"},
    {"id": 10, "name": "Chana Masala", "half_price": 90, "full_price": 140, "category": "Lunch"},
    {"id": 11, "name": "Tandoori Chicken", "half_price": 160, "full_price": 260, "category": "Dinner"},
    {"id": 12, "name": "Rajma Chawal", "half_price": 80, "full_price": 140, "category": "Lunch"},
    {"id": 13, "name": "Veg Kofta", "half_price": 110, "full_price": 170, "category": "Lunch"},
    {"id": 14, "name": "Aloo Gobi", "half_price": 70, "full_price": 120, "category": "Lunch"},
    {"id": 15, "name": "Palak Paneer", "half_price": 140, "full_price": 210, "category": "Lunch"},
    {"id": 16, "name": "Fish Fry", "half_price": 180, "full_price": 290, "category": "Dinner"},
    {"id": 17, "name": "Kadai Chicken", "half_price": 170, "full_price": 260, "category": "Dinner"},
    {"id": 18, "name": "Tandoori Roti", "half_price": 30, "full_price": 60, "category": "Both"},
    {"id": 19, "name": "Plain Rice", "half_price": 40, "full_price": 70, "category": "Both"},
    {"id": 20, "name": "Jeera Rice", "half_price": 50, "full_price": 80, "category": "Both"},
    {"id": 21, "name": "Butter Naan", "half_price": 40, "full_price": 80, "category": "Both"},
    {"id": 22, "name": "Stuffed Paratha", "half_price": 90, "full_price": 130, "category": "Breakfast"},
    {"id": 23, "name": "Idli Sambhar", "half_price": 60, "full_price": 100, "category": "Breakfast"},
    {"id": 24, "name": "Masala Uttapam", "half_price": 80, "full_price": 150, "category": "Breakfast"},
    {"id": 100, "name": "Water Bottle", "half_price": 0, "full_price": 20, "category": "Beverage"},
]
if __name__ == "__main__":
    menu = Menu()
    menu.load_items(menu_items)
    menu.show_menu()

    order = Order(menu)

    print("\nEnter your order (type 'done' at any time to finish):")
    while True:
        user_input = input("Enter item ID (or 'done'): ").strip()
        if user_input.lower() == "done":
            if len(order.ordered_items) < 3:
                print("Please order at least 3 different items before generating the bill.")
                continue
            break

        if not user_input.isdigit():
            print("Invalid input. Item ID must be a number.")
            continue

        item_id = int(user_input)
        item = menu.get_item(item_id)
        if not item:
            print(f"Item ID {item_id} not found.  Please choose from the menu:")
            menu.show_menu()
            continue

        portion = input("Enter portion (half/full): ").strip().lower()
        if portion not in ["half", "full"]:
            print("Invalid portion. Please enter 'half' or 'full'.")
            continue

        qty_input = input("Enter quantity: ").strip()
        if not qty_input.isdigit():
            print("Quantity must be a number.")
            continue

        quantity = int(qty_input)
        order.add_to_order(item_id, portion, quantity)

    if order.ordered_items:
        order.print_bill()
    else:
        print(" No items were ordered.")
