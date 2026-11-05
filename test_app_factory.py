# tests/test_app_factory.py
from flask import Flask

from app import create_app

def test_create_app_returns_flask_instance():
    """TC-US000-002: create_app() returns a Flask instance."""
    app = create_app()
    assert isinstance(app, Flask)

def test_app_returns_redirect_for_home_route():
    """TC-US000-003: Home route redirects to /tasks/new.

    S4_2 update: home route now exists and redirects to add task form.
    Previously this test checked for 404 (no home route defined).
    The test name and assertion are updated to reflect current behavior.
    """
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 302
    assert "/tasks/new" in response.location
