from Database import db_util

def add_review():
    while True:
        print("\n\033[1m\033[94m------ADD REVIEW MENU------\033[0m")
        print("[1] Add a review on a food item")
        print("[2] Add a review on a food establishment")
        print("[3] Back")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_food_review()
        elif choice == '2':
            add_food_establishment_review()
        elif choice == '3':
            break
        else:
            print("\n\033[91mInvalid choice. Please try again.\033[0m")

#Add food review on a food item
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
    
    food_item_id = input("\nEnter the Food Item ID: ")
    food_establishment_id = input("Enter the Food Establishment ID: ")
    rating = int(input("Rating (1-5): "))
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

 #add a food establishment review   
def add_food_establishment_review():
    print("\n\033[1m\033[94m-----ADD FOOD  ESTABLISHMENT REVIEW-----\033[0m")
    #QUery to show  all the food establishments
    print("FOOD ESTABLISHMENTS....")
    FoodEstablishmentChoice = input("\nChoice: ")
    EstablishmentRating= input("Rating (1-5):")
    EstablishmentContent= input("Review: ")
    print("\n\033[92mSuccessully added review of <FOOD ESTABLISHMENT>\033[0m\n")
    