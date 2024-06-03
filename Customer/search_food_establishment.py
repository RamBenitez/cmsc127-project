from Database import db_util

def search_food_establishment():
    while True:
        print("\n\033[1m\033[94m------SEARCH FOR A FOOD ESTABLISHMENT MENU------\033[0m")
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
            print("\n\033[91mInvalid choice. Please try again.\033[0m")

# Search for a food establishment by name
def search_by_name():
    print("\n\033[1m\033[94m-----SEARCH BY NAME-----\033[0m")
    restaurant_name = input("Input restaurant name: ")
    # query to retrieve food establishments with similar names
    query = """
    SELECT Food_establishment_id, Food_establishment_name
    FROM Food_Establishment
    WHERE Food_establishment_name LIKE %s
    """
    params = (f'%{restaurant_name}%',)
    # Execute the query
    results = db_util.execute_query(query, params, fetch=True)
    # Print the details of the food establishments
    if results:
        print("\nFood Establishments with Similar Names:")
        for establishment in results:
            print(f"Establishment ID: {establishment['Food_establishment_id']}, Name: {establishment['Food_establishment_name']}")
    else:
        print("\nNo food establishments found with similar names.")

# Search for food establishments by rating range
def search_by_rating():
    print("\n\033[1m\033[94m-----SEARCH BY RATING-----\033[0m")
    lower_range = float(input("Input lower range: "))
    higher_range = float(input("Input higher range: "))

    # Query to retrieve food establishments within the rating range
    query = """
    SELECT fe.Food_establishment_id, fe.Food_establishment_name, AVG(fr.Rating) as avg_rating
    FROM Food_Establishment fe
    JOIN Food_Review fr ON fe.Food_establishment_id = fr.Food_establishment_id
    WHERE fr.Food_id IS NULL
    GROUP BY fe.Food_establishment_id, fe.Food_establishment_name
    HAVING avg_rating BETWEEN %s AND %s
    """

    params = (lower_range, higher_range)
    # Execute the query
    results = db_util.execute_query(query, params, fetch=True)
    # Print the details of the food establishments
    if results:
        print("\nFood Establishments within the Rating Range:")
        for establishment in results:
            print(f"Establishment ID: {establishment['Food_establishment_id']}, Name: {establishment['Food_establishment_name']}, Rating: {establishment['avg_rating']:.2f}")
    else:
        print("\nNo food establishments found within the specified rating range.")
