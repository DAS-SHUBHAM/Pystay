🏨 PyStay – Hotel Management System
--------------------------------------------------------------------------------------------------------------------------------
PyStay is a desktop-based Hotel Management System built using Python (Tkinter) and MySQL.
It provides an easy-to-use graphical interface for managing customers, room bookings, and billing operations in a hotel environment.
-----------------------------------------------------------------------------------------------------------------------------------

This project is suitable for learning:
GUI development with Tkinter
Database connectivity with MySQL
CRUD operations in Python
-----------------------------------------------------------------------------------------------------------------------------------
✨ Features
------------------
🔐 Authentication System
-User Sign Up and Login
-Credentials stored in MySQL
-Mandatory authentication before accessing the system
-----------------------------------------------------------------------------------------------------------------------------------
🖥️ Main Dashboard
-------------------
-Centralized, menu-driven interface
-Easy navigation to:
-Customer
-Rooms
-Details
-Reports
-Attractive UI with images and layouts
----------------------------------------------------------------------------------------------------------------------------------
👤 Customer Management
------------------------
-Add, update, and delete customer records
-Auto-generate customer reference number
-Search customers by:
  -📱 Mobile number
  -🪪 ID number
  -🔖 Reference ID
----------------------------------------------------------------------------------------------------------------------------------
Display customer details using TreeView
----------------------------------------
-🛏️ Room Booking Management
-Book rooms with check-in & check-out dates
-Fetch customer details using contact number
-Select:
  -Room type (Single / Double / Luxury)
  -Meal type (Veg / Non-Veg)
  -Automatic bill calculation:
  -Tax
  -Subtotal
  -Total amount
  -Update or delete room bookings
----------------------------------------------------------------------------------------------------------------------------------
💰 Billing System
-------------------
-Calculates cost based on:
-Room type
-Meal type
-Number of staying days
-Displays:
  -Tax
  -Subtotal
  -Final payable amount
----------------------------------------------------------------------------------------------------------------------------------
🛠️ Technologies Used
----------------------
-Python 3.x
-Tkinter – GUI development
-Pillow (PIL) – Image handling
-MySQL – Database
-mysql-connector-python – Database connectivity
----------------------------------------------------------------------------------------------------------------------------------
📂 Project Structure
----------------------
PyStay/
│
├── login.py        # Authentication (Login & Signup)
├── main.py         # Tkinter application handler
├── customer.py     # Customer management module
├── room.py         # Room booking & billing module
├── details.py      # Customer & room details handling
├── img/            # UI / UX images
├── screenshots/    # Application screenshots
└── README.md
-----------------------------------------------------------------------------------------------------------------------------------
⚙️ Requirements
-------------------
🔹 Software Requirements
Python 3.8 or higher
MySQL Server
MySQL Workbench (optional)
-----------------------------------------
🔹 Python Libraries
Install the required libraries:
pip install pillow mysql-connector-python
Tkinter comes pre-installed with Python.
-------------------------------------------
🗄️ Database Setup
1️⃣ Create Database
CREATE DATABASE hoteldb;
USE hoteldb;

2️⃣ Create Customer Table
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

3️⃣ Create Rooms Table
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
--------------------------------------------------------
🔐 Database Configuration
----------------------------
Update MySQL credentials in
customer.py, room.py, and login/signup module if required:

mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="hoteldb"
)
--------------------------------------------------------------
▶️ How to Run the Project (Step-by-Step)
----------------------------------------
Step 1️⃣ Clone the Repository
git clone https://github.com/your-username/PyStay.git
cd PyStay
---------------------------------------
Step 2️⃣ Start MySQL Server
Ensure MySQL service is running
Database and tables must be created
---------------------------------------
Step 3️⃣ Run the Application
python main.py
---------------------------------------
🧭 How to Use the System
🔹 Step 1: Sign Up (First-Time Users)
    -Launch the application
    -Click Sign Up
    -Create a username and password
    -Account will be saved in the database

🔹 Step 2: Login
    -Enter registered credentials
    -Click Log In
    -On successful login, the Dashboard opens

🔹 Step 3: Dashboard Navigation
    -From the left menu, you can access:
    -Customer → Add / Update / Delete customer details
    -Rooms → Book rooms & calculate bills
    -Details → View booking details
    -Report → View system data
    -Logout → Exit the application
------------------------------------------------------------
🔐 Login Screen
📝 Sign Up Screen
🏨 Main Dashboard
👤 Customer Management Module
------------------------------------------------------------
🚀 Future Improvements
--------------------------
 -Role-based login (Admin / Staff)
 -Room availability tracking
 -PDF invoice generation
 -Calendar date picker
 -Stronger password hashing
 -Improved validation & error handling
---------------------------------------------------------------
👨‍💻 Author
------------
Shubham Das
Python Developer | GUI & Database Enthusiast
--------------------------------------------------------------
📜 License
This project is created for learning and educational purposes.
You are free to modify and enhance it.
