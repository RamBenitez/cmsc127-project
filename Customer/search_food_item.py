from Database import db_util

def search_food_item():
    while True:
        print("\n\033[1m\033[94m------SEARCH FOR A FOOD ITEM MENU------\033[0m")
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
            print("\n\033[91mInvalid choice. Please try again.\033[0m")

# Search for food items within a price range
def search_by_price_range():
    print("\n\033[1m\033[94m-----SEARCH BY PRICE RANGE-----\033[0m")
    lower_range = float(input("Input lower range: "))
    higher_range = float(input("Input higher range: "))
    
    # SQL query to retrieve food items within the price range
    query = """
    SELECT Food_id, Food_name, Food_price
    FROM Food_Item
    WHERE Food_price BETWEEN %s AND %s
    """
    params = (lower_range, higher_range)
    
    # Execute the query
    results = db_util.execute_query(query, params, fetch=True)
    
    # Print the food items within the price range
    if results:
        print("\nFood Items within the Price Range:")
        for item in results:
            print(f"Food ID: {item['Food_id']}, Food Name: {item['Food_name']}, Price: {item['Food_price']}")
    else:
        print("No food items found within the specified price range.")

# Search for food items by food type
def search_by_food_type():
    print("\n\033[1m\033[94m-----SEARCH BY FOOD TYPE-----\033[0m")
    food_type = input("Input food type: ")
    
    # SQL query to retrieve food items of the specified food type
    query = """
    SELECT fi.Food_id, fi.Food_name, fi.Food_price
    FROM Food_Item fi
    JOIN Food_Item_Type fit ON fi.Food_id = fit.Food_id
    WHERE fit.Food_item_type = %s
    """
    params = (food_type,)
    
    # Execute the query
    results = db_util.execute_query(query, params, fetch=True)
    
    # Print the food items matching the food type
    if results:
        print("Food Items of the Specified Food Type:")
        for item in results:
            print(f"Food ID: {item['Food_id']}, Food Name: {item['Food_name']}, Price: {item['Food_price']}")
    else:
        print("No food items found for the specified food type.")
