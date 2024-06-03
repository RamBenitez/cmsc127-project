import mysql.connector
from mysql.connector import errorcode

# Function to establish a connection to the database
def connect_to_db():
    try:
        # Connect to the MySQL database using the provided credentials
        cnx = mysql.connector.connect(
            user='cmsc127_project',  # username
            password='project',      # password
            database='cmsc127_project'  # database name
        )
        return cnx  
    except mysql.connector.Error as err: # handle errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied.")  # Invalid username or password
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")  # Database not found
        else:
            print(err)  # Print other errors
        return None  # Return None if the connection fails

# Function to execute a query
def execute_query(query, params=None, fetch=False): # Fetching = SELECT statements. Non-fetch = INSERT statements, etc.
    cnx = connect_to_db()  # Establish a database connection
    if not cnx:
        return None  # Exit if the connection fails
    cursor = cnx.cursor(dictionary=True if fetch else False)  # Create a cursor object, with dictionary results if fetching
    try:
        cursor.execute(query, params)  # Execute the query with the optional parameters
        if fetch:
            results = cursor.fetchall()  # Fetch all results if required
            return results  # Return the fetched results
        else:
            cnx.commit()  # Proceed with transaction if not fetching
            return cursor  # Return the cursor object
    except mysql.connector.Error as err:
        print(f"Error: {err}")  # Print any errors that occur during execution
        return None  # Return None if an error occurs
    finally:
        cursor.close()  # Close the cursor
        cnx.close()  # Close the database connection
