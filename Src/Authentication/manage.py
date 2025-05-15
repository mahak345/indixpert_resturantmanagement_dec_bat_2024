import os
import json
from .sign_in import sign_in
from .sign_up import Sign_up

USER_FILE = 'users.json'
def init_user_file():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w') as f:
             json.dump([], f)

def main(): 
    init_user_file()

    while True:
        print("\n1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = input(" Choose an option: ")

        if choice == '1':
            print("sign in")
            Sign_up()
        elif choice == '2':
            sign_in()
            print("sign up")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
     main()
