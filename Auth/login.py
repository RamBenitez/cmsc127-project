def login():
   #DUMMY LANG
    valid_username="Alice"
    valid_password="Alice"
    valid_name="Alice Guo"

    print("\n-----------LOG IN ---------")
    username= input("Enter username:")
    password= input("Enter password:")

    if username == valid_username and password == valid_password:
        print("\nSuccessfully logged in!")
        print(f"Welcome, {username}!")
    else:
        print("\nInvalid username/password")
        print("Please try again\n")


def successful_login():
    print("{ nakasign up}")