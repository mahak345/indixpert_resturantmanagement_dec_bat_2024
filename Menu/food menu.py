menu = [
    {"id": 1, "name": "Paneer Tikka", "half_price": 140, "full_price": 190, "category": "Lunch"},
    {"id": 2, "name": "Vegetable Biryani", "half_price": 140, "full_price": 225, "category": "Dinner"},
    {"id": 3, "name": "Masala Dosa", "half_price": 100, "full_price": 170, "category": "Lunch"},
    {"id": 4, "name": "Chole Bhature", "half_price": 120, "full_price": 190, "category": "Lunch"},
    {"id": 5, "name": "Aloo Paratha", "half_price": 90, "full_price": 150, "category": "Lunch"},
    {"id": 6, "name": "Veggie Burger", "half_price": 120, "full_price": 180, "category": "Lunch"},
    {"id": 7, "name": "Veg Hakka Noodles", "half_price": 130, "full_price": 180, "category": "Dinner"},
    {"id": 8, "name": "Palak Paneer", "half_price": 140, "full_price": 210, "category": "Dinner"},
    {"id": 9, "name": "Rajma Chawal", "half_price": 120, "full_price": 180, "category": "Lunch"},
    {"id": 10, "name": "Matar Paneer", "half_price": 140, "full_price": 210, "category": "Dinner"},
    {"id": 11, "name": "Veg Lasagna", "half_price": 150, "full_price": 250, "category": "Dinner"},
    {"id": 12, "name": "Stuffed Bell Peppers", "half_price": 140, "full_price": 220, "category": "Dinner"},
    {"id": 13, "name": "Kadai Mushroom", "half_price": 140, "full_price": 210, "category": "Lunch"},
    {"id": 14, "name": "Paneer Butter Masala", "half_price": 150, "full_price": 230, "category": "Dinner"},
    {"id": 15, "name": "Vegetable Kofta", "half_price": 150, "full_price": 220, "category": "Dinner"},
    {"id": 16, "name": "Baingan Bharta", "half_price": 120, "full_price": 190, "category": "Lunch"},
    {"id": 17, "name": "Potato Fry", "half_price": 130, "full_price": 210, "category": "Lunch"},
    {"id": 18, "name": "Veg Pulao", "half_price": 150, "full_price": 180, "category": "Dinner"},
    {"id": 19, "name": "Pav Bhaji", "half_price": 110, "full_price": 160, "category": "Lunch"},
    {"id": 20, "name": "Veg Spring Rolls", "half_price": 90, "full_price": 150, "category": "Dinner"},
]

def display_menu():
    print("\n" + "=" * 75)
    print("🌱 Welcome to the Vegetarian Menu 🌱".center(75))
    print("=" * 75)
    print(f"{'ID':<4}{'Dish Name':<30}{'Half Plate (₹)':>15}{'Full Plate (₹)':>15}{'Category':>10}")
    print("-" * 75)
    for item in menu:
        print(f"{item['id']:<4}{item['name']:<30}₹{item['half_price']:>13.2f}₹{item['full_price']:>13.2f}{item['category']:>10}")
    print("=" * 75)

def add_item():
    print("\n Add a New Dish")
    name = input("Enter dish name: ").strip().title()
    try:
        half_price = float(input("Enter half plate price (₹): "))
        full_price = float(input("Enter full plate price (₹): "))
        if half_price <= 0 or full_price <= 0:
            print("Prices must be positive numbers.")
            return
    except ValueError:
        print(" Invalid price input.")
        return

    category = input("Enter category (Lunch/Dinner): ").strip().capitalize()
    if category not in ["Lunch", "Dinner"]:
        print(" Invalid category.")
        return

    new_id = max(item['id'] for item in menu) + 1
    menu.append({
        "id": new_id,
        "name": name,
        "half_price": half_price,
        "full_price": full_price,
        "category": category
    })
    print(f" '{name}' has been added to the {category} menu.")

def update_item():
    try:
        item_id = int(input("Enter the ID of the dish to update: "))
    except ValueError:
        print(" Invalid ID.")
        return

    for item in menu:
        if item["id"] == item_id:
            print(f"Editing Dish: {item['name']}")
            item["name"] = input("Enter new dish name: ").strip().title()
            try:
                item["half_price"] = float(input("Enter new half plate price (₹): "))
                item["full_price"] = float(input("Enter new full plate price (₹): "))
            except ValueError:
                print(" Invalid price input.")
                return
            item["category"] = input("Enter new category (Lunch/Dinner): ").strip().capitalize()
            print(" Dish updated successfully!")
            return
    print(" Dish not found.")

def delete_item():
    try:
        item_id = int(input("Enter the ID of the dish to delete: "))
    except ValueError:
        print(" Invalid ID.")
        return

    for item in menu:
        if item["id"] == item_id:
            menu.remove(item)
            print(f"{item['name']}' has been deleted.")
            return
    print(" Dish not found.")

def main():
    while True:
        print("\n Menu Options")
        print("1. Display Menu")
        print("2. Add Dish")
        print("3. Update Dish")
        print("4. Delete Dish")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            display_menu()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print(" Thank you! Exiting...")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")

if __name__ == "__main__":
    main()
