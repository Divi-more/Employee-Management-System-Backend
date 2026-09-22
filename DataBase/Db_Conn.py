from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

Mongo_URI = os.getenv("Mongo_URL")

conn = MongoClient(Mongo_URI)

# conn = MongoClient("mongodb://localhost:27017/")
db = conn["Employees_01"]

col = db["Emp_Info"]

