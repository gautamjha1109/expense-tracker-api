import json
from pathlib import Path

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)
DATA_FILE = Path(__file__).resolve().parent.parent / "expenses.json"


def reset_storage() -> None:
    DATA_FILE.write_text(json.dumps([], indent=2), encoding="utf-8")


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_list_expenses() -> None:
    reset_storage()

    response = client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 12.5,
            "category": "Food",
            "date": "2026-08-01",
        },
    )
    assert response.status_code == 201

    list_response = client.get("/expenses")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1


def test_delete_expense() -> None:
    reset_storage()

    response = client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 12.5,
            "category": "Food",
            "date": "2026-08-01",
        },
    )
    assert response.status_code == 201
    expense_id = response.json()["id"]

    delete_response = client.delete(f"/expenses/{expense_id}")
    assert delete_response.status_code == 204

    list_response = client.get("/expenses")
    assert list_response.status_code == 200
    assert list_response.json() == []


def test_category_total() -> None:
    reset_storage()

    client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 12.5,
            "category": "Food",
            "date": "2026-08-01",
        },
    )
    client.post(
        "/expenses",
        json={
            "title": "Dinner",
            "amount": 25.0,
            "category": "Food",
            "date": "2026-08-01",
        },
    )

    response = client.get("/expenses/category-total", params={"category": "Food"})
    assert response.status_code == 200
    assert response.json() == {"category": "Food", "total": 37.5}
