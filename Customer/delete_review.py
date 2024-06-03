from Database import db_util

def delete_review(username):
    while True:
        print("\n\033[1m\033[94m------DELETE REVIEW MENU------\033[0m")
        print("[1] Delete a review on a food item")
        print("[2] Delete a review on a food establishment")
        print("[3] Back")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            delete_food_review(username)
        elif choice == '2':
            delete_food_establishment_review(username)
        elif choice == '3':
            break
        else:
            print("\n\033[91mInvalid choice. Please try again.\033[0m")

# Delete review of a food item
def delete_food_review(username):
    print("\n\033[1m\033[94m-----DELETE FOOD REVIEW-----\033[0m")

    query = """
    SELECT Food_review_id, Food_name, Rating, Content, Date 
    FROM Food_Review fr
    JOIN Food_Item fi ON fr.Food_id = fi.Food_id
    WHERE Username = %s AND fr.Food_id IS NOT NULL
    """
    params = (username,)
    reviews = db_util.execute_query(query, params, fetch=True)
    
    if not reviews:
        print("\n\033[91mNo food item reviews found.\033[0m\n")
        return
    
    print("List of your reviews:")
    for review in reviews:
        print(f"Food review id: {review['Food_review_id']}, Food Name: {review['Food_name']}, Rating: {review['Rating']}, Content: {review['Content']}, Date: {review['Date']}")
    # Customer selects a review to delete
    review_choice = input("\nEnter the Review ID to delete: ")

    # Delete the review from the database
    delete_query = "DELETE FROM Food_Review WHERE Food_review_id = %s AND Username = %s"
    delete_params = (review_choice, username)
    result = db_util.execute_query(delete_query, delete_params)

    if result:
        print("\n\033[92mSuccessfully deleted review of the food item!\033[0m\n")
    else:
        print("\n\033[91mFailed to delete review. Please try again.\033[0m\n")

# Delete review of a food establishment
def delete_food_establishment_review(username):
    print("\n\033[1m\033[94m-----DELETE FOOD ESTABLISHMENT REVIEW-----\033[0m")
    # Query to show all the customer's food establishment reviews
    print("CUSTOMER'S FOOD ESTABLISHMENT REVIEWS....")
    # Customer selects a review to delete
    review_choice = input("\nChoice: ")
    # Delete the review from the database
    print("\n\033[92mSuccessfully deleted review of <food establishment>!\033[0m\n")
