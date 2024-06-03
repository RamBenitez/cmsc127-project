from Database import db_util

def reports():
    while True:
        print("\n\033[1m\033[94m------REPORTS MENU------\033[0m") 
        print("[1] View all food establishments")
        print("[2] View all food items from an establishment")
        print("[3] View all food reviews for an establishment")
        print("[4] View all food reviews for a food item")
        print("[5] View all food items from an establishment that belong to a food type")
        print("[6] View all reviews made within a month for an establishment")
        print("[7] View all reviews made within a month for a food item")
        print("[8] View all establishments with a high average rating (rating >= 4)")
        print("[9] View all food items from an establishment arranged according to price ")
        print("[10] Back")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            view_food_est()
        elif choice == '2':
            view_food_items_est()
        elif choice == '3':
            view_food_reviews_est()
        elif choice == '4':
            view_food_review_item()
        elif choice == '5':
            view_food_items_type_est()
        elif choice == '6':
            view_food_reviews_est_month()
        elif choice == '7':
            view_food_reviews_item_month()
        elif choice == '8':
            view_food_est_high_ave()
        elif choice == '9':
            view_food_items_est_price()
        elif choice == '10':
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")

def view_food_est():
    print("\n\033[1m\033[94m------VIEW ALL FOOD ESTABLISHMENTS------\033[0m")  
    selectAllFoodEst = "select * from Food_Establishment"
    resultAllFoodEst = db_util.execute_query(selectAllFoodEst, None, True)

    for i in resultAllFoodEst:
        print(f"{i['Food_establishment_id']}: {i['Food_establishment_name']}")

def view_food_items_est():
    print("\n\033[1m\033[94m------VIEW ALL FOOD ITEMS FROM ESTABLISHMENT------\033[0m")  
    view_food_est()

    print("\nPick the Food Establishment ID you want to view")
    foodEstID = int(input("Choice: "))

    # Query to delete the selected food establishment
    selectAllFoodItems = "select * from Food_Establishment natural join Food_Item where Food_establishment_id=%s"
    selectAllFoodItemsParams = (foodEstID, )
    resultAllFoodItems = db_util.execute_query(selectAllFoodItems, selectAllFoodItemsParams, True)

    for i in resultAllFoodItems:
        print(f"{i['Food_id']}: {i['Food_name']} - Php {i['Food_price']}")

def view_food_reviews_est():
    print("\n\033[1m\033[94m------VIEW ALL FOOD REVIEWS FROM ESTABLISHMENT------\033[0m") 
    view_food_est()

    print("\nPick the Food Establishment ID you want to view food reviews from")
    foodEstID = int(input("Choice: ")) 

    selectReviews = "select * from Food_Review where Food_establishment_id=%s"
    selectReviewsParams = (foodEstID, )
    resultSelectReviews = db_util.execute_query(selectReviews, selectReviewsParams, True)

    if resultSelectReviews:
        print("\nList of food reviews")
        for i in resultSelectReviews:
            print(f"{i['Food_review_id']}: Review by {i['Username']}\nRating: {i['Rating']}/5\nDesc: {i['Content']}")
    else:
        print("\n\033[91mFailed to fetch food reviews of food establishment. Please try again.\033[0m\n")
        return False

def view_food_review_item():
    print("\n\033[1m\033[94m------VIEW ALL FOOD REVIEWS FROM ESTABLISHMENT------\033[0m") 
    view_food_items_est()

    print("\nPick the Food ID of the food item you want to view reviews of")
    foodID = int(input("Choice: ")) 
    
    selectReviews = "select * from Food_Review where Food_id=%s"
    selectReviewsParams = (foodID, )
    resultSelectReviews = db_util.execute_query(selectReviews, selectReviewsParams, True)

    if resultSelectReviews:
        print("\nList of food reviews")
        for i in resultSelectReviews:
            print(f"{i['Food_review_id']}: Review by {i['Username']}\nRating: {i['Rating']}/5\nDesc: {i['Content']}")
    else:
        print("\n\033[91mFailed to fetch food reviews of food item. Please try again.\033[0m\n")
        return False


def view_food_items_type_est():
    print("\n\033[1m\033[94m------VIEW ALL FOOD ITEMS WITH SPECIFIED TYPE------\033[0m") 
    view_food_est()

    print("\nPick the Food Establishment ID of the food items you want to view")
    foodEstID = int(input("Choice: ")) 
    foodType = input("Specify food type: ")
    
    selectFoodItemsType = "select * from Food_Item natural join Food_Item_Type where Food_establishment_id=%s and Food_item_type=%s"
    selectFoodItemsTypeParams = (foodEstID, foodType)
    resultselectFoodItemsType = db_util.execute_query(selectFoodItemsType, selectFoodItemsTypeParams, True)
    if resultselectFoodItemsType:
        print("\nList of food items with Food Type ("+ foodType +")")
        for i in resultselectFoodItemsType:
            print(f"{i['Food_id']}: {i['Food_name']} - {i['Food_item_type']}"),
    else:
        print("\n\033[91mFailed to fetch food items with food type specified. Please try again.\033[0m\n")
        return False

def view_food_reviews_est_month():
    print("\n\033[1m\033[94m------VIEW ALL FOOD REVIEWS FOR FOOD ESTABLISHMENT MADE WITHIN A MONTH------\033[0m")
    view_food_est()
    print("\nPick the Food Establishment ID of the food reviews you want to view")
    foodEstID = int(input("Choice: ")) 

    while True:
        month = int(input("Month (1-12): "))
        if 1 <= month <= 12:
            break 
        else:
            print("Invalid month. Please try again.")

    if month == 1:
        mon = "January"
    elif month == 2:
        mon = "February"
    elif month == 3:
        mon = "March"
    elif month == 4:
        mon = "April"
    elif month == 5:
        mon = "May"
    elif month == 6:
        mon = "June"
    elif month == 7:
        mon = "July"
    elif month == 8:
        mon = "August"
    elif month == 9:
        mon = "September"
    elif month == 10:
        mon = "October"
    elif month == 11:
        mon = "November"
    elif month == 12:
        mon = "December"

    selectMonth = "select * from Food_Review where Food_establishment_id=%s and Date like '2024-%s-__'"
    selectMonthParams = (foodEstID, month)
    resultSelectMonth = db_util.execute_query(selectMonth, selectMonthParams, True)

    if resultSelectMonth:
        print("\nList of food reviews made within the month of ("+ mon +")")
        for i in resultSelectMonth:
            print(f"{i['Food_review_id']}: Review by {i['Username']}\nRating: {i['Rating']}/5\nDesc: {i['Content']}")
    else:
        print("\n\033[91mFailed to fetch food reviews on specified month. Please try again.\033[0m\n")
        return False

def view_food_reviews_item_month():
    print("\n\033[1m\033[94m------VIEW ALL FOOD REVIEWS FOR FOOD ITEM MADE WITHIN A MONTH------\033[0m")
    view_food_items_est()
    print("\nPick the Food ID you want see food reviews of")
    foodItemID = int(input("Choice: ")) 

    while True:
        month = int(input("Month (1-12): "))
        if 1 <= month <= 12:
            break 
        else:
            print("Invalid month. Please try again.")

    if month == 1:
        mon = "January"
    elif month == 2:
        mon = "February"
    elif month == 3:
        mon = "March"
    elif month == 4:
        mon = "April"
    elif month == 5:
        mon = "May"
    elif month == 6:
        mon = "June"
    elif month == 7:
        mon = "July"
    elif month == 8:
        mon = "August"
    elif month == 9:
        mon = "September"
    elif month == 10:
        mon = "October"
    elif month == 11:
        mon = "November"
    elif month == 12:
        mon = "December"

    selectMonth = "select * from Food_Review where Food_id=%s and Date like '2024-%s-__'"
    selectMonthParams = (foodItemID, month)
    resultSelectMonth = db_util.execute_query(selectMonth, selectMonthParams, True)

    if resultSelectMonth:
        print("\nList of food reviews made within the month of ("+ mon +")")
        for i in resultSelectMonth:
            print(f"{i['Food_review_id']}: Review by {i['Username']}\nRating: {i['Rating']}/5\nDesc: {i['Content']}")
    else:
        print("\n\033[91mFailed to fetch food reviews on specified month. Please try again.\033[0m\n")
        return False

def view_food_est_high_ave():
    print("\n\033[1m\033[94m------VIEW ALL FOOD ESTABLISHMENTS WITH A HIGH AVERAGE RATING (4+)------\033[0m") 
    selectHighAve = """SELECT fe.Food_establishment_id,
    fe.Food_establishment_name,
    AVG(fer.Food_establishment_rating) AS average_rating
    FROM Food_Establishment fe
    NATURAL JOIN Food_Establishment_Rating fer
    GROUP BY fe.Food_establishment_id, fe.Food_establishment_name
    HAVING AVG(fer.Food_establishment_rating) >= 4.0;
    """
    resultHighAve = db_util.execute_query(selectHighAve, None, True)
    if resultHighAve:
        for i in resultHighAve:
            print(f"{i['Food_establishment_id']}: {i['Food_establishment_name']} - {i['average_rating']}")
    else:
        print("\n\033[91mFailed to add food item. Please try again.\033[0m\n")
        return False

def view_food_items_est_price():
    print("\n\033[1m\033[94m------VIEW ALL FOOD ITEMS ACCORDING TO PRICE------\033[0m")
    print("[1] Ascending")
    print("[2] Descending")
    choice = int(input("Choice: "))
    if choice == 1:
        order = "asc"
    elif choice == 2:
        order = "desc"

    view_food_est()

    print("\nPick the Food Establishment ID you want to view food items from")
    foodEstID = int(input("Choice: "))

    # Query to select food items from specified food establishment
    selectAllFoodItems = "select * from Food_Establishment natural join Food_Item where Food_establishment_id=%s order by %s"
    selectAllFoodItemsParams = (foodEstID, order)
    resultAllFoodItems = db_util.execute_query(selectAllFoodItems, selectAllFoodItemsParams, True)

    for i in resultAllFoodItems:
        print(f"{i['Food_id']}: {i['Food_name']} - Php {i['Food_price']}")