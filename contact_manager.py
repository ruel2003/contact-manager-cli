import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",           # change to your MySQL username
    password="Ruel@2003",  # change to your MySQL password
    database="contactDB"
)

cursor = db.cursor()

def add_contact(name, phone, email):
    sql = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"
    val = (name, phone, email)
    cursor.execute(sql, val)
    db.commit()
    print("✅ Contact added successfully.")

def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    result = cursor.fetchall()
    print("\n📇 All Contacts:")
    for row in result:
        print(row)

def delete_contact(contact_id):
    sql = "DELETE FROM contacts WHERE id = %s"
    val = (contact_id,)
    cursor.execute(sql, val)
    db.commit()
    print("🗑️ Contact deleted.")

def update_contact(contact_id, name, phone, email):
    sql = "UPDATE contacts SET name = %s, phone = %s, email = %s WHERE id = %s"
    val = (name, phone, email, contact_id)
    cursor.execute(sql, val)
    db.commit()
    print("✏️ Contact updated.")

while True:
    print("\n--- Contact Manager Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)

    elif choice == '2':
        view_contacts()

    elif choice == '3':
        cid = input("Enter Contact ID to delete: ")
        delete_contact(cid)

    elif choice == '4':
        cid = input("Enter Contact ID to update: ")
        name = input("New name: ")
        phone = input("New phone: ")
        email = input("New email: ")
        update_contact(cid, name, phone, email)

    elif choice == '5':
        print("👋 Exiting Contact Manager.")
        break

    else:
        print("❌ Invalid choice. Try again.")
