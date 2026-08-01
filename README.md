# Smart Expense Tracker API

A REST API built with FastAPI and JSON file storage to manage personal expenses.

## Features

- Add expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate category total
- Delete expense

## Tech stack

- Python 3.14
- FastAPI
- Uvicorn
- Pytest
- JSON file storage

## Project structure

```
expense-tracker-api/
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── expenses.json
├── .gitignore
├── .github/
│   └── workflows/
│       └── python-app.yml
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── storage.py
│   └── routes.py
└── tests/
    ├── __init__.py
    └── test_api.py
```

## Installation

```bash
cd expense-tracker-api
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run locally

```bash
python -m uvicorn src.main:app --reload
```

Open the API docs at `http://127.0.0.1:8000/docs`.

## API endpoints

- `POST /expenses` — create a new expense
- `GET /expenses` — list expenses
- `GET /expenses?category=Food` — filter by category
- `GET /expenses/total` — calculate total expenses
- `GET /expenses/category-total?category=Food` — calculate total for a category
- `DELETE /expenses/{expense_id}` — delete an expense

## Testing

```bash
python -m pytest -q
```

## GitHub Actions

A workflow is included at `.github/workflows/python-app.yml` to run tests on push and pull requests.
