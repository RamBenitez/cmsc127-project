def add_review():
    while True:
        print("\n\033[1m------ADD REVIEW MENU------\033[0m")
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
            print("\nInvalid choice. Please try again.")

#Add food review on a food item
def add_food_review():
    
    print("\n\033[1m-----ADD FOOD REVIEW-----\033[0m")
    #QUery to show  all the food items
    print("FOOD ITEMS....")
    FoodItemChoice = input("\nChoice: ")
    FoodRating= input("Rating (1-5):")
    FoodContent= input("Content")
    print("\nSuccessully added review of food <FOOD ITEM>\n")

 #add a food establishment review   
def add_food_establishment_review():
    print("\n\033[1m-----ADD FOOD  ESTABLISHMENT REVIEW-----\033[0m")
    #QUery to show  all the food establishments
    print("FOOD ESTABLISHMENTS....")
    FoodEstablishmentChoice = input("\nChoice: ")
    EstablishmentRating= input("Rating (1-5):")
    EstablishmentContent= input("Content")
    print("\nSuccessully added review of ESTABLISHMENT <FOOD ESTABLSIHMENT>\n")
    