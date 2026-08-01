from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class Expense(BaseModel):
    """Represents an expense entry."""

    id: int
    title: str = Field(min_length=1, max_length=100)
    amount: float = Field(gt=0)
    category: str = Field(min_length=1, max_length=50)
    date: date


class ExpenseCreate(BaseModel):
    """Payload used when creating a new expense."""

    title: str = Field(min_length=1, max_length=100)
    amount: float = Field(gt=0)
    category: str = Field(min_length=1, max_length=50)
    date: date
