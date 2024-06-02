import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS cmsc127_project")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)

def main():
    # Connect to MySQL server
    cnx = mysql.connector.connect(
        user='cmsc127_project',  # mysql username
        password='project'  # password
    )
    cursor = cnx.cursor()

    # Create database
    try:
        cursor.execute("USE cmsc127_project")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            cnx.database = 'cmsc127_project'
        else:
            print(err)
            exit(1)

    # Read schema.sql and execute it
    schema_path = 'schema.sql' 
    with open(schema_path) as f:
        schema_sql = f.read()

    for result in cursor.execute(schema_sql, multi=True):
        pass

    cursor.close()
    cnx.close()

if __name__ == "__main__":
    main()
