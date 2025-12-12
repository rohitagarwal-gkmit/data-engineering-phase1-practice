from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from schemas.employee import Employee_Response, Add_Employee, All_Employees_Response
from models.employee import Employee
from db import get_db_session

app = FastAPI()


@app.get("/employee", response_model=All_Employees_Response)
def get_all_employees(db: Session = Depends(get_db_session)):
    """Fetch all employees from the database."""

    employee = db.query(Employee)
    results = employee.all()
    return {"employees": results}


@app.post("/employee", response_model=Employee_Response)
def add_employee(request_data: Add_Employee, db: Session = Depends(get_db_session)):
    """Add a new employee to the database."""

    new_employee = Employee(name=request_data.name, department=request_data.department)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee
