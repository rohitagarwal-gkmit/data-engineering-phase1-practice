import pandas as pd
from sqlalchemy import create_engine

# connection string for the database inside the container
DATABASE_URL = "postgresql://postgres:qwerty@localhost:5432/test_db"
engine = create_engine(DATABASE_URL)

# the CSV file
df = pd.read_csv("user_data.csv")

# Load the DataFrame into the SQL table
try:
    df.to_sql(name="users", con=engine, if_exists="replace", index=False)
    print("Pandas: Data successfully loaded into 'users' table.")
except Exception as e:
    print(f"failed: {e}")
