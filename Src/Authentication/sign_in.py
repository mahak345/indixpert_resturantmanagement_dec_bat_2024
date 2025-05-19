import json
import os

def sign_in():
    print("\n--- Sign In ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    users_file = 'database/users.json'

    if not os.path.exists(users_file):
        print("No user database found. Please sign up first.")
        return False

    with open(users_file, 'r') as f:
        users = json.load(f)

    for user in users:
        if user['username'] == username and user['password'] == password:
            print("Sign in successful!")
            return True

    print("Invalid username or password.")
    return False
