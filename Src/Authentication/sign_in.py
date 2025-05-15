class User:
    def __init__(self, username, password, contract, address):
        self.username = username
        self.password = password
        self.contract = contract
        self.address = address

    def __str__(self):
        return f"User(username: {self.username}, address: {self.address})"
users_db = {}

def register_user(username, password, contract, address):
    if username in users_db:
        print("Username already exists. Please try a different one.")
    else:
        new_user = User(username, password, contract, address)  
        users_db[username] = new_user  
        print(f"User {username} registered successfully!")
def sign_in(username, password):
    if username not in users_db:
        print("No such username found!")
        return False

    user = users_db[username]
    if user.password == password:
        print(f"Welcome back, {user.username}!")
        return True
    else:
        print("Incorrect password!")
        return False
username = input("Enter username: ")
password = input("Enter password: ")
contract = input("Enter contract info: ")
address = input("Enter address: ")

register_user(username, password, contract, address)
username = input("Enter username to sign in: ")
password = input("Enter password: ")

if sign_in(username, password):
    print("Sign in successful!")
else:
    print("Sign in failed!")
