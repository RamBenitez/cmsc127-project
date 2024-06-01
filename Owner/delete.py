def delete():
    while True:
        print("\n\033[1m------DELETE MENU------\033[0m") 
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
            print("Invalid choice. Please try again.")

def delete_food_establishment():
    print("\n\033[1m------DELETE A FOOD ESTABLISHMENT------\033[0m")  
    # Query to get all food establishments
    # Print all food establishments
    print("Food Establishments...")
    choice = input("Choice: ")
    # Query to delete the selected food establishment
    # Delete the food establishment from the database
    print("Successfully Deleted!")

def delete_food_item():
    print("\n\033[1m------DELETE A FOOD ITEM------\033[0m")  
    # Query to get all food items of the selected food establishment
    # Print all food items
    print("Food Items:")
    choice = input("Choice: ")
    # Query to delete the selected food item
    # Delete the food item from the database
    print("Successfully Deleted!")

def delete_food_review():
    print("\n\033[1m------DELETE A FOOD REVIEW------\033[0m")  
    # Query to get all food reviews
    # Print all food reviews
    print("Food Reviews...")
    choice = input("Choice: ")
    # Query to delete the selected food review
    # Delete the food review from the database
    print("Successfully Deleted!")
