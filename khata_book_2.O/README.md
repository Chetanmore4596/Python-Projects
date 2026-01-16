# 📒 Khata Book 2.O (Contact Book Management System)

A **console-based Contact & Account Management System** built using **Python and MySQL**.  
Khata Book 2.O allows users to **create accounts, manage contacts, update profiles, and securely store data** using a relational database.

---

## 🚀 Features  

✅ **User Account Creation & Login**  
✅ **Secure Authentication (Email & Password)**  
✅ **Create, Update, Delete & View Contacts**  
✅ **User-wise Contact Management**  
✅ **Profile Update & Account Deletion**  
✅ **MySQL Database Integration**  
✅ **Beginner-Friendly & Well Structured**

---

## 🛠️ Tech Stack  

- **Python 3**  
- **MySQL**  
- **mysql-connector-python**  
- **Console / Terminal Application**

---

## 🗃️ Database Files  

This project uses **two MySQL database files**:

- `khata_book_users.sql` → Stores user account details  
- `khata_book_contacts.sql` → Stores contact details  

📌 Import both files into MySQL before running the project.

---

## ⚡ Installation & Setup  

### 🔹 Prerequisites
- Python 3 installed  
- MySQL Server installed  
- mysql-connector-python library  

Install MySQL connector:
```bash
pip install mysql-connector-python
# Clone repository
git clone https://github.com/Chetanmore4596/Khata-Book-2.0.git

# Navigate to project folder
cd Khata-Book-2.0

# Run the application
python khata_book.py
CREATE DATABASE khata_book;

mysql -u root -p khata_book < khata_book_users.sql
mysql -u root -p khata_book < khata_book_contacts.sql
