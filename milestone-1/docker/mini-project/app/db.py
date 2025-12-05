from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator


DATABASE_URL = "postgresql://admin:qwerty@postgres_db:5432/employees"

Base = declarative_base()  # SQLAlchemy Base class for models
engine = create_engine(DATABASE_URL)  # Create the database engine
SessionLocal = sessionmaker(bind=engine)  # Create a configured "Session" class


def get_db_session() -> Generator:
    """Dependency to get a database session."""

    db = SessionLocal()
    print("Database connection established.")
    try:
        yield db
    finally:
        db.close()
        print("Database connection closed.")
