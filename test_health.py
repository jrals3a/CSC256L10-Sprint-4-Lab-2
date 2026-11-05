from app import create_app

def test_health_check():
    """TC-US001-001: GET /api/health returns 200 + {"status": "ok"}."""
    app = create_app()
    client = app.test_client()
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
