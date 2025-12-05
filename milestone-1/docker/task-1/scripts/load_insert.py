import csv
import psycopg2

conn = None
try:
    conn = psycopg2.connect(
        "dbname='test_db' user='postgres' host='localhost' password='qwerty'"
    )
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO users (user_id, username, email, signup_date, is_active)
    VALUES (%s, %s, %s, %s, %s)
    """

    with open("user_data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header

        for row in reader:
            # Execute the parameterized query
            cursor.execute(insert_query, row)

    conn.commit()
    print("Data successfully loaded into 'users' table.")

except Exception as e:
    print(f"failed: {e}")
finally:
    if conn:
        conn.close()
