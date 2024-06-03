from Customer.customer import customer_menu
from Owner.owner import owner_menu
from Database import db_util
import bcrypt # for hashing passwords

def login():

    print("\n\033[1m\033[94m-----------LOG IN -----------\033[0m")
    username= input("Enter username: ")
    password= input("Enter password: ")

    query = "SELECT * FROM User WHERE Username = %s"
    params = (username,)
    result = db_util.execute_query(query, params, True) # retrieves results that match the username

    if result:
        stored_password = result[0]['Password'].encode('utf-8')  # Decode to bytes
        if check_password(stored_password, password):
            name = result[0]['Name']
            usertype = result[0]['Usertype']
            print("\n\033[92mSuccessfully logged in!\033[0m")
            print(f"\033[92mWelcome, {name}!\033[0m")

            if usertype == 'Customer':
                print("You are logged in as a Customer.")
                customer_menu(name)
            elif usertype == 'Owner':
                print("You are logged in as an Owner.")
                owner_menu(name)

            return
        else:
            print("\n\033[91mInvalid password. Please try again.\033[0m\n")
            return None
    else:
        print("\n\033[91mInvalid username/password. Please try again.\033[0m")
        return None

def check_password(stored_password, entered_password):
    # Check if the entered password matches the stored hashed password
    return bcrypt.checkpw(entered_password.encode(), stored_password)