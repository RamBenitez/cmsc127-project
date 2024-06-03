from Database.connection import get_connection
from mysql.connector import Error

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
    FoodEstablishmentName = input("Enter Food Establishment Name: ")
    
    try:
        connection = get_connection()
        if connection is None:
            print("\033[91mConnection to database failed.\033[0m")
            return

        cursor = connection.cursor()
        insert_query = """
        INSERT INTO Food_Establishment (Food_establishment_name) 
        VALUES (%s)
        """
        cursor.execute(insert_query, (FoodEstablishmentName,))
        connection.commit()
        
        print("\033[92mSuccessfully Added!\033[0m")
    except Error as e:
        print(f"\033[91mError: {e}\033[0m")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def add_food_item():
    print("\n\033[1m\033[94m------ADD A FOOD ITEM------\033[0m")
    try:
        connection = get_connection()
        if connection is None:
            print("\033[91mConnection to database failed.\033[0m")
            return
        
        cursor = connection.cursor()
        cursor.execute("SELECT Food_establishment_id, Food_establishment_name FROM Food_Establishment")
        establishments = cursor.fetchall()
        
        print("List of Food Establishments:")
        for est in establishments:
            print(f"ID: {est[0]}, Name: {est[1]}")
            
        cursor.close()
    except Error as e:
        print(f"\033[91mError: {e}\033[0m")
        return
    finally:
        if connection.is_connected():
            connection.close()
            
    FoodItemEstablishmentID = input("Enter Food Establishment ID of where to add food: ")
    FoodItemName = input("Enter Food Name: ")
    FoodItemPrice = input("Enter Food Price: ")
    FoodItemCategory = input("Enter Food Category: ")

    try:
        connection = get_connection()
        if connection is None:
            print("\033[91mConnection to database failed.\033[0m")
            return

        cursor = connection.cursor()
        insert_query = """
        INSERT INTO Food_Item (Food_name, Food_price, Food_establishment_id) 
        VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (FoodItemName, FoodItemPrice, FoodItemEstablishmentID))
        connection.commit()
        

        Food_id = cursor.lastrowid
        
        # Insert the food item type
        insert_type_query = """
        INSERT INTO Food_Item_Type (Food_id, Food_item_type) 
        VALUES (%s, %s)
        """
        cursor.execute(insert_type_query, (Food_id, FoodItemCategory))
        connection.commit()

        print("\033[92mSuccessfully Added!\033[0m")
    except Error as e:
        print(f"\033[91mError: {e}\033[0m")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
