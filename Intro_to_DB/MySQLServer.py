import mysql.connector

# Database connection parameters
DB_CONFIG = {
    'host': 'localhost',  
    'user': 'root',  
    'password': 'AdminRoot2025'
}

DATABASE_NAME = 'alx_book_store'

def create_database():
    """
    Connects to MySQL server and creates the specified database.
    Handles existing database gracefully and prints status messages.
    """
    connection = None
    try:
        # Connect to MySQL server without specifying a database initially
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # SQL statement to create the database if it doesn't exist
        # This implicitly handles the case where the database already exists
        # without needing SELECT or SHOW statements, as per requirements.
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"
        cursor.execute(create_db_query)

        print(f"Database '{DATABASE_NAME}' created successfully!")

    except mysql.connector.Error as err:
        # Print error message if connection or query fails
        print(f"Error connecting to or creating database: {err}")
    finally:
        # Ensure the connection is closed
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()