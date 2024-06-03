import mysql.connector
from mysql.connector import errorcode


def connect_to_db():
    try:
        
        cnx = mysql.connector.connect(
            user='cmsc127_project',  
            password='project',     
            database='cmsc127_project'  
        )
        return cnx  
    except mysql.connector.Error as err:
        
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied.")  
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")  
        else:
            print(err)  
        return None  


def execute_query(query, params=None, fetch=False):
    cnx = connect_to_db()  
    if not cnx:
        return None  
    cursor = cnx.cursor(dictionary=True if fetch else False)  
    try:
        cursor.execute(query, params)  
        if fetch:
            results = cursor.fetchall() 
            return results  
        else:
            cnx.commit()  
            return cursor  
    except mysql.connector.Error as err:
        print(f"Error: {err}")  
        return None  
    finally:
        cursor.close()  
        cnx.close()  
