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
                login()
        elif choice == '2':
            if signup_owner():
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
    
    print("\n-----SIGN UP CUSTOMER -----")
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
    print("\n-----SIGN UP OWNER -----")
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

  