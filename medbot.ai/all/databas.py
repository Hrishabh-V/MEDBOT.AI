import mysql.connector

cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='pythondatas')
cursor = cnx.cursor()
# Execute an SQL command to create a new table (optional)
cursor.execute("CREATE TABLE my_table (id INT, name VARCHAR(50), age INT)")
# Define a list of data to be inserted into the table
data = [(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 35)]
# Loop through the list of data and insert each row into the table
for row in data:
    cursor.execute("INSERT INTO my_table (id, name, age) VALUES (%s, %s, %s)", row)
# Commit the changes
cnx.commit()
# Close the cursor and connection
cursor.close()
cnx.close()
