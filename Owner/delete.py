from Database.connection import get_connection
from mysql.connector import Error

def delete():
    while True:
        print("\n\033[1m\033[94m------DELETE MENU------\033[0m") 
        print("[1] Delete a food establishment")
        print("[2] Delete a food item")
        print("[3] Delete a food review")
        print("[4] Back")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            delete_food_establishment()
        elif choice == '2':
            delete_food_item()
        elif choice == '3':
            delete_food_review()
        elif choice == '4':
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")

def delete_food_establishment():
    print("\n\033[1m\033[94m------DELETE A FOOD ESTABLISHMENT------\033[0m")
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
    choice = input("Choice: ")
    try:
        connection = get_connection()
        if connection is None:
            print("\033[91mConnection to database failed.\033[0m")
            return
        
        cursor = connection.cursor()
        delete_query = "DELETE FROM Food_Establishment WHERE Food_establishment_id = %s"
        cursor.execute(delete_query, (choice,))
        connection.commit()
        print("\033[92mSuccessfully Deleted!\033[0m")
    except Error as e:
        print(f"\033[91mError: {e}\033[0m")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    print("\033[92mSuccessfully Deleted!\033[0m")

def delete_food_item():
    print("\n\033[1m\033[94m------DELETE A FOOD ITEM------\033[0m")
    print("List of all Food Establishments...")
    est_choice = input("Choice: ")
    try:
        connection = get_connection()
        if connection is None:
            print("\033[91mConnection to database failed.\033[0m")
            return
        
        cursor = connection.cursor()
        delete_query = "DELETE FROM Food_Establishment WHERE Food_establishment_id = %s"
        cursor.execute(delete_query, (choice,))
        connection.commit()
        print("\033[92mSuccessfully Deleted!\033[0m")
    except Error as e:
        print(f"\033[91mError: {e}\033[0m")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_food_review():
    print("\n\033[1m------DELETE A FOOD REVIEW------\033[0m")
    # Query to get all food reviews
    # Print all food reviews
    # Query to delete the selected food review
    # Delete the food review from the database
    print("\033[92mSuccessfully Deleted!\033[0m")
