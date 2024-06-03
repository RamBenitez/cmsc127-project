from Database import db_util

# Search food items from any establishment based on a given price range and/or food type.

def search():
    while True:
        print("\n\033[1m\033[94m------SEARCH MENU------\033[0m")
        print("[1] Search for food items by given price range")
        print("[2] Search for food items by food type")
        print("[3] Search for food items by given price range and food type")
        print("[3] Back")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            search_by_price_range()
        elif choice == 2:
            search_by_food_type()
        elif choice == 3:
            search_by_both()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

def search_by_price_range():
    print("\n\033[1m\033[94m------SEARCH VIA PRICE RANGE------\033[0m")
    price_min = input("Enter minimum price: ")
    price_min = float(price_min)

    price_max = input("Enter maximum price: ")
    price_max = float(price_max)

    query = "SELECT * FROM Food_Item WHERE Food_price BETWEEN %s AND %s"
    params = (price_min, price_max)
    results = db_util.execute_query(query, params, True)

    if results:
        for i in results:
            print(f"{i['Food_id']}: {i['Food_name']} - Php {i['Food_price']}")
    else:
        print("\n\033[91mFailed to find any food item matching the price range. Please try again.\033[0m\n")
        return False

def search_by_food_type():
    print("\n\033[1m\033[94m------SEARCH VIA FOOD TYPE------\033[0m")
    food_type = input("Enter food type: ")
    query = "SELECT * FROM Food_Item fi JOIN Food_Item_Type fit ON fi.food_name WHERE fit.Food_item_type=%s"
    params = (food_type, )
    results = db_util.execute_query(query, params, True)

    if results:
        for i in results:
            print(f"{i['Food_id']}: {i['Food_name']} - {i['Food_item_type']}")
    else:
        print("\n\033[91mFailed to find any food item matching the food type. Please try again.\033[0m\n")
        return False

def search_by_both():
    print("\n\033[1m\033[94m------SEARCH VIA PRICE RANGE AND FOOD TYPE------\033[0m")
    price_min = input("Enter minimum price: ")
    price_min = float(price_min)

    price_max = input("Enter maximum price: ")
    price_max = float(price_max)

    food_type = input("Enter food type: ")

    query = "SELECT * FROM Food_Item fi JOIN Food_Item_Type fit ON fi.food_name WHERE fi.Food_price BETWEEN %s AND %s AND fit.Food_item_type=%s"
    params = (price_min, price_max, food_type)
    results = db_util.execute_query(query, params, True)

    if results:
        for i in results:
            print(f"{i['Food_id']}: {i['Food_name']} - Php {i['Food_price']} - {i['Food_item_type']}")
    else:
        print("\n\033[91mFailed to find any food item matching the given price range and food type. Please try again.\033[0m\n")
        return False