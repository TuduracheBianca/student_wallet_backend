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

def delete_expense(db:Session, expense_id:int):
    expense= db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()
    if expense:
        db.delete(expense)
        db.commit()
        return True
    return False

def update_expense(db:Session,expense_id:int, update_data:Expense):
    expense=db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()
    if expense:
        expense.name=update_data.name
        expense.amount=update_data.amount
        expense.category=update_data.category
        db.commit()
        db.refresh(expense)
        return expense
    return None
