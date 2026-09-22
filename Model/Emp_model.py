from pydantic import BaseModel, Field, EmailStr
from typing import Annotated
from datetime import date

class Employee_details(BaseModel):
    id: Annotated[int, Field(title="Enter Employee ID: ")]
    name: Annotated[str, Field(title="Enter employee name: ")]
    dept: Annotated[str, Field(title="Enter department: ")]
    post: Annotated[str, Field(title="Enter post/designation: ")]
    mail: Annotated[EmailStr, Field(title="Enter email ID: ")]
    phone: Annotated[str, Field(title="Enter phone number: ")]
    salary: Annotated[int, Field(title="Enter salary: ")]
    joining_date: Annotated[date, Field(title="Enter joining date: ")]
    address: Annotated[str, Field(title="Enter address: ")]
    gender: Annotated[str, Field(title="Enter gender: ")]
    age: Annotated[int, Field(title="Enter age: ")]
    experience: Annotated[int, Field(title="Enter years of experience: ")]
    employment_type: Annotated[str, Field(title="Enter employment type: ")]
    status: Annotated[str, Field(title="Enter employee status: ")]    