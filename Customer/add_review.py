from Database import db_util

def add_review(username):
    while True:
        print("\n\033[1m\033[94m------ADD REVIEW MENU------\033[0m")
        print("[1] Add a review on a food item")
        print("[2] Add a review on a food establishment")
        print("[3] Back")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_food_review(username)
        elif choice == '2':
            add_food_establishment_review(username)
        elif choice == '3':
            break
        else:
            print("\n\033[91mInvalid choice. Please try again.\033[0m")

def get_valid_rating():
    while True:
        try:
            rating = int(input("New Rating (1-5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("\n\033[91mInvalid rating. Please enter a value between 1 and 5.\033[0m")
        except ValueError:
            print("\n\033[91mInvalid input. Please enter a number between 1 and 5.\033[0m")

# Add food review on a food item
def add_food_review(username):
    print("\n\033[1m\033[94m-----ADD FOOD REVIEW-----\033[0m")
    
    # Query to show all the food items along with their food establishments
    query = """
    SELECT fi.Food_id, fi.Food_name, fe.Food_establishment_id, fe.Food_establishment_name
    FROM Food_Item fi
    JOIN Food_Establishment fe ON fi.Food_establishment_id = fe.Food_establishment_id
    """
    food_items = db_util.execute_query(query, fetch=True)
    
    print("List of Food Items:")
    for item in food_items:
        print(f"Food ID: {item['Food_id']}, Food Name: {item['Food_name']}, Establishment ID: {item['Food_establishment_id']}, Establishment Name: {item['Food_establishment_name']}")
    
    if not food_items:
            print("\n\033[91mNo food items available to review.\033[0m\n")
            return

    while True:
        food_item_id = input("\nEnter the Food Item ID: ")
        # Check if the food item ID is valid
        valid_food_item_query = "SELECT Food_id FROM Food_Item WHERE Food_id = %s"
        valid_food_item = db_util.execute_query(valid_food_item_query, (food_item_id,), fetch=True)
        if valid_food_item:
            break
        else:
            print("\n\033[91mInvalid Food Item ID. Please try again.\033[0m")
    
    while True:
        food_establishment_id = input("Enter the Food Establishment ID: ")
        # Check if the food establishment ID is valid
        valid_food_establishment_query = "SELECT Food_establishment_id FROM Food_Establishment WHERE Food_establishment_id = %s"
        valid_food_establishment = db_util.execute_query(valid_food_establishment_query, (food_establishment_id,), fetch=True)
        if valid_food_establishment:
            break
        else:
            print("\n\033[91mInvalid Food Establishment ID. Please try again.\033[0m")

    rating = get_valid_rating()
    content = input("Review: ")

    # Insert the review into Food_Review table
    query = """
    INSERT INTO Food_Review (Rating, Content, Date, Username, Food_id, Food_establishment_id)
    VALUES (%s, %s, CURDATE(), %s, %s, %s)
    """
    params = (rating, content, username, food_item_id, food_establishment_id)  # Replace 'username_placeholder' with actual username
    result = db_util.execute_query(query, params)

    if result:
        print("\n\033[92mSuccessfully added review of the food item.\033[0m\n")
    else:
        print("\n\033[91mFailed to add review. Please try again.\033[0m\n")

# Add a review on a food establishment   
def add_food_establishment_review(username):
    print("\n\033[1m\033[94m-----ADD FOOD ESTABLISHMENT REVIEW-----\033[0m")
    # Query to show all the food establishments
    query = "SELECT Food_establishment_id, Food_establishment_name FROM Food_Establishment"
    food_establishments = db_util.execute_query(query, fetch=True)
    
    print("List of Food Establishments:")
    for establishment in food_establishments:
        print(f"{establishment['Food_establishment_id']}: {establishment['Food_establishment_name']}")
    
    if not food_establishments:
            print("\n\033[91mNo food establishments available to review.\033[0m\n")
            return

    while True:
        food_establishment_id = input("\nEnter the Food Establishment ID: ")
        # Check if the food establishment ID is valid
        valid_food_establishment_query = "SELECT Food_establishment_id FROM Food_Establishment WHERE Food_establishment_id = %s"
        valid_food_establishment = db_util.execute_query(valid_food_establishment_query, (food_establishment_id,), fetch=True)
        if valid_food_establishment:
            break
        else:
            print("\n\033[91mInvalid Food Establishment ID. Please try again.\033[0m")
            
    rating = get_valid_rating()
    content = input("Review: ")

    # Insert the review into Food_Review table
    query = """
    INSERT INTO Food_Review (Rating, Content, Date, Username, Food_establishment_id)
    VALUES (%s, %s, CURDATE(), %s, %s)
    """
    params = (rating, content, username, food_establishment_id, )
    result = db_util.execute_query(query, params)

    if result:
        print("\n\033[92mSuccessfully added review of the food establishment.\033[0m\n")
    else:
        print("\n\033[91mFailed to add review. Please try again.\033[0m\n")
    