from Src.Authentication.sign_up import sign_up
from Src.Authentication.sign_in import sign_in
from Src.Authentication.exit_program import exit_program

def main():
    print("Welcome to the Vegetarian Restaurant Management System!")

    is_logged_in = False

    while True:
        print("\nMain Menu")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Enter your choice: ")

from Src.Menu._menu import view_menu
from Src.order.place_order import place_order
from Src.Bill.Generate_bill import generate_bill
from Src.TableBooking.book_table import book_table

def main():
    print("Welcome to the Vegetarian Restaurant Management System!")

    is_logged_in = False

    while True:
        print("\nMain Menu")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. View Menu")
        print("4. Place Order")
        print("5. Generate Bill")
        print("6. Book Table")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            is_logged_in = sign_in()
            if is_logged_in:
                print("Successfully signed in.")
            else:
                print("Sign-in failed.")
        elif choice == '3':
            if is_logged_in:
                view_menu()
            else:
                print("Please sign in first.")
        elif choice == '4':
            if is_logged_in:
                place_order()
            else:
                print("Please sign in first.")
        elif choice == '5':
            if is_logged_in:
                generate_bill()
            else:
                print("Please sign in first.")
        elif choice == '6':
            if is_logged_in:
                book_table()
            else:
                print("Please sign in first.")
        elif choice == '7':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
