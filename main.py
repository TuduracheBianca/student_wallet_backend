from fastapi import FastAPI
from pydantic import BaseModel # for creating data models

app = FastAPI() # initialize the FastAPI application

# endpoint to check if the app is running (health check)
@app.get("/")
def read_root():
    return {"message": "Student Wallet API is running"}

class Expense(BaseModel):
    id: int
    name: str
    amount: float
    category: str
    # date: str

expenses = [] # list to store the expenses

@app.post("/add-expense/") # endpoint for adding an expense
def add_expense(expense: Expense):
    expenses.append(expense)
    return {"message": "Expense added successfully"}

@app.get("/expenses/") # endpoint to retrieve all expenses
def get_all_expenses():
    return expenses