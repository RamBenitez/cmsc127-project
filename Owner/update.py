from Database import db_util
from .reports import view_food_est, view_food_items_est


def update(username):
    while True:
        print("\n\033[1m\033[94m------UPDATE MENU------\033[0m") 
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
            print("\033[91mInvalid choice. Please try again.\033[0m")

def update_food_establishment():
    print("\n\033[1m\033[94m------UPDATE A FOOD ESTABLISHMENT------\033[0m")  

    # Print all food establishments
    view_food_est()

    print("Pick the ID of the food establishment you want to modify")
    choice = input("Choice: ")

    new_name = input("Enter New Food Establishment Name: ")
    query = "update Food_Establishment set Food_establishment_name=%s where Food_establishment_id=%s"                                               # Password() for encrpytion
    params = (new_name, choice) 
    result = db_util.execute_query(query, params)
    if result:
        print("\n\033[92mSuccesfully updated food establishment name to \033[0m\n" + new_name + "\033[0m\n")
        return True
    else:
        print("\n\033[91mFailed to update the food establishment name. Please try again.\033[0m\n")
        return False

def update_food_item():
    print("\n\033[1m\033[94m------UPDATE A FOOD ITEM------\033[0m")  
    # Query to get all food items of the selected food establishment
    # Print all food items
    view_food_items_est()

    print("Pick the ID of the food you want to modify")
    choice = input("Choice: ")
   
    new_name = input("Enter New Food Item Name: ")
    new_price = input("Enter New Food Item Price: ")
    new_category = input("Enter New Food Item Category: ")
    query = "update Food_Item set Food_name=%s, Food_price=%s where Food_id=%s"                                              
    params = (new_name, new_price, choice) 
    result = db_util.execute_query(query, params)

    # Query to delete all food types of food item in food item type
    delFoodTypes = "delete from Food_Item_Type where Food_id=%s"
    delFoodTypesParams = (choice, )
    db_util.execute_query(delFoodTypes, delFoodTypesParams)

    category_list = new_category.split(",")

    addFoodItemType = """
        INSERT INTO Food_Item_Type (Food_id, Food_item_type)
        VALUES (%s, %s)
    """
    for category in category_list:
        addFoodItemTypeParams = (choice, category.strip()) 
        db_util.execute_query(addFoodItemType, addFoodItemTypeParams)

    if result:
        print("\n\033[92mSuccesfully updated food information\033[0m\n")
        return True
    else:
        print("\n\033[91mFailed to update the food information. Please try again.\033[0m\n")
        return False
