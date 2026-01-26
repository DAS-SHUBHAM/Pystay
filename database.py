import mysql.connector
from tkinter import messagebox
import bcrypt

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "hoteldb"
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to database: {err}")
        return None

def initialize_db():
    """Ensures the users table exists."""
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL
                )
            """)
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error initializing database: {err}")

def verify_login(username, password):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()
            if result:
                stored_password = result[0]
                # Check if stored password is bytes (hashed) or string
                if isinstance(stored_password, str):
                    stored_password = stored_password.encode('utf-8')
                
                if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                    return True
            return False
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error verifying login: {err}")
            return False
        except Exception as e:
            print(f"Login error: {e}") # Debugging
            return False
        finally:
            conn.close()
    return False

def register_user(username, password, question=None, answer=None):
    conn = get_db_connection()
    if conn:
        try:
            # Handle optional security fields for DB compatibility
            if question is None:
                question = "Not Set"
            if answer is None:
                answer = "Not Set"

            hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", 
                           (username, hashed_pw))
            conn.commit()
            return True
        except mysql.connector.IntegrityError:
            return False # Username likely exists
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error registering user: {err}")
            return False
        finally:
            conn.close()
    return False

def get_security_question(username):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT security_question FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()
            return result
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error fetching security question: {err}")
            return None
        finally:
            conn.close()
    return None

def reset_password(username, answer, new_password):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Verify answer first
            cursor.execute("SELECT security_answer FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()
            if result and result[0] == answer:
                cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new_password, username))
                conn.commit()
                return True
            return False
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error resetting password: {err}")
            return False
        finally:
            conn.close()
    return False

# Initialize table on import or first run
initialize_db()
