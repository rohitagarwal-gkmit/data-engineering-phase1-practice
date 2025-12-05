# Task 1 - Postgress container - Python Scripts

This document details the steps taken to generate 60 records of data using a Python script and load this data into a PostgreSQL database running inside a Docker container, demonstrating three data methods.

## Environment

established the environment by running the PostgreSQL container and installing the required Python packages inside it.

### Commands Run:

1.  **Start the PostgreSQL Container:**

    ```bash
    docker run --name pg_db -e POSTGRES_PASSWORD=qwerty -p 5432:5432 -d postgres
    ```

    ![PostgreSQL Container Started](./screenshorts/container_started.png)

2.  **Access the Container Shell and Install Dependencies:**

    ```bash
    docker exec -it pg_db bash
    # Inside the container:
    apt update
    apt install -y python3 python3-pip nano
    pip3 install psycopg2-binary pandas sqlalchemy
    ```

    ![Dependencies Installed](screenshorts/Screenshot%202025-12-05%20at%2011.18.17 AM.png)

3.  **the Python Data Generation Script:**

    ```bash
    nano script.py

    import csv
    import random
    from datetime import datetime, timedelta

    # --- Configuration ---
    header = ['user_id', 'username', 'email', 'signup_date', 'is_active']
    num_records = 60
    output_filename = 'user_data.csv'

    # --- Data Generation Helper ---
    def random_date(start_date):
        """Generates a random date within the last year."""
        return start_date - timedelta(days=random.randint(1, 365))

    # --- Main Logic ---
    data = []
    start_date = datetime.now()

    for i in range(1, num_records + 1):
        user_id = i
        username = f"user_{i:03d}"
        email = f"user{i}@example.com"
        signup_date = random_date(start_date).strftime('%Y-%m-%d')
        is_active = random.choice([True, False])

        data.append([user_id, username, email, signup_date, is_active])

    # --- Write to CSV file ---
    try:
        with open(output_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)  # Write header
            writer.writerows(data)   # Write data rows

        print(f"✅ Successfully generated {num_records} records in {output_filename}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")
    ```

created the 60-record CSV file and set up the target table in the database.

### Commands Run:

1.  **Re-access the Container and Run the Script:**

    ```bash
    python3 generate_data.py
    ```

    ![Data Generation Script Executed](screenshorts/Screenshot%202025-12-05%20at%2011.19.39 AM.png)

2.  **Verify CSV Content:**

    ```bash
    cat user_data.csv | head -n 5
    ```

    ![CSV Content Verification](screenshorts/Screenshot%202025-12-05%20at%2011.20.15 AM.png)

3.  **Connect to `psql` and Create Database/Table:**

    ```bash
    psql -U postgres -d postgres

    # Inside psql:
    CREATE DATABASE test_db;
    \c test_db
    CREATE TABLE users (
        user_id INT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE,
        signup_date DATE,
        is_active BOOLEAN
    );
    \q
    ```

    ![Database and Table Created](screenshorts/Screenshot%202025-12-05%20at%2011.25.24 AM.png)

## Data Loading Methods Executed

The `user_data.csv` file was loaded into the `users` table using three different methods.

### Method 1: Pandas (`df.to_sql()`)

This method uses the Pandas library to treat the CSV as a DataFrame, which is then mapped and inserted into the database via SQLAlchemy.

```python
import pandas as pd
from sqlalchemy import create_engine

# connection string for the database inside the container
DATABASE_URL = "postgresql://postgres:qwerty@localhost:5432/test_db"
engine = create_engine(DATABASE_URL)

# the CSV file
df = pd.read_csv('user_data.csv')

# Load the DataFrame into the SQL table
try:
    df.to_sql(name='users', con=engine, if_exists='replace', index=False)
    print("Pandas: Data successfully loaded into 'users' table.")
except Exception as e:
    print(f"failed: {e}")
```

ran command -

```bash
python load_pandas.py
```

![Pandas Data Loading](screenshorts/Screenshot%202025-12-05%20at%2011.29.46 AM.png)

### Method 2: Standard SQL `INSERT` Statements (`psycopg2`)

This method reads the CSV row-by-row and executes a standard, parameterized SQL `INSERT` statement for each record.

```python
import csv
import psycopg2

conn = None
try:
    conn = psycopg2.connect("dbname='test_db' user='postgres' host='localhost' password='qwerty'")
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO users (user_id, username, email, signup_date, is_active)
    VALUES (%s, %s, %s, %s, %s)
    """

    with open('user_data.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip header

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
```

ran command -

```bash
python load_insert.py
```

![SQL INSERT Data Loading](screenshorts/Screenshot%202025-12-05%20at%2011.30.00 AM.png)

### Method 3: SQLAlchemy ORM Bulk Insertion (`bulk_insert_mappings`)

This method is an optimized intermediate approach. It uses the SQLAlchemy Object-Relational Mapper (ORM) to map CSV records to Python objects and then executes a single, highly efficient multi-row `INSERT` statement.

```python
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import date
import pandas as pd

# Define the base class for declarative class definitions
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True)
    signup_date = Column(Date)
    is_active = Column(Boolean)

# Connection string for the database inside the container
DATABASE_URL = "postgresql://postgres:qwerty@localhost:5432/test_db"
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

try:
    # Create a session
    session = Session()
    df = pd.read_csv('user_data.csv')
    user_mappings = df.to_dict('records')
    session.bulk_insert_mappings(User, user_mappings)

    session.commit()
    print("Load: Data successfully loaded into 'users' table.")

except Exception as e:
    session.rollback()
    print(f"SQLAlchemy Bulk Load failed: {e}")
finally:
    session.close()
```

ran commands -

```bash
python load_bulk.py
```

![SQLAlchemy Bulk Data Loading](screenshorts/Screenshot%202025-12-05%20at%2011.31.02 AM.png)

![Data Loading Verification](screenshorts/Screenshot%202025-12-05%20at%2011.34.24 AM.png)

![Final Database Check](screenshorts/Screenshot%202025-12-05%20at%2011.39.50 AM.png)

![Container Status Check](screenshorts/Screenshot%202025-12-05%20at%2011.49.37 AM.png)

![Final Results Summary](screenshorts/Screenshot%202025-12-05%20at%2011.53.36 AM.png)
