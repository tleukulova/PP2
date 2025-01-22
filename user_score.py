import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_table():
    # Database connection parameters
    dbname = "user_score"
    user = "postgres"
    password = "66699193061519"
    host = "localhost"

    # Connect to your postgres DB
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    
    # Set the isolation level (required to create a database)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Create table
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL UNIQUE,
                email VARCHAR(255) NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        print("Table created successfully")
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up
        cur.close()
        conn.commit()
        conn.close()

if __name__ == '__main__':
    create_table()
