import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL Server (NOT to any database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Penielokrah@12"   # put your actual MySQL password here
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")  # optional

if __name__ == "__main__":
    create_database()