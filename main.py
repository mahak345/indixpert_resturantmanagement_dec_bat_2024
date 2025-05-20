import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Src.Authentication.sign_in import sign_in
from Src.Authentication.sign_up import sign_up
from Src.Authentication.exit_program import exit_program
from Src.Domain.Bill.Generate_bill import generate_bill
from Src.Domain.Booking.tablebooking import table_booking
from Src.Domain.Menu.menu import show_menu
from Src.Domain.order.order_class import place_order
from Src.logs.restaurant_logs import log_event 
def main_menu():
    while True:
        print("\n--- Welcome to Vegetarian Restaurant Management System ---")
        print("1. Sign In")
        print("2. Sign Up")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            if sign_in():
                logged_in_menu()
                break
        elif choice == '2':
            sign_up()
        elif choice == '3':
            exit_program()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def logged_in_menu():
    while True:
        print("\n--- Main Dashboard ---")
        print("1. Display Menu")
        print("2. Take Order")
        print("3. Book Table")
        print("4. Generate Bill")
        print("5. Log Out")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            show_menu()
            log_event("Displayed Menu")
        elif choice == '2':
            place_order()
            log_event("Order Taken")
        elif choice == '3':
            table_booking()
            log_event("Table Booked")
        elif choice == '4':
            generate_bill()
            log_event("Bill Generated")
        elif choice == '5':
            print("Logging out...\n")
            break
        else:
            print("Invalid option. Please select between 1 and 5.")

if __name__ == "__main__":
    main_menu()
