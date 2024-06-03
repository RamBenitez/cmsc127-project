from Database import db_util

# Search food items from any establishment based on a given price range and/or food type.

def search(username):
    while True:
        print("\n\033[1m\033[94m------SEARCH MENU------\033[0m")
        print("[1] Search for food items by given price range")
        print("[2] Search for food items by food type")
        print("[3] Search for food items by given price range and food type")
        print("[0] Back")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            search_by_price_range()
        elif choice == 2:
            search_by_food_type()
        elif choice == 3:
            search_by_both()
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please try again.")

# Search for food items within a price range
def search_by_price_range():
    print("\n\033[1m\033[94m-----SEARCH BY PRICE RANGE-----\033[0m")
    lower_range = float(input("Input lower range: "))
    higher_range = float(input("Input higher range: "))
    
    # SQL query to retrieve food items within the price range and their food establishments
    query = """
    SELECT fi.Food_id, fi.Food_name, fi.Food_price, fe.Food_establishment_name
    FROM Food_Item fi
    JOIN Food_Establishment fe ON fi.Food_establishment_id = fe.Food_establishment_id
    WHERE fi.Food_price BETWEEN %s AND %s
    """
    params = (lower_range, higher_range)
    
    # Execute the query
    results = db_util.execute_query(query, params, fetch=True)
    
    # Print the food items within the price range
    if results:
        print("\nFood Items within the Price Range:")
        for item in results:
            print(f"Food ID: {item['Food_id']}, Food Name: {item['Food_name']}, Price: {item['Food_price']}, Establishment: {item['Food_establishment_name']}")
    else:
        print("No food items found within the specified price range.")

# Search for food items by food type
def search_by_food_type():
    print("\n\033[1m\033[94m-----SEARCH BY FOOD TYPE-----\033[0m")
    food_type = input("Enter food type: ")
    
    # SQL query to retrieve food items of the specified food type and their food establishments
    query = """
    SELECT fi.Food_id, fi.Food_name, fi.Food_price, fit.Food_item_type, fe.Food_establishment_name
    FROM Food_Item fi
    JOIN Food_Item_Type fit ON fi.Food_id = fit.Food_id
    JOIN Food_Establishment fe ON fi.Food_establishment_id = fe.Food_establishment_id
    WHERE fit.Food_item_type = %s
    """
    params = (food_type,)
    
    # Execute the query
    results = db_util.execute_query(query, params, fetch=True)
    
    # Print the food items matching the food type
    if results:
        print("Food Items of the Specified Food Type:")
        for item in results:
            print(f"Food ID: {item['Food_id']}, Food Name: {item['Food_name']}, Price: {item['Food_price']}, Type: {item['Food_item_type']}, Establishment: {item['Food_establishment_name']}")
    else:
        print("No food items found for the specified food type.")

# Search for food items by price range and food type
def search_by_both():
    print("\n\033[1m\033[94m-----SEARCH BY PRICE RANGE AND FOOD TYPE-----\033[0m")
    price_min = float(input("Enter minimum price: "))
    price_max = float(input("Enter maximum price: "))
    food_type = input("Enter food type: ")

    # SQL query to retrieve food items within the price range and of the specified food type
    query = """
    SELECT fi.Food_id, fi.Food_name, fi.Food_price, fit.Food_item_type, fe.Food_establishment_name
    FROM Food_Item fi
    JOIN Food_Item_Type fit ON fi.Food_id = fit.Food_id
    JOIN Food_Establishment fe ON fi.Food_establishment_id = fe.Food_establishment_id
    WHERE fi.Food_price BETWEEN %s AND %s AND fit.Food_item_type = %s
    """
    params = (price_min, price_max, food_type)
    
    # Execute the query
    results = db_util.execute_query(query, params, fetch=True)
    
    # Print the food items matching the price range and food type
    if results:
        print("Food Items within the Specified Price Range and Food Type:")
        for item in results:
            print(f"Food ID: {item['Food_id']}, Food Name: {item['Food_name']}, Price: {item['Food_price']}, Type: {item['Food_item_type']}, Establishment: {item['Food_establishment_name']}")
    else:
        print("No food items found for the specified price range and food type.")