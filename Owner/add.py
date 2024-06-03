from Database.connection import get_connection
from Database import db_util


def add(username):
    while True:
        print("\n\033[1m\033[94m------ADD MENU------\033[0m") 
        print("[1] Add a food establishment")
        print("[2] Add a food item")
        print("[3] Back")
        
        choice = input("\nEnter your choice: ")
        if choice == '1':
            add_food_establishment(username)
        elif choice == '2':
            add_food_item(username)
        elif choice == '3':
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")

def add_food_establishment(username):
    print("\n\033[1m\033[94m------ADD A FOOD ESTABLISHMENT------\033[0m")
    foodEstName = input("Enter Food Establishment Name: ")
    
    query = """
        INSERT INTO Food_Establishment (Food_establishment_name)
        VALUES (%s)
    """
    params = (foodEstName,) 
    result = db_util.execute_query(query, params)
    
    if result:
        print("\n\033[92mSuccessfully added:\033[0m " + foodEstName + "\033[0m\n")
        
        # Retrieve the max inserted ID
        getMaxEstID = "SELECT MAX(Food_establishment_id) AS Food_establishment_id FROM Food_Establishment"
        selectMaxEstID_result = db_util.execute_query(getMaxEstID, None, fetch=True)
        foodEstID = selectMaxEstID_result[0]['Food_establishment_id']
        
        # Insert into Creates table
        addCreates = """
            INSERT INTO Creates (Username, Food_establishment_id, Food_id)
            VALUES (%s, %s, NULL)
        """
        addCreatesParams = (username, foodEstID)
        resultCreates = db_util.execute_query(addCreates, addCreatesParams)
        
        if resultCreates:
            print("\n\033[92mSuccessfully added entry to Creates table!\033[0m\n")
            return True
        else:
            print("\n\033[91mFailed to add entry to Creates table. Please try again.\033[0m\n")
            return False
    else:
        print("\n\033[91mFailed to add food establishment. Please try again.\033[0m\n")
        return False

            
def add_food_item(username):
    print("\n\033[1m\033[94m------ADD A FOOD ITEM------\033[0m")
    selectAllFoodEst = "SELECT * FROM Food_Establishment"
    resultAllFoodEst = db_util.execute_query(selectAllFoodEst, fetch=True)
    print("List of Food Establishments")
    for i in resultAllFoodEst:
        print(f"{i['Food_establishment_id']}: {i['Food_establishment_name']}")

    foodEstID = input("Enter Food Establishment ID of where to add food: ")
    
    # Validate Food Establishment ID
    valid_food_est_query = "SELECT * FROM Food_Establishment WHERE Food_establishment_id = %s"
    valid_food_est = db_util.execute_query(valid_food_est_query, (foodEstID,), fetch=True)
    if not valid_food_est:
        print("\n\033[91mInvalid Food Establishment ID. Please try again.\033[0m\n")
        return False

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

    if not addFoodItemResult:
        print("\n\033[91mFailed to add food item. Please try again.\033[0m\n")
        return False

    # Retrieve the max inserted ID
    getMaxFoodID = "SELECT MAX(Food_id) AS Food_id FROM Food_Item"
    selectMaxFoodID_result = db_util.execute_query(getMaxFoodID, None, fetch=True)
    foodID = selectMaxFoodID_result[0]['Food_id']

    addFoodItemType = """
        INSERT INTO Food_Item_Type (Food_id, Food_item_type)
        VALUES (%s, %s)
    """
    for category in category_list:
        addFoodItemTypeParams = (foodID, category.strip()) 
        db_util.execute_query(addFoodItemType, addFoodItemTypeParams)
    
    # Insert into Creates table
    addCreates = """
        INSERT INTO Creates (Username, Food_establishment_id, Food_id)
        VALUES (%s, %s, %s)
    """
    addCreatesParams = (username, foodEstID, foodID)
    resultCreates = db_util.execute_query(addCreates, addCreatesParams)

    if resultCreates:
        print("\n\033[92mFood item added successfully!\033[0m\n")
        return True
    else:
        print("\n\033[91mFailed to add food item. Please try again.\033[0m\n")
        return False

