import json
menu = [
    {"id": 1, "name": "Paneer Tikka", "category": "Lunch", "portions": {"half": {"price": 140}, "full": {"price": 190}}},
    {"id": 2, "name": "Vegetable Biryani", "category": "Dinner", "portions": {"half": {"price": 140}, "full": {"price": 225}}},
    {"id": 3, "name": "Masala Dosa", "category": "Lunch", "portions": {"half": {"price": 100}, "full": {"price": 170}}},
    {"id": 4, "name": "Dal Makhani", "category": "Dinner", "portions": {"half": {"price": 120}, "full": {"price": 200}}},
    {"id": 5, "name": "Chole Bhature", "category": "Lunch", "portions": {"half": {"price": 110}, "full": {"price": 180}}},
    {"id": 6, "name": "Veg Pulao", "category": "Dinner", "portions": {"half": {"price": 130}, "full": {"price": 210}}},
    {"id": 7, "name": "Aloo Paratha", "category": "Lunch", "portions": {"half": {"price": 90}, "full": {"price": 150}}},
    {"id": 8, "name": "Paneer Butter Masala", "category": "Dinner", "portions": {"half": {"price": 160}, "full": {"price": 250}}},
    {"id": 9, "name": "Veg Manchurian", "category": "Lunch", "portions": {"half": {"price": 120}, "full": {"price": 190}}},
    {"id": 10, "name": "Rajma Chawal", "category": "Dinner", "portions": {"half": {"price": 130}, "full": {"price": 220}}},
    {"id": 11, "name": "Samosa", "category": "Lunch", "portions": {"half": {"price": 60}, "full": {"price": 100}}},
    {"id": 12, "name": "Kadhi Pakora", "category": "Dinner", "portions": {"half": {"price": 100}, "full": {"price": 170}}},
    {"id": 13, "name": "Pav Bhaji", "category": "Lunch", "portions": {"half": {"price": 110}, "full": {"price": 180}}},
    {"id": 14, "name": "Matar Paneer", "category": "Dinner", "portions": {"half": {"price": 140}, "full": {"price": 230}}},
    {"id": 15, "name": "Idli Sambar", "category": "Lunch", "portions": {"half": {"price": 90}, "full": {"price": 140}}},
    {"id": 16, "name": "Veg Hakka Noodles", "category": "Dinner", "portions": {"half": {"price": 150}, "full": {"price": 240}}},
    {"id": 17, "name": "Bhel Puri", "category": "Lunch", "portions": {"half": {"price": 70}, "full": {"price": 110}}},
    {"id": 18, "name": "Malai Kofta", "category": "Dinner", "portions": {"half": {"price": 180}, "full": {"price": 280}}},
    {"id": 19, "name": "Poha", "category": "Lunch", "portions": {"half": {"price": 80}, "full": {"price": 130}}},
    {"id": 20, "name": "Paneer Bhurji", "category": "Dinner", "portions": {"half": {"price": 150}, "full": {"price": 230}}}
]
def show_menu():
    print("\n----- MENU -----")
    for item in menu:
        print(f"ID: {item['id']} | {item['name']} ({item['category']})")
        for portion, data in item['portions'].items():
            print(f"  {portion.capitalize()}: ₹{data['price']}")
        print("-" * 20)

def add_dish():
    try:
        new_id = max(item['id'] for item in menu) + 1
    except ValueError:
        new_id = 1
    name = input("Enter dish name: ").strip()
    category = input("Enter category (Lunch/Dinner): ").strip().capitalize()
    if category not in ["Lunch", "Dinner"]:
        print("Invalid category! Must be 'Lunch' or 'Dinner'.")
        return
    try:
        half_price = int(input("Enter half portion price: "))
        full_price = int(input("Enter full portion price: "))
    except ValueError:
        print("Invalid price! Must be a number.")
        return

    dish = {
        "id": new_id,
        "name": name,
        "category": category,
        "portions": {
            "half": {"price": half_price},
            "full": {"price": full_price}
        }
    }
    menu.append(dish)
    print(f"Dish '{name}' added with ID {new_id}.")

def delete_dish():
    try:
        dish_id = int(input("Enter dish ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    for i, item in enumerate(menu):
        if item['id'] == dish_id:
            removed = menu.pop(i)
            print(f"Dish '{removed['name']}' deleted.")
            return
    print("Dish not found.")

def update_dish():
    try:
        dish_id = int(input("Enter dish ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return
    for item in menu:
        if item['id'] == dish_id:
            print(f"Current details: {item}")
            name = input("Enter new name (leave blank to keep current): ").strip()
            category = input("Enter new category (Lunch/Dinner, leave blank to keep current): ").strip().capitalize()
            half_price_input = input("Enter new half portion price (leave blank to keep current): ").strip()
            full_price_input = input("Enter new full portion price (leave blank to keep current): ").strip()

            if name:
                item['name'] = name
            if category in ["Lunch", "Dinner"]:
                item['category'] = category
            elif category:
                print("Invalid category, keeping old.")
            if half_price_input:
                try:
                    item['portions']['half']['price'] = int(half_price_input)
                except ValueError:
                    print("Invalid half price input, keeping old.")
            if full_price_input:
                try:
                    item['portions']['full']['price'] = int(full_price_input)
                except ValueError:
                    print("Invalid full price input, keeping old.")

            print("Dish updated.")
            return
    print("Dish ID not found.")

def main():
    while True:
        print("\nMenu Management")
        print("1. Show Menu")
        print("2. Add Dish")
        print("3. Delete Dish")
        print("4. Update Dish")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            show_menu()
        elif choice == '2':
            add_dish()
        elif choice == '3':
            delete_dish()
        elif choice == '4':
            update_dish()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
