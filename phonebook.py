import psycopg2, csv

db=psycopg2.connect(dbname='phonebook', user='postgres', password='66699193061519', host='localhost')
current=db.cursor()

print('''What do you want?

Press "1" to search contact by name or phone
Press "2" to add a new contact or update existing 
Press "3" to add many contacts by list
Press "4" to see first N contacts
Press "5" to delete contact by name or phone
Press "6" to add contacts from .csv file
Press "7" to change name or phone of contact
Press "8" to see all names of contacts
Press "9" to see all phones of contacts 
Press "10" to see all phonebook
''')
req = input("Enter the number of request:")

if req == '1':
    n = input("Enter name or phone:")
    sql="""
        SELECT * FROM contacts WHERE contacts.name LIKE %s OR contacts.phone LIKE %s;
    """
    current.execute(sql, (n, n))
    results = current.fetchall()
    print(results)

elif req == '2':
    name = input("Enter name:")
    phone = input("Enter phone:")
    
    # Delete the existing contact with the given name
    delete_sql = "DELETE FROM contacts WHERE contacts.name = %s;"
    current.execute(delete_sql, (name,))
    
    # Insert the new contact
    insert_sql = "INSERT INTO contacts (name, phone) VALUES (%s, %s);"
    current.execute(insert_sql, (name, phone))
    print("The contact was added successfully!")

elif req == '3':
#   example of list = [('v', 123), ('xij', 1331), ('hjdh', 222425626)]
    contact = input("Enter the list of contacts:")
    
    cont = []
    for tup in contact.split('), ('):
        tup = tup.replace(')','').replace('(','')
        cont.append(tuple(tup.split(',')))
    print(cont)
    sql="""
        INSERT INTO contacts VALUES(%s, %s);
    """
    for i in range(len(cont)):
        current.execute(sql, (cont[i][0], cont[i][1]))

elif req == '4':
    x = input("Enter the number of contacts:") 
    sql = """
        SELECT * FROM contacts;
    """
    current.execute(sql)
    results = current.fetchmany(int(x))
    print('''PHONEBOOK
=========================================
NAME                PHONE
=========================================''')
    for i in range(len(results)):
        print('{0:20}{1:20}'.format(results[i][1], results[i][3]))

elif req == '5':
    print("Enter the name or phone:")
    delete = input()
    sql="""
        DELETE FROM contacts WHERE contacts.name = %s;
    """
    current.execute(sql, (delete,))
    sql="""
        DELETE FROM contacts WHERE contacts.phone = %s;
    """
    current.execute(sql, (delete,))
    print("Contact", delete, "has been deleted")

elif req == '6':
    sql = """
        INSERT INTO contacts (name, surname, phone) VALUES (%s, %s, %s);
    """
    with open(r'/Users/aruzhantleukul/Desktop/tsis10/contacts.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 4:  # Ensure there are at least 4 elements in the row
                current.execute(sql, (row[1], row[2], row[3]))  # Assuming contactid is at index 0
            else:
                print("Invalid row format:", row)
    print("Data has been added to the phonebook")

elif req == '7':
    w = input("Do you want to update name or phone:")
    if w == 'name':
        x = input("Enter the phone: ")
        y = input("Enter the new name: ")
        sql = """
            UPDATE contacts SET contacts.name = %s WHERE contacts.phone = %s;
        """
        current.execute(sql, (y, x))
        print("Data has been updated")
    elif w == 'phone':
        x = input("Enter the name: ")
        y = input("Enter the new phone_number: ")
        sql = """
            UPDATE contacts SET contacts.phone = %s WHERE contacts.name = %s;
        """
        current.execute(sql, (y, x))
        print("Data has been updated")

elif req == '8':
    sql = """
        SELECT contacts.name FROM contacts
    """
    current.execute(sql)
    results = current.fetchall()
    for i in range(len(results)):
        print(results[i][0])

elif req == '9':
    sql = """
        SELECT contacts.phone FROM contacts
    """
    current.execute(sql)
    results = current.fetchall()
    for i in range(len(results)):
        print(results[i][0])   
elif req == "10":
    sql = "SELECT * FROM contacts;"
    current.execute(sql)
    rows = current.fetchall()
    for row in rows:
        print(row)

else:
    print("Request is unidentified")

current.close()
db.commit()
db.close()