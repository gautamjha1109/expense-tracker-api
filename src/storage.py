import json
from pathlib import Path

from src.models import Expense

DATA_FILE = Path(__file__).resolve().parent.parent / "expenses.json"


def load_expenses() -> list[Expense]:
    """Load all expenses from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as handle:
            raw_data = json.load(handle)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return []

    if not isinstance(raw_data, list):
        return []

    return [Expense(**item) for item in raw_data]


def save_expenses(expenses: list[Expense]) -> None:
    """Persist the full list of expenses to the JSON file."""
    payload = [expense.model_dump(mode="json") for expense in expenses]

    with DATA_FILE.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
