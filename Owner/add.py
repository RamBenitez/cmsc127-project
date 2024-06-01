def add():
    while True:
        print("\n\033[1m------ADD MENU------\033[0m") 
        print("[1] Add a food establishment")
        print("[2] Add a food item")
        print("[3] Back")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            add_food_establishment()
        elif choice == '2':
            add_food_item()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def add_food_establishment():
    print("\n\033[1m------ADD A FOOD ESTABLISHMENT------\033[0m")  
    FoodEstablishmentName =input("Enter Food Establishment Name:")
    #insert  query food establishment name to database

def add_food_item():
    print("\n\033[1m------ADD A FOOD ITEM------\033[0m")  
    FoodItemName =input("Enter Food Establishment Name:")
    FoodItemEstablishmentName =input("Enter Food Item Establishment Name:")
    FoodItemPrice =input("Enter Food Item Price:")
    FoodItemCategory=input("Enter Food Item Category:")
    #insert queries to add food item infos 