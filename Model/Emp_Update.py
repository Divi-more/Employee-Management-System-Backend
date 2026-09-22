from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Optional
from datetime import date

class Employee_Update(BaseModel):
    id: Annotated[Optional[int], Field(title="Enter Employee ID: ",default=None)]
    name: Annotated[Optional[str], Field(title="Enter employee name: ",default=None)]
    dept: Annotated[Optional[str], Field(title="Enter department: ",default=None)]
    post: Annotated[Optional[str], Field(title="Enter post/designation: ",default=None)]
    mail: Annotated[Optional[EmailStr], Field(title="Enter email ID: ",default=None)]
    phone: Annotated[Optional[str], Field(title="Enter phone number: ",default=None)]
    salary: Annotated[Optional[int], Field(title="Enter salary: ",default=None)]
    joining_date: Annotated[date, Field(title="Enter joining date: ",default=None)]
    address: Annotated[Optional[str], Field(title="Enter address: ",default=None)]
    gender: Annotated[Optional[str], Field(title="Enter gender: ",default=None)]
    age: Annotated[Optional[int], Field(title="Enter age: ",default=None)]
    experience: Annotated[Optional[int], Field(title="Enter years of experience: ",default=None)]
    employment_type: Annotated[Optional[str], Field(title="Enter employment type: ",default=None)]
    status: Annotated[Optional[str], Field(title="Enter employee status: ",default=None)]    