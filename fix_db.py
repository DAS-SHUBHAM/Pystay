import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "hoteldb"
}

def fix_schema():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Check columns
        cursor.execute("DESCRIBE users")
        columns = [row[0] for row in cursor.fetchall()]
        print("Current columns:", columns)
        
        if "security_question" not in columns:
            print("Adding security_question column...")
            cursor.execute("ALTER TABLE users ADD COLUMN security_question VARCHAR(255) NOT NULL DEFAULT 'Default Question'")
            
        if "security_answer" not in columns:
            print("Adding security_answer column...")
            cursor.execute("ALTER TABLE users ADD COLUMN security_answer VARCHAR(255) NOT NULL DEFAULT 'Default Answer'")
            
        conn.commit()
        print("Schema update complete.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    fix_schema()
