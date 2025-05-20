import json
import os

USER_DB = "Src/logs/Database/admin.json"

def is_valid_username(username):
    return username.isalpha()

def is_valid_password(password):
    return password.isdigit()

def sign_in():
    if not os.path.exists(USER_DB):
        print("No users found. Please sign up first.")
        return False

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not is_valid_username(username):
        print("Invalid username! Only alphabetic characters are allowed.")
        return False

    if not is_valid_password(password):
        print("Invalid password! Only numeric digits are allowed.")
        return False

    with open(USER_DB, 'r') as f:
        users = json.load(f)
 
 
 
    for user in users:
       if user['username'] == username and user['password'] == password:
            print("Login successful!")
            return True
    print("Invalid username or password")
    return False
