def search_food_item():
    while True:
        print("\n------SEARCH FOR A FOOD ITEM MENU------")
        print("[1] Search by price range")
        print("[2] Search by food type")
        print("[3] Back")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            search_by_price_range()
        elif choice == '2':
            search_by_food_type()
        elif choice == '3':
            break
        else:
            print("\nInvalid choice. Please try again.")

# Search for food items within a price range
def search_by_price_range():
    print("\n-----SEARCH BY PRICE RANGE-----")
    lower_range = float(input("Input lower range: "))
    higher_range = float(input("Input higher range: "))
    # Query the database to retrieve food items within the price range
    # Print the food items that fall within the  price range

# Search for food items by food type
def search_by_food_type():
    print("\n-----SEARCH BY FOOD TYPE-----")
    food_type = input("Input food type: ")
    # Query the database to retrieve food items of the food type
    # Print the food items that match the food type
