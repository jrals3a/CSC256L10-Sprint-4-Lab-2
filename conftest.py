# tests/conftest.py
import pytest

from app import create_app

# ── Fixtures ────────────────────────────────────────────────────────────────

@pytest.fixture
def client():
    """Flask test client using real TaskService and FileTaskRepository."""
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def db_client():
    """Flask test client wired to DatabaseTaskRepository with in-memory SQLite.

    Use this fixture for tests that exercise the database layer or UI routes
    when the database backend is active.

    Each test gets a fresh :memory: database — no cleanup needed.
    engine.dispose() is called after each test to explicitly release
    all SQLAlchemy connections and prevent ResourceWarning.
    """
    app = create_app(
        use_db=True,
        config={"TESTING": True, "DATABASE_URL": "sqlite:///:memory:"},
    )
    with app.test_client() as client:
        yield client
    # Explicitly dispose the SQLAlchemy engine after each test
    app.task_service._repository._engine.dispose()  # type: ignore[attr-defined]


@pytest.fixture(autouse=True)
def reset_tasks(client):
    """
    Resets task state before and after every test.

    Uses /api/tasks/reset endpoint (calls TaskService.clear_tasks()).
    This fixture works regardless of which repository backend is active —
    the reset route delegates to whatever repository is injected.
    """
    client.post("/api/tasks/reset")
    yield
    client.post("/api/tasks/reset")

