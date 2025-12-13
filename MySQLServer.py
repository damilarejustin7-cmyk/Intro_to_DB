import mysql.connector
from mysql.connector import Error

def main():
    connection = None
    try:
        # 1. Connect to MySQL server (no database argument here)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # change if you use another user
            password="YOUR_PASSWORD_HERE"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # 2. Create database if it does not already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # 3. Success message
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        # 4. Error message on failure
        print(f"Error connecting to MySQL or creating database: {err}")

    finally:
        # 5. Cleanly close cursor and connection
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()

