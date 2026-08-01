from fastapi import APIRouter, HTTPException, Query, status

from src.models import Expense, ExpenseCreate
from src.storage import load_expenses, save_expenses

router = APIRouter()


@router.post("/expenses", response_model=Expense, status_code=status.HTTP_201_CREATED)
def create_expense(expense_data: ExpenseCreate) -> Expense:
    """Create a new expense and persist it."""
    expenses = load_expenses()
    new_expense = Expense(
        id=len(expenses) + 1,
        title=expense_data.title,
        amount=expense_data.amount,
        category=expense_data.category,
        date=expense_data.date,
    )
    expenses.append(new_expense)
    save_expenses(expenses)
    return new_expense


@router.get("/expenses", response_model=list[Expense])
def list_expenses(category: str | None = Query(default=None)) -> list[Expense]:
    """Return all expenses, optionally filtered by category."""
    expenses = load_expenses()
    if category:
        expenses = [expense for expense in expenses if expense.category.lower() == category.lower()]
    return expenses


@router.get("/expenses/total")
def get_total_expenses() -> dict[str, float]:
    """Return the sum of all expenses."""
    expenses = load_expenses()
    total = sum(expense.amount for expense in expenses)
    return {"total": round(total, 2)}


from src.models import CategoryTotal


@router.get("/expenses/category-total", response_model=CategoryTotal)
def get_category_total(category: str) -> CategoryTotal:
    """Return the total for a specific category."""
    expenses = load_expenses()
    total = sum(
        expense.amount for expense in expenses if expense.category.lower() == category.lower()
    )
    return CategoryTotal(category=category, total=round(total, 2))


@router.delete("/expenses/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(expense_id: int) -> None:
    """Delete an expense by ID."""
    expenses = load_expenses()
    remaining = [expense for expense in expenses if expense.id != expense_id]
    if len(remaining) == len(expenses):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")

    save_expenses(remaining)
