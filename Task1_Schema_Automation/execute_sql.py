import mysql.connector

# AWS RDS Database Configuration
db_config = {
    "host": "database-1.cdogxn9itvft.us-east-1.rds.amazonaws.com",  # Replace with your RDS endpoint
    "user": "admin",  # Replace with your RDS username
    "password": "admin1234",  # Replace with your RDS password
    "database": "companydb"  # Replace with your database name
}

def execute_sql_script(file_path):
    conn = None
    cursor = None  # Initialize cursor to avoid unbound error

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        with open(file_path, "r") as sql_file:
            sql_commands = sql_file.read().split(";")

        for command in sql_commands:
            if command.strip():
                cursor.execute(command)

        conn.commit()
        print("SQL script executed successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:  # Ensure cursor is initialized before closing
            cursor.close()
        if conn:  # Ensure connection exists before closing
            conn.close()

# Run the script
execute_sql_script("schema_changes.sql")