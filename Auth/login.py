from Customer.customer import customer_menu

def login():
   #DUMMY LANG ito yong valid credentials for logging in 
    valid_username="Alice"
    valid_password="Alice"
    valid_name="Alice Guo"

    print("\n\033[1m\033[94m-----------LOG IN -----------\033[0m")
    username= input("Enter username:")
    password= input("Enter password:")

    #successfull login
    if username == valid_username and password == valid_password:
        print("\n\033[92mSuccessfully logged in!\033[0m")
        print(f"\033[92mWelcome, {valid_name}!\033[0m") #dummy palang
        return valid_name
     #invalid username or password   
    else:
        print("\n\033[91mInvalid username/password\033[0m")
        print("\033[91mPlease try again\n\033[0m")
        return None


def successful_login(name):
    customer_menu(name)