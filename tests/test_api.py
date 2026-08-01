from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_list_expenses() -> None:
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
    assert len(list_response.json()) >= 1
