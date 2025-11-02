import psycopg2

def stream_user_ages():
    connection = psycopg2.connect(
        dbname="alx_prodev",
        user="postgres",
        password="yared@pgdb",
        host="localhost"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    for row in cursor:
        yield row[0]

    cursor.close()
    connection.close()

def compute_average_age():
    total = 0
    count = 0

    for age in stream_user_ages():
        total += age
        count += 1

    if count > 0:
        average = total / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No users found.")

# ✅ Add this line to trigger the computation
compute_average_age()
