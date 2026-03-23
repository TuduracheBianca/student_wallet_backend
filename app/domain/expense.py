from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Expense(BaseModel):
    id: Optional[int] = None
    name: str
    amount: float
    category: str
    date: Optional[datetime] = None