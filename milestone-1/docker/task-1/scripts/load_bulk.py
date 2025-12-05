from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import date
import pandas as pd

# Define the base class for declarative class definitions
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
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
    df = pd.read_csv("user_data.csv")
    user_mappings = df.to_dict("records")
    session.bulk_insert_mappings(User, user_mappings)

    session.commit()
    print("Load: Data successfully loaded into 'users' table.")

except Exception as e:
    session.rollback()
    print(f"SQLAlchemy Bulk Load failed: {e}")
finally:
    session.close()
