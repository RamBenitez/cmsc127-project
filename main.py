from Auth.login import login
from Auth.signup import signup

def main_menu():
    while True:
        print("\n-------- MENU --------")  
        print("[1] Log In")
        print("[2] Sign Up")
        print("[0] Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            login()
        elif choice == '2':
            signup()
        elif choice == '0':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
