import mysql.connector
# Connect to MySQL (replace these with your database credentials)
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root",
 database="your_database_name"
)
# Check if the connection is successful
if mydb.is_connected():
 print("Connected to MySQL database!")
 # Creating a cursor object to interact with the database
 my_cursor = mydb.cursor()
 # Creating an address book table
 create_table_query = """
 CREATE TABLE IF NOT EXISTS address_book (
 id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(50) NOT NULL,
 address VARCHAR(100) NOT NULL,
 phone_number VARCHAR(15) NOT NULL
 )
 """
 my_cursor.execute(create_table_query)
 print("Address book table created successfully!")
 # Closing the cursor and database connection
 my_cursor.close()
 mydb.close()
else:
 print("Connection to MySQL database failed!")
