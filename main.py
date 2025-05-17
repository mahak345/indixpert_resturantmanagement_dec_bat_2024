from Src.Authentication import sign_up, sign_in, exit_program

def main():
    while True:
        print("\n===== Restaurant Management System =====")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
     main()
