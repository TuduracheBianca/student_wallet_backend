from sqlalchemy.orm import Session
from app.models.expense import ExpenseDB
from app.domain.expense import Expense

def get_expenses(db: Session):
    return db.query(ExpenseDB).all()

def create_expense(db: Session, expense: Expense):
    db_expense = ExpenseDB(
        name=expense.name,
        amount=expense.amount,
        category=expense.category
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense