def update_review():
    while True:
        print("\n\033[1m------UPDATE REVIEW MENU------\033[0m")
        print("[1] Update a review on a food item")
        print("[2] Update a review on a food establishment")
        print("[3] Back")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            update_food_review()
        elif choice == '2':
            update_food_establishment_review()
        elif choice == '3':
            break
        else:
            print("\nInvalid choice. Please try again.")

# Update review of a food item
def update_food_review():
    print("\n\033[1m-----UPDATE FOOD REVIEW-----\033[0m")
    # Query to show all the customer's food item reviews
    print("CUSTOMER'S FOOD ITEM REVIEWS....")
    # Customer selects a review to update
    review_choice = input("\nChoice: ")
    new_rating = input("New Rating (1-5): ")
    new_content = input("Content: ")
    # Update the review in the database
    print("\nSuccessfully updated review of <food item>!\n")

# Update review of a food establishment
def update_food_establishment_review():
    print("\n\033[1m-----UPDATE FOOD ESTABLISHMENT REVIEW-----\033[0m")
    # Query to show all the customer's food establishment reviews
    print("CUSTOMER'S FOOD ESTABLISHMENT REVIEWS....")
    # Customer selects a review to update
    review_choice = input("\nChoice: ")
    new_rating = input("New Rating (1-5): ")
    new_content = input("Content: ")
    # Update the review in the database
    print("\nSuccessfully updated review of <food establishment>!\n")
