from Database import db_util

def update_review(username):
    while True:
        print("\n\033[1m\033[94m------UPDATE REVIEW MENU------\033[0m")
        print("[1] Update a review on a food item")
        print("[2] Update a review on a food establishment")
        print("[3] Back")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            update_food_review(username)
        elif choice == '2':
            update_food_establishment_review(username)
        elif choice == '3':
            break
        else:
            print("\n\033[91mInvalid choice. Please try again.\033[0m")

# Update review of a food item
def update_food_review(username):
    print("\n\033[1m\033[94m-----UPDATE FOOD REVIEW-----\033[0m")
    
    # Query to show all the customer's food item reviews
    query = """
    SELECT Food_review_id, Food_name, Rating, Content, Date 
    FROM Food_Review fr
    JOIN Food_Item fi ON fr.Food_id = fi.Food_id
    WHERE Username = %s AND fr.Food_id IS NOT NULL
    """
    params = (username,)
    food_reviews = db_util.execute_query(query, params, fetch=True)
    
    if not food_reviews:
        print("\n\033[91mNo food reviews available to update.\033[0m\n")
        return
    
    print("CUSTOMER'S FOOD ITEM REVIEWS:")
    for review in food_reviews:
        print(f"Review ID: {review['Food_review_id']}, Food Name: {review['Food_name']}, Rating: {review['Rating']}, Content: {review['Content']}, Date: {review['Date']}")
    
    # Customer selects a review to update
    review_choice = input("\nEnter the Review ID to update: ")
    new_rating = input("New Rating (1-5): ")
    new_content = input("New Content: ")

    # Update the review in the database
    update_query = """
    UPDATE Food_Review
    SET Rating = %s, Content = %s, Date = CURDATE()
    WHERE Food_review_id = %s AND Username = %s
    """
    update_params = (new_rating, new_content, review_choice, username)
    result = db_util.execute_query(update_query, update_params)

    if result:
        print("\n\033[92mSuccessfully updated review of the food item!\033[0m\n")
    else:
        print("\n\033[91mFailed to update review. Please try again.\033[0m\n")

# Update review of a food establishment
def update_food_establishment_review(username):
    print("\n\033[1m\033[94m-----UPDATE FOOD ESTABLISHMENT REVIEW-----\033[0m")
    
    # Query to show all the customer's food establishment reviews

    query = """
    SELECT Food_review_id, Food_establishment_name, Rating, Content, Date 
    FROM Food_Review fr
    JOIN Food_Establishment fe ON fr.Food_establishment_id = fe.Food_establishment_id
    WHERE Username = %s AND fr.Food_establishment_id IS NOT NULL AND Food_id IS NULL
    """
    params = (username,)
    food_establishment_reviews = db_util.execute_query(query, params, fetch=True)

    if not food_establishment_reviews:
        print("\n\033[91mNo food reviews available to update.\033[0m\n")
        return
    
    print("CUSTOMER'S FOOD ESTABLISHMENT REVIEWS:")
    for review in food_establishment_reviews:
        print(f"Review ID: {review['Food_review_id']}, Establishment Name: {review['Food_establishment_name']}, Rating: {review['Rating']}, Content: {review['Content']}, Date: {review['Date']}")
    
    # Customer selects a review to update
    review_choice = input("\nEnter the Review ID to update: ")
    new_rating = input("New Rating (1-5): ")
    new_content = input("New Content: ")

    # Update the review in the database
    update_query = """
    UPDATE Food_Review
    SET Rating = %s, Content = %s, Date = CURDATE()
    WHERE Food_review_id = %s AND Username = %s
    """
    update_params = (new_rating, new_content, review_choice, username)
    result = db_util.execute_query(update_query, update_params)

    if result:
        print("\n\033[92mSuccessfully updated review of the food establishment!\033[0m\n")
    else:
        print("\n\033[91mFailed to update review. Please try again.\033[0m\n")
