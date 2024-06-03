def delete():
    while True:
        print("\n\033[1m\033[94m------DELETE MENU------\033[0m") 
        print("[1] Delete a food establishment")
        print("[2] Delete a food item")
        print("[3] Delete a food review")
        print("[4] Back")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            delete_food_establishment()
        elif choice == '2':
            delete_food_item()
        elif choice == '3':
            delete_food_review()
        elif choice == '4':
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")

def delete_food_establishment():
    print("\n\033[1m\033[94m------DELETE A FOOD ESTABLISHMENT------\033[0m")  
    # Query to get all food establishments
    # Print all food establishments
    print("List of all Food Establishments...")
    choice = input("Choice: ")
    # Query to delete the selected food establishment
    # Delete the food establishment from the database
    print("\033[92mSuccessfully Deleted!\033[0m")

def delete_food_item():
    print("\n\033[1m\033[94m------DELETE A FOOD ITEM------\033[0m")
    print("List of all Food Establishments...")
    est_choice = input("Choice: ")  
    # Query to get all food items of the selected food establishment
    # Print all food items
    print("List of all Food Items in :")
    food_choice = input("Choice: ")
    # Query to delete the selected food item
    # Delete the food item from the database
    print("\033[92mSuccessfully Deleted!\033[0m")

def delete_food_review():
    print("\n\033[1m------DELETE A FOOD REVIEW------\033[0m")  
    # Query to get all food reviews
    # Print all food reviews
    print("List of all Food Reviews...")
    choice = input("Choice: ")
    # Query to delete the selected food review
    # Delete the food review from the database
    print("\033[92mSuccessfully Deleted!\033[0m")
