from fastapi.testclient import TestClient

from app.main import app


def test_security_headers_are_present():
    response = TestClient(app).get("/")

    assert response.headers["x-content-type-options"] == "nosniff"
    assert response.headers["referrer-policy"] == "strict-origin-when-cross-origin"
    assert "x-request-id" in response.headers
