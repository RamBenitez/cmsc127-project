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
    SELECT Food_review_id, Rating, Content
    FROM Food_Review
    WHERE Username = %s AND Food_id IS NOT NULL
    """
    params = (username, )
    food_reviews = db_util.execute_query(query, params, fetch=True)
    
    if not food_reviews:
        print("\n\033[91mNo food reviews available to update.\033[0m\n")
        return
    
    print("CUSTOMER'S FOOD ITEM REVIEWS....")
    for review in food_reviews:
        print(f"Review ID: {review['Food_review_id']}, Rating: {review['Rating']}, Content: {review['Content']}")
    # Customer selects a review to update
    review_choice = input("\nChoice: ")
    new_rating = input("New Rating (1-5): ")
    new_content = input("Content: ")
    # Update the review in the database
    print("\n\033[92mSuccessfully updated review!\033[0m\n")

# Update review of a food establishment
def update_food_establishment_review(username):
    food_establishment_reviews = 0
    print("\n\033[1m\033[94m-----UPDATE FOOD ESTABLISHMENT REVIEW-----\033[0m")
    # Query to show all the customer's food establishment reviews

    if not food_establishment_reviews:
        print("\n\033[91mNo food reviews available to update.\033[0m\n")
        return
    
    print("CUSTOMER'S FOOD ESTABLISHMENT REVIEWS....")
    # Customer selects a review to update
    review_choice = input("\nChoice: ")
    new_rating = input("New Rating (1-5): ")
    new_content = input("Content: ")
    # Update the review in the database
    print("\n\033[92mSuccessfully updated review!\033[0m\n")
