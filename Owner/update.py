def update():
    while True:
        print("\n\033[1m------UPDATE MENU------\033[0m") 
        print("[1] Update a food establishment")
        print("[2] Update a food item")
        print("[3] Back")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            update_food_establishment()
        elif choice == '2':
            update_food_item()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def update_food_establishment():
    print("\n\033[1m------UPDATE A FOOD ESTABLISHMENT------\033[0m")  
    # Query to get all food establishments
    # Print all food establishments
    print("Food Establishments...")
    choice = input("Choice: ")
    new_name = input("Enter New Food Establishment Name: ")
    # Query to update the food establishment name in the database

def update_food_item():
    print("\n\033[1m------UPDATE A FOOD ITEM------\033[0m")  
    # Query to get all food items of the selected food establishment
    # Print all food items
    print("Food Items:")
    choice = input("Choice: ")
   
    new_name = input("Enter New Food Item Name: ")
    new_price = input("Enter New Food Item Price: ")
    new_category = input("Enter New Food Item Category: ")
    # Update food item name, price, and category in the database
