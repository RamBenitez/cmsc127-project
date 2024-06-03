from .login import login 
from Customer.customer import customer_menu
from Owner.owner import owner_menu
from Database import db_util
import bcrypt # for hashing passwords

def signup():
    while True:
        print("\n\033[1m\033[94m-------- SIGN UP --------\033[0m")
        print("[1] Sign Up as Customer")
        print("[2] Sign Up as Food Establishment Owner")
        print("[3] Back")
        print("[0] Exit") 
        choice = input("Enter your choice: ") 

        if choice == '1':
            if signup_customer():
                name = login()
                if name:
                    customer_menu(name)  
                    break
                else:
                    print("\033[91mLogin failed. Please try again.\033[0m")
                    login()
        elif choice == '2':
            if signup_owner():
                name = login()
                if name:
                    owner_menu(name)
                    break  
                else:
                    print("\033[91mLogin failed. Please try again.\033[0m")
                    login()
        elif choice == '3':
            break
        elif choice == '0':
            print("Exiting the application.")
            exit(0)
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")  


# Sign up as customer             
def signup_customer():
    
    print("\n\033[1m\033[94m-----SIGN UP AS CUSTOMER -----\033[0m")
    customerName= input("Enter name: ")
    customerUsername= input("Enter username: ")
    customerPassword= input("Enter password: ")
    customerConfirmPassword= input("Confirm password: ")

    if customerPassword != customerConfirmPassword:
        print("\n\033[91mPasswords do not match. Please try again.\033[0m\n")
        return False
    else:

        # converting password to array of bytes 
        encodedPass = customerPassword.encode('utf-8') 
        
        # generating the salt 
        salt = bcrypt.gensalt() 
        
        # Hashing the password 
        hashedPW = bcrypt.hashpw(encodedPass, salt) 

        # Save the new customer to the database
        query = """
        INSERT INTO User (Username, Password, Name, Usertype)
        VALUES (%s, %s, %s, 'Customer')
        """                                                     # Password() for encrpytion
        params = (customerUsername, hashedPW, customerName) 
        result = db_util.execute_query(query, params)
        if result:
            print("\n\033[92mCustomer signed up successfully!\033[0m\n")
            return True
        else:
            print("\n\033[91mFailed to sign up. Please try again.\033[0m\n")
            return False


# Sign up as an owner
def signup_owner():
    print("\n\033[1m\033[94m-----SIGN UP AS OWNER -----\033[0m")
    ownerName= input("Enter name: ")
    ownerUsername= input("Enter username: ")
    ownerPassword= input("Enter password: ")
    ownerConfirmPassword= input("Confirm password: ")

    if ownerPassword != ownerConfirmPassword:
        print("\n\033[91mPasswords do not match. Please try again.\033[0m\n")
        return False
    else:

        # converting password to array of bytes 
        encodedPass = ownerPassword.encode('utf-8') 
        
        # generating the salt 
        salt = bcrypt.gensalt() 
        
        # Hashing the password 
        hashedPW = bcrypt.hashpw(encodedPass, salt)

        # Save the new owner to the database
        query = """
        INSERT INTO User (Username, Password, Name, Usertype)
        VALUES (%s, %s, %s, 'Owner')
        """                                                     # Password() for encrpytion
        params = (ownerUsername, hashedPW, ownerName) 
        result = db_util.execute_query(query, params)
        if result:
            print("\n\033[92mOwner signed up successfully!\033[0m\n")
            return True
        else:
            print("\n\033[91mFailed to sign up. Please try again.\033[0m\n")
            return False
  