import json

MENU_DB = "Src/logs/Database/menu.json"
ORDER_DB = "Src/logs/Database/order.json"

def place_order():
    try:
        with open(MENU_DB, 'r') as f:
            menu = json.load(f)

        orders = []

        while True:
            item_id = input("Enter item ID to order (or 'done' to finish): ").strip()
            if item_id.lower() == 'done':
                break

            if not item_id.isdigit():
                print("Please enter a valid numeric ID.")
                continue

            item_id = int(item_id)
            item = next((i for i in menu if i['id'] == item_id), None)

            if not item:
                print("Item not found.")
                continue

            print(f"DEBUG: Found item: {item}")

            available_portions = []
            if 'portions' in item and isinstance(item['portions'], dict):
                for portion_name in ['half', 'full']:
                    portion_data = item['portions'].get(portion_name)
                    if portion_data and isinstance(portion_data, dict):
                        price = portion_data.get('price')
                        if isinstance(price, (int, float)) and price > 0:
                            available_portions.append(portion_name)

            print(f"DEBUG: Available portions: {available_portions}")

            if not available_portions:
                print("No available portions for this item.")
                continue

            print(f"Available portions: {', '.join(available_portions)}")
            portion = input("Enter portion size (half/full): ").strip().lower()

            if portion not in available_portions:
                print(f"{portion.capitalize()} portion not available for this item.")
                continue

            quantity = input("Enter quantity: ").strip()
            if not quantity.isdigit() or int(quantity) <= 0:
                print("Invalid quantity.")
                continue
            quantity = int(quantity)

            price = item['portions'][portion]['price']
            total = price * quantity

            orders.append({
                "item_id": item['id'],
                "item_name": item['name'],
                "portion": portion,
                "price": price,
                "quantity": quantity,
                "total": total
            })

            print(f"Added {quantity} x {item['name']} ({portion}) to your order.")

        with open(ORDER_DB, 'w') as f:
            json.dump(orders, f, indent=4)

        print("\nOrder placed successfully.")
    except Exception as e:
        print("Error placing order:", e)
