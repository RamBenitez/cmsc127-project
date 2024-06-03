from Database.connection import get_connection
from Database import db_util


def add():
    while True:
        print("\n\033[1m\033[94m------ADD MENU------\033[0m") 
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
            print("\033[91mInvalid choice. Please try again.\033[0m")

def add_food_establishment():
    print("\n\033[1m\033[94m------ADD A FOOD ESTABLISHMENT------\033[0m")
    foodEstName = input("Enter Food Establishment Name: ")
    
    query = """
        INSERT INTO Food_Establishment (Food_establishment_name)
        VALUES (%s)
        """                                                     # Password() for encrpytion
    params = (foodEstName, ) 
    result = db_util.execute_query(query, params)
    if result:
        print("\n\033[92mSuccesfully added:\033[0m " + foodEstName + "\033[0m\n")
        return True
    else:
        print("\n\033[91mFailed to add food establishment. Please try again.\033[0m\n")
        return False

    # try:
    #     connection = get_connection()
    #     if connection is None:
    #         print("\033[91mConnection to database failed.\033[0m")
    #         return

    #     cursor = connection.cursor()
    #     insert_query = """
    #     INSERT INTO Food_Establishment (Food_establishment_name) 
    #     VALUES (%s)
    #     """
    #     cursor.execute(insert_query, (FoodEstablishmentName,))
    #     connection.commit()
        
    #     print("\033[92mSuccessfully Added!\033[0m")
    # except Error as e:
    #     print(f"\033[91mError: {e}\033[0m")
    # finally:
    #     if connection.is_connected():
    #         cursor.close()
    #         connection.close()
            
def add_food_item():
    print("\n\033[1m\033[94m------ADD A FOOD ITEM------\033[0m")
    selectAllFoodEst = "select * from Food_Establishment"
    resultAllFoodEst = db_util.execute_query(selectAllFoodEst, None, True)
    print("List of Food Establishments")
    for i in resultAllFoodEst:
        print(f"{i['Food_establishment_id']}: {i['Food_establishment_name']}")

    foodEstID = input("Enter Food Establishment ID of where to add food: ")
    foodName = input("Enter Food Name: ")
    foodPrice = input("Enter Food Price: ")
    foodCategory = input("Enter Food Category/ies (separated by comma ,): ")
    category_list = foodCategory.split(",")

    addFoodItem = """
        INSERT INTO Food_Item (Food_name, Food_price, Food_establishment_id)
        VALUES (%s, %s, %s)
    """                                                     
    addFoodItemParams = (foodName, foodPrice, foodEstID) 
    addFoodItemResult = db_util.execute_query(addFoodItem, addFoodItemParams)

    # Retrieve the last inserted ID
    getLastInsertId = "select max(Food_id) as Food_id from Food_Item"
    selectMaxFoodID_result = db_util.execute_query(getLastInsertId, None, True)
    foodID = selectMaxFoodID_result[0]['Food_id']

    addFoodItemType = """
        INSERT INTO Food_Item_Type (Food_id, Food_item_type)
        VALUES (%s, %s)
    """
    for category in category_list:
        addFoodItemTypeParams = (foodID, category.strip()) 
        db_util.execute_query(addFoodItemType, addFoodItemTypeParams)

    if addFoodItemResult:
        print("\n\033[92mFood item added successfully!\033[0m\n")
        return True
    else:
        print("\n\033[91mFailed to add food item. Please try again.\033[0m\n")
        return False

