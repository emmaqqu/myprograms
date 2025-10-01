import sqlite3

# Connection: ALlows us to connect Python to a SQL database
connection = sqlite3.connect("./database.db")
# Cursor: Allows us to interact with the SQL DB
cursor = connection.cursor()

query = """
SELECT * 
FROM Products 
WHERE ;

"""

result = cursor.execute(query).fetchall()
print(f"OUR SQL RESULT: {result}")

# End of code
connection.commit() # Commits changes
connection.close() # Disconnects the connection