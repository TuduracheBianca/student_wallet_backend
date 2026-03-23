from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# Importam uneltele din noile noastre foldere
from app.database.connection import SessionLocal, engine, Base
from app.domain.expense import Expense
from app.repository import expense as repo_expense

# Cream baza de date
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Student Wallet API is running"}

@app.post("/add-expense/")
def add_expense(expense: Expense, db: Session = Depends(get_db)):
    new_expense = repo_expense.create_expense(db=db, expense=expense)
    return {"message": "Expense added successfully", "expense": new_expense}

@app.get("/expenses/")
def get_all_expenses(db: Session = Depends(get_db)):
    return repo_expense.get_expenses(db=db)