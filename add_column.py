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

# Alter the table to add new columns
try:
    cur.execute("""
        ALTER TABLE contacts
        ADD COLUMN name VARCHAR(255),
        ADD COLUMN surname VARCHAR(255),
        ADD COLUMN phone_number VARCHAR(20);
    """)
    print("Columns added successfully")
except psycopg2.Error as e:
    print(f"An error occurred: {e}")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
