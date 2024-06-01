def search_food_establishment():
    while True:
        print("\n\033[1m------SEARCH FOR A FOOD ESTABLISHMENT MENU------\033[0m")
        print("[1] Search by name")
        print("[2] Search by rating")
        print("[0] Back")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            search_by_name()
        elif choice == '2':
            search_by_rating()
        elif choice == '0':
            break
        else:
            print("\nInvalid choice. Please try again.")

# Search for a food establishment by name
def search_by_name():
    print("\n\033[1m-----SEARCH BY NAME-----\033[0m")
    restaurant_name = input("Input restaurant name: ")
    # Query the database to retrieve food establishments name
    # Print the details of the food establishments name

# Search for food establishments by rating range
def search_by_rating():
    print("\n\033[1m-----SEARCH BY RATING-----\033[0m")
    lower_range = float(input("Input lower range: "))
    higher_range = float(input("Input higher range: "))
    # Query the database to retrieve food establishments within the rating range
    # Print the details of the food establishments
