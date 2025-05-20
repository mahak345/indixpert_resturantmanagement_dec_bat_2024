import json
import os
import re

USER_DB = "Src/logs/Database/admin.json"

def is_valid_username(username):
    return username.isalpha()

def is_valid_password(password):
    return password.isdigit()

def is_valid_contact(contact):
    return contact.isdigit() and len(contact) == 10

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def sign_up():
    if not os.path.exists(USER_DB):
        with open(USER_DB, 'w') as f:
            json.dump([], f)

    username = input("Enter username (alphabets only): ").strip()
    password = input("Enter password (digits only): ").strip()
    contact = input("Enter contact number (10 digits): ").strip()
    address = input("Enter address: ").strip()
    email = input("Enter email: ").strip()

    if not is_valid_username(username):
        print("Invalid username! Only alphabetic characters are allowed.")
        return

    if not is_valid_password(password):
        print("Invalid password! Only numeric digits are allowed.")
        return

    if not is_valid_contact(contact):
        print("Invalid contact! Must be exactly 10 digits.")
        return

    if not address:
        print("Address cannot be empty.")
        return

    if not is_valid_email(email):
        print("Invalid email format.")
        return

    with open(USER_DB, 'r') as f:
        users = json.load(f)
    for user in users:
        if user['username'] == username:
            print("Username already exists!")
            return

    users.append({
        'username': username,
        'password': password,
        'contact': contact,
        'address': address,
        'email': email
    })

    with open(USER_DB, 'w') as f:
        json.dump(users, f, indent=4)

    print("Sign-up successful!")
