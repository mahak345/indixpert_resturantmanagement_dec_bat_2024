from sign_in import sign_in

def main():
    while True:
        print("\n1. Sign In\n2. Sign Up\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
             sign_in()
        elif choice == '2':
            print("Sign Up option not yet implemented.")  
         elif choice == '3':
         print("Goodbye!")
        break
    else:
     print("Invalid option. Try again.")

if __name__ == "__main__":
    main ()
