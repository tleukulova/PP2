import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="66699193061519",
    host="localhost"
)

# Create a cursor object
cur = conn.cursor()

# Delete data in the column (optional)
cur.execute('DELETE FROM contacts WHERE lastname IS NOT NULL')

# Alter the table to drop the column
try:
    cur.execute('ALTER TABLE contacts DROP COLUMN lastname')
    print("Column dropped successfully")
except psycopg2.Error as e:
    print(f"An error occurred: {e}")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
