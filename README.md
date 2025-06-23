# Contact Management System (Python + MySQL)

A beginner-friendly command-line application to manage contact information using Python and MySQL.

## 📌 Features
- Add new contacts
- View all contacts
- Update existing contacts
- Delete contacts
- Search contacts by name
- Export contacts to CSV

## 🛠️ Tech Stack
- Python
- MySQL
- MySQL Connector for Python

## 🧪 How to Run
1. Make sure MySQL server is installed and running
2. Create the database:
```sql
CREATE DATABASE contactDB;
USE contactDB;
CREATE TABLE contacts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  phone VARCHAR(15),
  email VARCHAR(100)
);
