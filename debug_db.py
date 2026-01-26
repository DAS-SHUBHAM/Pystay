import mysql.connector
import database

def inspect_db():
    conn = database.get_db_connection()
    if not conn:
        print("Failed to connect.")
        return

    cursor = conn.cursor()
    
    print("--- Table: users ---")
    try:
        cursor.execute("DESCRIBE users")
        columns = cursor.fetchall()
        for col in columns:
            print(col)
    except Exception as e:
        print(f"Error describing users: {e}")

    print("\n--- Rows (First 5) ---")
    try:
        cursor.execute("SELECT * FROM users LIMIT 5")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error fetching rows: {e}")
        
    conn.close()

if __name__ == "__main__":
    inspect_db()
