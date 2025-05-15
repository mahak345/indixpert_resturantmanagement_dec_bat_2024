# sign_in.py

def sign_in(users):
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = users.get(username)
    if user and user["password"] == password:
        print("Sign in successful!")
        print("Contract:", user["contract"])
        print("Address:", user["address"])
    else:
        print("Invalid username or password.")
