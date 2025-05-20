import os
import json

ORDER_DB = "Src/logs/Database/order.json"
BILL_DB = "Src/logs/Database/bill.json"

def generate_bill():
    try:
    
        if not os.path.exists(ORDER_DB):
            print("Order file not found. Please ensure an order is placed before generating a bill.")
            return

        with open(ORDER_DB, 'r') as f:
            orders = json.load(f)

        if not orders:
            print("No orders to bill.")
            return

        total_amount = sum(item['total'] for item in orders)

        print("\n--- Bill Receipt ---")
        for item in orders:
            print(f"{item['quantity']} x {item['item_name']} ({item['portion']}) - ₹{item['total']}")
        print(f"Total: ₹{total_amount}")
        print("--------------------\n")

        bill_data = {
            "orders": orders,
            "total": total_amount
        }
        with open(BILL_DB, 'a') as f:
            f.write(json.dumps(bill_data) + '\n')

        print("Bill generated and saved successfully.")

    except FileNotFoundError:
        print(" Order file not found.")
    except json.JSONDecodeError:
        print("Order file is corrupted or not in valid JSON format.")
    except Exception as e:
        print(" Error generating bill:", e)

if __name__ == "__main__":
    generate_bill() 

