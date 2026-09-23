from fastapi import FastAPI
from Routes.Emp_Routes import route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://emp-mgmt-project-divya.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route)

@app.get("/")
def greet():
    return {"message":"Project for Employee Management..."}