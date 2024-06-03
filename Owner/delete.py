
from Database import db_util

def delete():
    while True:
        print("\n\033[1m\033[94m------DELETE MENU------\033[0m") 
        print("[1] Delete a food establishment")
        print("[2] Delete a food item")
        print("[3] Back")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            delete_food_establishment()
        elif choice == '2':
            delete_food_item()
        elif choice == '3':
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")

def delete_food_establishment():
    print("\n\033[1m\033[94m------DELETE A FOOD ESTABLISHMENT------\033[0m")  
    selectAllFoodEst = "select * from Food_Establishment"
    resultAllFoodEst = db_util.execute_query(selectAllFoodEst, None, True)
    print("List of Food Establishments")
    for i in resultAllFoodEst:
        print(f"{i['Food_establishment_id']}: {i['Food_establishment_name']}")

    print("\nPick the Food Establishment ID you want to delete.")
    foodEstID = int(input("Choice: "))

    # Query to delete the selected food establishment
    delFoodEst = "delete from Food_Establishment where Food_establishment_id=%s"                                                  
    delFoodEstParams = (foodEstID, ) 

    # Delete the food establishment from the database
    delFoodEstResult = db_util.execute_query(delFoodEst, delFoodEstParams)

    if delFoodEstResult:
        print("\n\033[92mFood establishment successfully deleted!\033[0m\n")
        return True
    else:
        print("\n\033[91mFailed to delete food establishment. Please try again.\033[0m\n")
        return False

def delete_food_item():
    print("\n\033[1m\033[94m------DELETE A FOOD ITEM------\033[0m")
    selectAllFoodEst = "select * from Food_Establishment"
    resultAllFoodEst = db_util.execute_query(selectAllFoodEst, None, True)
    print("List of Food Establishments")
    for i in resultAllFoodEst:
        print(f"{i['Food_establishment_id']}: {i['Food_establishment_name']}")

    print("Pick the Food Establishment ID you want to delete.")
    foodEstID = int(input("Choice: "))

    selectFoodEstName = "SELECT Food_establishment_name FROM Food_Establishment WHERE Food_establishment_id = %s"
    selectFoodEstNameParams = (foodEstID,)
    resultselectFoodEstName = db_util.execute_query(selectFoodEstName, selectFoodEstNameParams, True)
    if resultselectFoodEstName:
        foodEstName =  resultselectFoodEstName[0]['Food_establishment_name']
    
    # Query to get all food items of the selected food establishment
    selectAllFoodItems = "select * from Food_Establishment natural join Food_Item where Food_establishment_id=%s"
    selectAllFoodItemsParams = (foodEstID, )
    resultAllFoodItems = db_util.execute_query(selectAllFoodItems, selectAllFoodItemsParams, True)
    
    # Print all food items
    print("\nList of Food Items in "+ foodEstName)
    for i in resultAllFoodItems:
        print(f"{i['Food_id']}: {i['Food_name']}")

    print("\nPick the Food ID you want to delete.")
    foodID = int(input("Choice: "))

    # Query to delete all food types of food item in food item type
    delFoodTypes = "delete from Food_Item_Type where Food_id=%s"
    delFoodTypesParams = (foodID, )
    db_util.execute_query(delFoodTypes, delFoodTypesParams)

    # Query to delete the selected food item
    delFoodItem = "delete from Food_Item where Food_id=%s and Food_establishment_id=%s"
    delFoodItemParams = (foodID, foodEstID) 
    delFoodItemResult = db_util.execute_query(delFoodItem, delFoodItemParams)

    # Delete the food item from the database
    if delFoodItemResult:
        print("\n\033[92mFood item has been successfully deleted!\033[0m\n")
        return True
    else:
        print("\n\033[91mFailed to delete food item. Please try again.\033[0m\n")
        return False


   