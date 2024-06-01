def delete_review():
    while True:
        print("\n\033[1m------DELETE REVIEW MENU------\033[0m")
        print("[1] Delete a review on a food item")
        print("[2] Delete a review on a food establishment")
        print("[3] Back")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            delete_food_review()
        elif choice == '2':
            delete_food_establishment_review()
        elif choice == '3':
            break
        else:
            print("\nInvalid choice. Please try again.")

# Delete review of a food item
def delete_food_review():
    print("\n\033[1m-----DELETE FOOD REVIEW-----\033[0m")
    # Query to show all the customer's food item reviews
    print("CUSTOMER'S FOOD ITEM REVIEWS....")
    # Customer selects a review to delete
    review_choice = input("\nChoice: ")
    # Delete the review from the database
    print("\nSuccessfully deleted review of <food item>!\n")

# Delete review of a food establishment
def delete_food_establishment_review():
    print("\n\033[1m-----DELETE FOOD ESTABLISHMENT REVIEW-----\033[0m")
    # Query to show all the customer's food establishment reviews
    print("CUSTOMER'S FOOD ESTABLISHMENT REVIEWS....")
    # Customer selects a review to delete
    review_choice = input("\nChoice: ")
    # Delete the review from the database
    print("\nSuccessfully deleted review of <food establishment>!\n")
