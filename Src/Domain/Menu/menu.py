
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
    {"id": 24, "name": "Masala Uttapam", "half_price": 90, "full_price": 150, "category": "Breakfast"},
]

fixed_item = {
    "id": 100,
    "name": "Water Bottle",
    "half_price": 10,
    "full_price": 20,
    "category": "Both"
}
class Menu:
    def __init__(self):
        self.items = {}

menu = Menu()
def show_menu():
    print("\n====== MENU ======")
    print("{:<5} {:<20} {:<12} {:<10} {:<10}".format("ID", "Dish Name", "Category", "Half", "Full"))
    print("-" * 60)
    for item in menu_items:
        print("{:<5} {:<20} {:<12} ₹{:<9} ₹{:<9}".format(
            item["id"], item["name"], item["category"], item["half_price"], item["full_price"]))

    print("{:<5} {:<20} {:<12} ₹{:<9} ₹{:<9}".format(
        fixed_item["id"], fixed_item["name"], fixed_item["category"], fixed_item["half_price"], fixed_item["full_price"]))

    print(f"\nTotal Dishes: {len(menu_items) + 1}\n")
def add_dish():
    try:
        name = input("Enter new dish name: ").strip()
        if not name:
            print("Dish name cannot be empty.")
            return
        
        for dish in menu_items:
            if dish["name"].lower() == name.lower():
                print("Dish already exists.")
                return
        
        category = input("Dish category (Breakfast/Lunch/Dinner/Both): ").capitalize().strip()
        half_price = float(input("Enter half plate price: ₹").strip())
        full_price = float(input("Enter full plate price: ₹").strip())
        new_id = max(d["id"] for d in menu_items) + 1

        new_dish = {
            "id": new_id,
            "name": name,
            "half_price": half_price,
            "full_price": full_price,
            "category": category
        }

        menu_items.append(new_dish)
        print(f"{name} added successfully.")
    except ValueError:
        print("Invalid price input. Please enter numeric values.")
def update_dish():
    try:
        dish_id = int(input("Enter the dish ID to update: ").strip())
        dish = next((item for item in menu_items if item["id"] == dish_id), None)
        
        if not dish:
            print("Dish not found.")
            return
        
        name = input(f"New name for '{dish['name']}' (leave blank to keep same): ").strip()
        if name:
            dish["name"] = name
        
        category = input("New category (leave blank to keep same): ").strip()
        if category:
            dish["category"] = category.capitalize()
        
        half_price = input("New half plate price (leave blank to keep same): ").strip()
        if half_price:
            dish["half_price"] = float(half_price)
        
        full_price = input("New full plate price (leave blank to keep same): ").strip()
        if full_price:
            dish["full_price"] = float(full_price)

        print("Dish updated successfully.")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
def delete_dish():
    try:
        dish_id = int(input("Enter the dish ID to delete: ").strip())
        dish = next((item for item in menu_items if item["id"] == dish_id), None)
        
        if not dish:
            print("Dish not found.")
            return
        
        menu_items.remove(dish)
        print(f"{dish['name']} deleted successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid dish ID.")
def admin_menu():
    while True:
        print("\n1. Show Menu")
        print("2. Add Dish")
        print("3. Update Dish")
        print("4. Delete Dish")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_dish()
        elif choice == "3":
            update_dish()
        elif choice == "4":
            delete_dish()
        elif choice == "5":
            print("Exiting menu management.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    admin_menu()
