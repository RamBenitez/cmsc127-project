def signup():
    while True:
        print("\n-------- SIGN UP --------")
        print("[1] Sign Up as Customer")
        print("[2] Sign Up as Food Establishment Owner")
        print("[3] Back")
        print("[0] Exit") 
        choice = input("Enter your choice: ") 

        if choice == '1':
            signup_customer()
        elif choice == '2':
            signup_owner()
        elif choice == '3':
            break
        elif choice == '0':
            print("Exiting the application.")
            exit(0)
        else:
            print("Invalid choice. Please try again.")  


 #Sign up as customer             
def signup_customer():
    print("\n Customer Signup ")


#sign up as customer
def signup_owner():
    print("\n Food Establishment Owner Signup ")
