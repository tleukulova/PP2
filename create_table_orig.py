import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE Contacts (
            ContactID INT AUTO_INCREMENT PRIMARY KEY,
            FirstName VARCHAR(50),
            LastName VARCHAR(50)
        )
        """,
        """ CREATE TABLE ContactDetails (
                ContactDetailID INT AUTO_INCREMENT PRIMARY KEY,
                ContactID INT,
                PhoneNumber VARCHAR(15),
                FOREIGN KEY (ContactID) REFERENCES Contacts(ContactID)
                )
        """)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()