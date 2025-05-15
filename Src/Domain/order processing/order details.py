import json

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
        print("\n------ MENU ------")
        for item in self.items.values():
            print(item)
        print("------------------")

    def get_item(self, item_id):
        return self.items.get(item_id)


class Order:
    def __init__(self, menu):
        self.menu = menu
        self.ordered_items = []

    def add_to_order(self, item_id, portion, quantity):
        item = self.menu.get_item(item_id)
        if not item:
            print(" Invalid item ID.")
            return
        price = item.half_price if portion == "half" else item.full_price
        self.ordered_items.append((item, portion, quantity, price))
        print(f" Added: {quantity} x {item.name} ({portion})")

    def print_bill(self):
        if not self.ordered_items:
            print(" No items in order.")
            return
        print("\n======= BILL =======")
        total = 0
        print("{:<25} {:<10} {:<5} {:<10}".format("Item", "Portion", "Qty", "Total"))
        print("-" * 55)
        for item, portion, qty, price in self.ordered_items:
            line_total = qty * price
            print("{:<25} {:<10} {:<5} ₹{:<10}".format(item.name, portion.capitalize(), qty, line_total))
            total += line_total
        print("-" * 55)
        print(f"{'Grand Total':<42} ₹{total}")
        print("=====================")


def load_menu_items_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Menu file not found!")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON data!")
        return []


if __name__ == "__main__":
    menu_items_file = 'menu_items.json'
    menu_items_data = load_menu_items_from_file(menu_items_file)
    
    if not menu_items_data:
        print("No menu items loaded. Exiting program.")
    else:
        menu = Menu()
        menu.load_items(menu_items_data)
        order = Order(menu)

        print(" Welcome to the Restaurant!")
        menu.show_menu()

        while True:
            user_input = input("\nEnter item ID to order (or 'done' to finish): ").strip()
            if user_input.lower() == "done":
                break
            if not user_input.isdigit():
                print(" Please enter a valid number.")
                continue
            item_id = int(user_input)
            item = menu.get_item(item_id)
            if not item:
                print(" Item not found.")
                continue

            portion = input("Portion (half/full): ").strip().lower()
            if portion not in ["half", "full"]:
                print(" Portion must be 'half' or 'full'.")
                continue

            quantity = input("Quantity: ").strip()
            if not quantity.isdigit() or int(quantity) <= 0:
                print(" Please enter a valid quantity.")
                continue

            order.add_to_order(item_id, portion, int(quantity))

        order.print_bill()
