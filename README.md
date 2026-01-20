
# PyStay – Hotel Management System 🏨

PyStay is a **desktop-based Hotel Management System** built using **Python (Tkinter)** and **MySQL**. It provides an easy-to-use graphical interface for managing **customers**, **room bookings**, and **billing** operations in a hotel environment.

This project is suitable for **learning GUI development**, **database connectivity**, and **CRUD operations** using Python.
---
## ✨ Features
### 🔹 Main Dashboard
* Centralized menu-driven interface
* Navigation to Customer and Room Booking modules
* Attractive UI using images and layout
  
### 🔹 Customer Management
* Add, update, delete customer records
* Auto-generate customer reference number
* Search customers by mobile, ID number, or reference ID
* View customer details in a table (TreeView)

### 🔹 Room Booking Management
* Book rooms with check-in & check-out dates
* Fetch customer details using contact number
* Select room type, meal type, and stay duration
* Automatic bill calculation (tax, subtotal, total price)
* Update or delete room bookings

### 🔹 Billing System
* Calculates cost based on:
  * Room type (Single / Double / Luxury)
  * Meal type (Veg / Non-Veg)
  * Number of staying days
* Displays tax, subtotal, and final amount
---

## 🛠️ Technologies Used
* **Python 3.x**
* **Tkinter** – GUI development
* **Pillow (PIL)** – Image handling
* **MySQL** – Database
* **mysql-connector-python** – Database connectivity
---

## 📂 Project Structure
```
PyStay/
│
├── main.py              # Main dashboard (HotelManagementSystem)
├── customer.py          # Customer management module
├── room.py              # Room booking & billing module
├── img/                 # Images used in the UI
│   ├── logo.png
│   ├── hotels.jpg
│   ├── bedroom.jpg
│   └── ...
├── README.md
```

---

## ⚙️ Requirements
### 🔹 Software Requirements
* Python **3.8 or higher**
* MySQL Server
* MySQL Workbench (optional, for database management)

### 🔹 Python Libraries
Install the required libraries using:
```bash
pip install pillow mysql-connector-python
```
Tkinter comes **pre-installed** with Python.
---
## 🗄️ Database Setup
### 1️⃣ Create Database
```sql
CREATE DATABASE hoteldb;
USE hoteldb;
```
### 2️⃣ Create Customer Table
```sql
CREATE TABLE Customer (
    c_ref VARCHAR(20) PRIMARY KEY,
    c_name VARCHAR(100),
    m_name VARCHAR(100),
    gender VARCHAR(20),
    zipcode VARCHAR(20),
    mobile VARCHAR(20),
    email VARCHAR(100),
    nationality VARCHAR(50),
    id_proof VARCHAR(50),
    id_number VARCHAR(50),
    address VARCHAR(255)
);
```
### 3️⃣ Create Rooms Table
```sql
CREATE TABLE rooms (
    contact VARCHAR(20),
    CheckIn VARCHAR(20),
    CheckOut VARCHAR(20),
    RoomType VARCHAR(50),
    RoomNumber VARCHAR(20),
    StayingDays VARCHAR(10),
    MealType VARCHAR(20),
    PaidTax VARCHAR(20),
    SubTotal VARCHAR(20),
    TotalPrice VARCHAR(20)
);
```
### 4️⃣ Update Database Credentials
In **customer.py** and **room.py**, update the MySQL credentials if required:
```python
mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="hoteldb"
)
```
---
## ▶️ How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/PyStay.git
   ```
2. Navigate to the project folder:
   ```bash
   cd PyStay
   ```
3. Ensure MySQL server is running
4. Run the main file:
   ```bash
   python main.py
   ```
---
## 📸 Screens Included
* Dashboard UI
* Customer Management Window
* Room Booking Window
* Billing Calculation Screen
*(Add screenshots here for better GitHub presentation)*
---
## 🚀 Future Improvements
* Login & authentication system
* Room availability tracking
* PDF invoice generation
* Date picker calendar
* Improved validation & error handling
---
## 👨‍💻 Author
**Shubham Das**
Python Developer | GUI & Database Enthusiast
---
## 📜 License
This project is created for **learning and educational purposes**. You are free to modify and enhance it.
---

⭐ If you like this project, don’t forget to **star the repository** on GitHub!
