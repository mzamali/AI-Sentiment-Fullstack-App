import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        connection=psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        connection.autocommit=True
        return connection
    except Exception as error:
        print(f"Error: Could not connect to database. {error}")
        return None

        
if __name__ == "__main__":
    conn=get_db_connection()
    if conn:
        print("--- Success! Python is now talking to PostgreSQL! ---")
        conn.close()
