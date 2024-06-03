from Database import db_util

def delete(username):
    while True:
        print("\n\033[1m\033[94m------DELETE MENU------\033[0m") 
        print("[1] Delete a food establishment")
        print("[2] Delete a food item")
        print("[3] Back")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            delete_food_establishment(username)
        elif choice == '2':
            delete_food_item(username)
        elif choice == '3':
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")

def delete_food_establishment(username):
    print("\n\033[1m\033[94m------DELETE A FOOD ESTABLISHMENT------\033[0m")  
    selectAllFoodEst = """
        SELECT fe.Food_establishment_id, fe.Food_establishment_name 
        FROM Food_Establishment fe
        JOIN Creates c ON fe.Food_establishment_id = c.Food_establishment_id
        WHERE c.Username = %s AND c.Food_id IS NULL
    """
    resultAllFoodEst = db_util.execute_query(selectAllFoodEst, (username,), fetch=True)
    
    if not resultAllFoodEst:
        print("\n\033[91mNo food establishments found or you don't have permission to delete any food establishment.\033[0m\n")
        return

    print("List of Food Establishments")
    for i in resultAllFoodEst:
        print(f"{i['Food_establishment_id']}: {i['Food_establishment_name']}")

    print("\nPick the Food Establishment ID you want to delete.")
    foodEstID = int(input("Choice: "))

    # Check if the user has permission to delete this food establishment
    if not any(fe['Food_establishment_id'] == foodEstID for fe in resultAllFoodEst):
        print("\n\033[91mYou do not have permission to delete this food establishment.\033[0m\n")
        return False

    # Delete associated food items and their entries in Creates and Food_Item_Type tables
    selectAllFoodItems = "SELECT Food_id FROM Food_Item WHERE Food_establishment_id=%s"
    selectAllFoodItemsParams = (foodEstID,)
    resultAllFoodItems = db_util.execute_query(selectAllFoodItems, selectAllFoodItemsParams, fetch=True)
    
    if resultAllFoodItems:
        for foodItem in resultAllFoodItems:
            foodID = foodItem['Food_id']

            # Delete from Food_Item_Type
            delFoodTypes = "DELETE FROM Food_Item_Type WHERE Food_id=%s"
            delFoodTypesParams = (foodID,)
            db_util.execute_query(delFoodTypes, delFoodTypesParams)

            # Delete from Creates
            delCreates = "DELETE FROM Creates WHERE Food_id=%s"
            delCreatesParams = (foodID,)
            db_util.execute_query(delCreates, delCreatesParams)

            # Delete the food item
            delFoodItem = "DELETE FROM Food_Item WHERE Food_id=%s"
            delFoodItemParams = (foodID,)
            db_util.execute_query(delFoodItem, delFoodItemParams)

    # Delete entries in Creates for the food establishment
    delCreatesEst = "DELETE FROM Creates WHERE Food_establishment_id=%s AND Username=%s"
    delCreatesEstParams = (foodEstID, username)
    db_util.execute_query(delCreatesEst, delCreatesEstParams)

    # Delete the food establishment
    delFoodEst = "DELETE FROM Food_Establishment WHERE Food_establishment_id=%s"
    delFoodEstParams = (foodEstID,)
    delFoodEstResult = db_util.execute_query(delFoodEst, delFoodEstParams)

    if delFoodEstResult:
        print("\n\033[92mFood establishment successfully deleted!\033[0m\n")
        return True
    else:
        print("\n\033[91mFailed to delete food establishment. Please try again.\033[0m\n")
        return False

def delete_food_item(username):
    print("\n\033[1m\033[94m------DELETE A FOOD ITEM------\033[0m")
    selectAllFoodEst = """
        SELECT fe.Food_establishment_id, fe.Food_establishment_name 
        FROM Food_Establishment fe
        JOIN Creates c ON fe.Food_establishment_id = c.Food_establishment_id
        WHERE c.Username = %s AND c.Food_id IS NULL
    """
    resultAllFoodEst = db_util.execute_query(selectAllFoodEst, (username,), fetch=True)
    
    if not resultAllFoodEst:
        print("\n\033[91mNo food establishments found or you don't have permission to delete any food items.\033[0m\n")
        return

    print("List of Food Establishments")
    for i in resultAllFoodEst:
        print(f"{i['Food_establishment_id']}: {i['Food_establishment_name']}")

    print("Pick the Food Establishment ID you want to delete.")
    foodEstID = int(input("Choice: "))

    # Check if the user has permission to delete items from this food establishment
    if not any(fe['Food_establishment_id'] == foodEstID for fe in resultAllFoodEst):
        print("\n\033[91mYou do not have permission to delete items from this food establishment.\033[0m\n")
        return False

    selectFoodEstName = "SELECT Food_establishment_name FROM Food_Establishment WHERE Food_establishment_id = %s"
    selectFoodEstNameParams = (foodEstID,)
    resultselectFoodEstName = db_util.execute_query(selectFoodEstName, selectFoodEstNameParams, fetch=True)
    if resultselectFoodEstName:
        foodEstName = resultselectFoodEstName[0]['Food_establishment_name']
    
    # Query to get all food items of the selected food establishment
    selectAllFoodItems = """
        SELECT fi.Food_id, fi.Food_name
        FROM Food_Item fi
        JOIN Creates c ON fi.Food_id = c.Food_id
        WHERE fi.Food_establishment_id=%s AND c.Username=%s
    """
    selectAllFoodItemsParams = (foodEstID, username)
    resultAllFoodItems = db_util.execute_query(selectAllFoodItems, selectAllFoodItemsParams, fetch=True)
    
    if not resultAllFoodItems:
        print("\n\033[91mNo food items found or you don't have permission to delete any food items.\033[0m\n")
        return

    # Print all food items
    print("\nList of Food Items in " + foodEstName)
    for i in resultAllFoodItems:
        print(f"{i['Food_id']}: {i['Food_name']}")

    print("\nPick the Food ID you want to delete.")
    foodID = int(input("Choice: "))

    # Check if the user has permission to delete this food item
    if not any(fi['Food_id'] == foodID for fi in resultAllFoodItems):
        print("\n\033[91mYou do not have permission to delete this food item.\033[0m\n")
        return False

    # Query to delete all food types of food item in food item type
    delFoodTypes = "DELETE FROM Food_Item_Type WHERE Food_id=%s"
    delFoodTypesParams = (foodID,)
    db_util.execute_query(delFoodTypes, delFoodTypesParams)

    # Delete corresponding entries in the Creates table
    delCreates = "DELETE FROM Creates WHERE Food_id=%s"
    delCreatesParams = (foodID,)
    db_util.execute_query(delCreates, delCreatesParams)

    # Query to delete the selected food item
    delFoodItem = "DELETE FROM Food_Item WHERE Food_id=%s AND Food_establishment_id=%s"
    delFoodItemParams = (foodID, foodEstID)
    delFoodItemResult = db_util.execute_query(delFoodItem, delFoodItemParams)

    # Delete the food item from the database
    if delFoodItemResult:
        print("\n\033[92mFood item has been successfully deleted!\033[0m\n")
        return True
    else:
        print("\n\033[91mFailed to delete food item. Please try again.\033[0m\n")
        return False

