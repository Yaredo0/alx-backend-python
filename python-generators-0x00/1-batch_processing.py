import psycopg2
import psycopg2.extras

def stream_users_in_batches(batch_size):
    connection = psycopg2.connect(
        dbname="alx_prodev",
        user="postgres",
        password="yared@pgdb",
        host="localhost"
    )
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM user_data")

    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        for row in rows:
            yield dict(row)

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    for user in stream_users_in_batches(batch_size):
        if user["age"] > 25:
            yield user
