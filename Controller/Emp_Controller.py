from Model.Emp_model import Employee_details
from DataBase.Db_Conn import col
from Model.Emp_Update import Employee_Update

def add_emp(data:Employee_details):
    
    info = {
            "id" : data.id,
            "name" : data.name,
            "dept" : data.dept,
            "post" : data.post,
            "mail" : data.mail,
            "phone" : data.phone, 
            "salary" : data.salary,
            "joining_date" : data.joining_date.isoformat(),
            "address" : data.address,
            "gender" : data.gender,
            "age" : data.age,
            "experience" : data.experience,
            "employment_type" : data.employment_type,
            "status" : data.status
    }
    
    col.insert_one(info)
    
    return{"message":"Emp data inserted successfully..!"}

def update_emp(id:int, data:Employee_Update):
        update_data = {}
        
        if data.name is not None:
                update_data["name"] = data.name
                
        if data.dept is not None:
                update_data["dept"] = data.dept
                
        if data.post is not None:
                update_data["post"] = data.post
                
        if data.mail is not None:
                update_data["mail"] = data.mail
                
        if data.phone is not None:
                update_data["phone"] = data.phone
                        
        if data.salary is not None:
                update_data["salary"] = data.salary
                        
        if data.joining_date is not None:
                update_data["joining_date"] = (
                        data.joining_date.isoformat()
                        if data.joining_date
                        else None
                )
                
        if data.address is not None:
                update_data["address"] = data.address
                
        if data.gender is not None:
                update_data["gender"] = data.gender
                        
        if data.age is not None:
                update_data["age"] = data.age
                        
        if data.experience is not None:
                update_data["experience"] = data.experience
                        
        if data.employment_type is not None:
                update_data["employment_type"] = data.employment_type
                                
        if data.status is not None:
                update_data["status"] = data.status
                
        if not update_data:
                return{"message":"No data to update"}
        
        res = col.update_one(
                {"id":id},
                {"$set":update_data}
        )
        
        if res.matched_count == 0:
                return {"message": "Employee not found"}

        return {"message":"Employee Updated"}

def delete_emp(id:int):
        
        col.delete_one({"id":id})
        
        return{"message":"Employee deleted..!"}


def get_emp():
        return list(col.find({},{"_id":0}))