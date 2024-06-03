from .add_review import add_review
from .delete_review import delete_review
from .search_food_establishment import search_food_establishment
from .search_food_item import search_food_item
from .update_review import update_review

def customer_menu(username, name):
    while True:
        print(f"\n\033[1m\033[94m Welcome, {name}!\033[0m\n") #dummy palang
        print("\033[1m—---------- MENU —----\033[0m")
        print("[1] Add a review")
        print("[2] Update a review")
        print("[3] Delete a review")
        print("[4] Search for a food item")
        print("[5] Search for a food establishment")
        print("[6] Log out")
        print("[0] Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_review(username)
        elif choice == '2':
            update_review(username)
        elif choice == '3':
            delete_review(username)
        elif choice == '4':
            search_food_item()
        elif choice == '5':
            search_food_establishment()
        elif choice == '6':
            print("Logging out.")
            break
        elif choice == '0':
            print("Exiting the application.")
            exit(0)
        else:
            print("Invalid choice. Please try again.")

