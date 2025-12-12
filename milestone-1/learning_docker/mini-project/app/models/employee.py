from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()


class Employee(base):
    """Model for the employees table."""

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)

    def __repr__(self):
        return f"Employee(id={self.id}, name={self.name}, department={self.department})"
