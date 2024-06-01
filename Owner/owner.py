from .add import add
from .delete import delete
from .reports import reports
from .search import search
from .update import update

def owner_menu(name):
    while True:
        print(f"\nWelcome, {name}!\n") #dummy palang
        print("—---------- MENU —----")
        print("[1] Add")
        print("[2] Update")
        print("[3] Delete")
        print("[4] Search")
        print("[5] reports")
        print("[6] Log out")
        print("[0] Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            add()
        elif choice == '2':
            update()
        elif choice == '3':
            delete()
        elif choice == '4':
            search()
        elif choice == '5':
            reports()
        elif choice == '6':
            print("Logging out.")
            break
        elif choice == '0':
            print("Exiting the application.")
            exit(0)
        else:
            print("Invalid choice. Please try again.")

