from pydantic import BaseModel, Field
from typing import Optional


class Employee_Response(BaseModel):
    """Schema for employee response."""

    id: int
    name: str
    department: str

    class Config:
        orm_mode = True

    def __repr__(self):
        return f"Employee_Response(id={self.id}, name={self.name}, department={self.department})"


class All_Employees_Response(BaseModel):
    """Schema for all employees response."""

    employees: list[Employee_Response]

    def __repr__(self):
        return f"All_Employees_Response(employees={self.employees})"


class Add_Employee(BaseModel):
    """Schema for adding a new employee."""

    name: str = Field(..., description="Name of the employee")
    department: str = Field(..., description="Department where the employee works")
    id: Optional[int] = None

    def __repr__(self):
        return f"Add_Employee(name={self.name}, department={self.department}, id={self.id})"
