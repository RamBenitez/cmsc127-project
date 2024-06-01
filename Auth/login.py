from Customer.customer import customer_menu

def login():
   #DUMMY LANG ito yong valid credentials for logging in 
    valid_username="Alice"
    valid_password="Alice"
    valid_name="Alice Guo"

    print("\n-----------LOG IN ---------")
    username= input("Enter username:")
    password= input("Enter password:")

    #successfull login
    if username == valid_username and password == valid_password:
        print("\nSuccessfully logged in!")
        print(f"Welcome, {valid_name}!") #dummy palang
        return valid_name
     #invalid username or password   
    else:
        print("\nInvalid username/password")
        print("Please try again\n")
        return None


def successful_login(name):
    customer_menu(name)