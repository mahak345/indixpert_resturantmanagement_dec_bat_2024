def sign_in():
    print("\n--- Sign In ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    users = load_user()
    for user in users:
        if user['username'] == username and user['password'] == password:
            print("Sign in successful!")
            return
    print("Invalid username or password.")
