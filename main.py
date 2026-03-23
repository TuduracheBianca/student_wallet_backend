import models
from database import engine, SessionLocal, Base
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends
from pydantic import BaseModel # for creating data models

app = FastAPI() # initialize the FastAPI application
models.Base.metadata.create_all(bind=engine) # create the database tables

# endpoint to check if the app is running (health check)
@app.get("/")
def read_root():
    return {"message": "Student Wallet API is running"}

class Expense(BaseModel):
    name: str
    amount: float
    category: str
    date: Optional[datetime] = None
    int: Optional[int] = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/add-expense/") # endpoint for adding an expense
def add_expense(expense: Expense, db: Session = Depends(get_db)):
    new_expense = models.ExpenseDB(
        name=expense.name,
        amount=expense.amount,
        category=expense.category,
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return {"message": "Expense added successfully", "expense": new_expense}

@app.get("/expenses/") # endpoint to retrieve all expenses
def get_all_expenses(db:Session=Depends(get_db)):
    expenses= db.query(models.ExpenseDB).all()
    return expenses
