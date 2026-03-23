from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base

class ExpenseDB(Base):
    __tablename__ = "expenses"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String)
    amount = Column(Float)
    category = Column(String)
    date=Column(DateTime,default=datetime.now)
