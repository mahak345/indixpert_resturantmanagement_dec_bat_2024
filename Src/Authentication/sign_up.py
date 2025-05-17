import json
import os
import re

USERS_FILE =  "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return [] 
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def sign_up():
    print("\n--- Sign Up ---")
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    contact = input("Enter your contact number: ")
    address = input("Enter your address (max 100 chars): ")
    if len(address) > 100:
        address = address[:100]
        print("Address truncated to 100 characters.")
    email = input("Enter your email: ")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format.")
        return

    users = load_users()

    # Check duplicate username
    if any(u['username'] == username for u in users):
        print("Username already exists.")
        return

    users.append({
        "username": username,
        "password": password,
        "contact": contact,
        "address": address,
        "email": email
    })
    save_users(users)
    print("Sign up successful!")


