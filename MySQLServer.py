import mysql.connector
from mysql.connector import Error
from mysql.connector.constants import ClientFlag
from dotenv import load_dotenv
import os


load_dotenv()

def create_database():
    connection = None
    try:
        
        host = os.getenv("MYSQL_HOST")
        port = int(os.getenv("MYSQL_PORT"))
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")

        
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            client_flags=[ClientFlag.SSL],
            ssl_disabled=False
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
