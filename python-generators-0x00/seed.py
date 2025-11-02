import psycopg2
import csv

def connect_db():
    # Connect to the default 'postgres' database
    try:
        return psycopg2.connect(
            dbname="alx_prodev",
            user="postgres",
            password="yared@pgdb",  # Add your password if needed
            host="localhost"
        )
    except Exception as e:
        print("Connection failed:", e)
        return None

def create_database(connection):
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("SELECT datname FROM pg_database WHERE datname = 'alx_prodev';")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute("CREATE DATABASE alx_prodev")
        print("Database alx_prodev created")
    cursor.close()

import time

def create_database(connection):
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM pg_database WHERE datname='alx_prodev'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute("CREATE DATABASE alx_prodev")
        print("Database alx_prodev created")
    else:
        print("Database alx_prodev already exists")
    cursor.close()

def connect_to_prodev():
    try:
        return psycopg2.connect(
            dbname="alx_prodev",  # ← match the actual name used in CREATE DATABASE
            user="postgres",
            password="yared@pgdb",
            host="localhost"
        )
    except Exception as e:
        print("Connection to alx_prodev failed:", e)
        return None

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id UUID PRIMARY KEY,
            name VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            age DECIMAL NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    print("Table user_data created successfully")

def insert_data(connection, csv_file):
    cursor = connection.cursor()
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (user_id) DO NOTHING
            """, (row['user_id'], row['name'], row['email'], row['age']))
    connection.commit()
    cursor.close()
    print("Data inserted successfully")
