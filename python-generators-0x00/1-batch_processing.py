import psycopg2
import psycopg2.extras

def stream_users_in_batches(batch_size):
    try:
        connection = psycopg2.connect(
            dbname="alx_prodev",
            user="postgres",
            password="",
            host="localhost"
        )
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM user_data")

        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield [dict(row) for row in batch]

        cursor.close()
        connection.close()

    except Exception as e:
        print("Error streaming batches:", e)

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                yield user
