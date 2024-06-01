from .login import login 
from Customer.customer import customer_menu
from Owner.owner import owner_menu

def signup():
    while True:
        print("\n-------- SIGN UP --------")
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
                    print("Login failed. Please try again.")
                    login()
        elif choice == '2':
            if signup_owner():
                name = login()
                if name:
                    owner_menu(name)
                    break  
                else:
                    print("Login failed. Please try again.")
                    login()
        elif choice == '3':
            break
        elif choice == '0':
            print("Exiting the application.")
            exit(0)
        else:
            print("Invalid choice. Please try again.")  


 #Sign up as customer             
def signup_customer():
    
    print("\n\033[1m-----SIGN UP CUSTOMER -----\033[0m")
    customerName= input("Enter name:")
    customerUsername= input("Enter username:")
    customerPassword= input("Enter password:")
    customerConfirmPassword= input("Confirm password:")

    if customerPassword != customerConfirmPassword:
        print("\nPasswords do not match. Please try again.\n")
        return False
    else:
        #Save the new customer to the database
        print("\nCustomer signed up successfully!\n")
        return True


#sign up as customer
def signup_owner():
    print("\n\033[1m-----SIGN UP OWNER -----\033[0m")
    ownerName= input("Enter name:")
    ownerUsername= input("Enter username:")
    ownerPassword= input("Enter password:")
    ownerConfirmPassword= input("Confirm password:")

    if ownerPassword != ownerConfirmPassword:
        print("\nPasswords do not match. Please try again.\n")
        return False
    else:
        #Save the new owner to the database
        print("\nCustomer signed up successfully!\n")
        return True

  