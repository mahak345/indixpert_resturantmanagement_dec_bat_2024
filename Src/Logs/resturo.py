import logging

logging.basicConfig(filename='restaurant.log', level=logging.INFO, format='%(asctime)s - %(message)s')
users = {}

menu = {
    1: {"name": "Paneer Tikka", "half": 140, "full": 190},
    2: {"name": "Masala Dosa", "half": 100, "full": 170},
    100: {"name": "Special Thali", "half": 180, "full": 300},
}

tables = {} 

def signup():
    username = input("Enter new username: ")
    if username in users:
        print("User already exists.")
        return False
    password = input("Enter password: ")
    users[username] = password
    logging.info(f"New user signed up: {username}")
    print(" Signup successful.")
    return True

def signin():
    username = input("Username: ")
    password = input("Password: ")
    if users.get(username) == password:
        logging.info(f"User signed in: {username}")
        print(" Sign-in successful.")
        return True
    else:
        print(" Invalid credentials.")
        return False

# ----------- Core Features -----------
def show_menu():
    print("\n--- MENU ---")
    for id, item in menu.items():
        print(f"{id}. {item['name']} - Half: ₹{item['half']}, Full: ₹{item['full']}")
    print("------------")

def book_table():
    try:
        table = int(input("Table number: "))
        if table in tables:
            print(" Already booked.")
            return
        name = input("Customer name: ")
        tables[table] = {"customer": name, "orders": []}
        print(f"Table {table} booked for {name}.")
    except:
        print(" Invalid input.")

def place_order():
    try:
        table = int(input("Table number: "))
        if table not in tables:
            print(" Table not booked.")
            return
        show_menu()
        item_id = int(input("Enter item ID: "))
        size = input("Size (half/full): ").lower()
        qty = int(input("Quantity: "))
        item = menu[item_id]
        price = item[size] * qty
        tables[table]['orders'].append((item['name'], size, qty, price))
        print(f"{qty} x {item['name']} ({size}) added.")
    except Exception as e:
        logging.error(f"Order error: {e}")
        print(" Error in order.")

def generate_bill():
    try:
        table = int(input("Table number: "))
        if table not in tables:
            print(" Table not found.")
            return
        print(f"\n=== Bill for Table {table} ===")
        total = 0
        for name, size, qty, price in tables[table]['orders']:
            print(f"{qty} x {name} ({size}) = ₹{price}")
            total += price
        print(f"TOTAL: ₹{total}\n=========================")
        logging.info(f"Bill generated for table {table}: ₹{total}")
    except:
        print(" Error generating bill.")
def main():
    print("Welcome to Restaurant System")
    while True:
        choice = input("\n1. Sign Up\n2. Sign In\n3. Exit\nChoose: ")
        if choice == '1':
            signup()
        elif choice == '2' and signin():
            while True:
                action = input("\n1. Book Table\n2. Place Order\n3. Show Bill\n4. Logout\nChoose: ")
                if action == '1': book_table()
                elif action == '2': place_order()
                elif action == '3': generate_bill()
                elif action == '4': break
        elif choice == '3':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
