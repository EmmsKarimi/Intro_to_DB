import mysql.connector

try:
    # Establish connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="Emma-39058178"  # Replace with your MySQL password
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

except mysql.connector.Error as e:  # Ensure this line is in your script
    print(f"Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")
