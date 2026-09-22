from Controller.Emp_Controller import add_emp, update_emp, delete_emp, get_emp
from Model.Emp_model import Employee_details
from Model.Emp_Update import Employee_Update
from fastapi import APIRouter

route = APIRouter()

@route.post("/addEmp")
def add_data(data:Employee_details):
    return add_emp(data)

@route.put("/edit/{id}")
def update_data(id:int, data:Employee_Update):
    return update_emp(id, data)

@route.delete("/delete/{id}")
def del_data(id:int):
    return delete_emp(id)

@route.get("/getAll")
def get_data():
    return get_emp()