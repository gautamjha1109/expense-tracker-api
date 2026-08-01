from fastapi import FastAPI

from src.routes import router

app = FastAPI(
    title="Smart Expense Tracker API",
    description="A REST API for tracking expenses with JSON storage.",
    version="1.0.0",
)

app.include_router(router)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return a simple health status for the API."""
    return {"status": "ok"}
