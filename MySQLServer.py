import mysql.connector

try:
    # Establish connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Emma-39058178"
    )

    print("Connected to MySQL server successfully!")

    # Create a cursor object
    cursor = connection.cursor()

    # Create database if it does not exist
    create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
    cursor.execute(create_db_query)

    print("Database 'alx_book_store' created successfully!")

    # Close cursor and connection
    cursor.close()
    connection.close()
    print("MySQL connection closed.")

except mysql.connector.MySQLError as e:
    print(f"Error: {e}")

finally:
    if 'connection' in locals() and connection.open:
        connection.close()
        print("MySQL connection closed.")
