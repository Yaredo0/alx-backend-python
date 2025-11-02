import psycopg2
import psycopg2.extras

def stream_users():
    try:
        connection = psycopg2.connect(
            dbname="alx_prodev",
            user="postgres",
            password="yared@pgdb",
            host="localhost"
        )
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield dict(row)

        cursor.close()
        connection.close()

    except Exception as e:
        print("Error streaming users:", e)
