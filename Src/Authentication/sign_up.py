import json
import os

USER_FILE = 'users.json'

def load_users():
    try:
           with  open(USER_FILE, 'r') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, FileNotFoundError):
         return []

def Sign_up(): 
    print("== Sign Up ==")
    email = input("Enter email: ")
    password = input("Enter password: ")
    address=input("Enter address:")
    contract=input("Enter contract:")
    role = input("Enter role (user/admin/staff): ").lower()

    if role not in ['user', 'admin', 'staff']:
        print("Invalid role. Please choose from user/admin/staff.")
        return

    users = load_users()
    for user in users:
        if user['email'] == email:
            print("Email already exists. Please try again.")
        return

    users.append({'email': email, 'password': password, 'role': role})
    print("User registered successfully!")