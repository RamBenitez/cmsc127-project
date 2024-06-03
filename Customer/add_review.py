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
def add_food_review():
    print("\n\033[1m\033[94m-----ADD FOOD REVIEW-----\033[0m")
    #QUery to show  all the food items
    print("List of Food Items: ")
    FoodItemChoice = input("\nChoice: ")
    FoodRating= input("Rating (1-5): ")
    FoodContent= input("Review: ")
    print("\n\033[92mSuccessully added review of <FOOD ITEM>\033[0m\n")

 #add a food establishment review   
def add_food_establishment_review():
    print("\n\033[1m\033[94m-----ADD FOOD  ESTABLISHMENT REVIEW-----\033[0m")
    #QUery to show  all the food establishments
    print("FOOD ESTABLISHMENTS....")
    FoodEstablishmentChoice = input("\nChoice: ")
    EstablishmentRating= input("Rating (1-5):")
    EstablishmentContent= input("Review: ")
    print("\n\033[92mSuccessully added review of <FOOD ESTABLISHMENT>\033[0m\n")
    