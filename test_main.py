from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health_is_defensive():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "mode": "defensive-awareness"}


def test_capabilities_disable_collection_and_control():
    body = client.get("/api/v1/capabilities").json()
    assert body["collection"] is False
    assert body["remote_control"] is False
    assert body["browser_media_access"] is False


def test_sensitive_api_is_explicitly_disabled():
    response = client.post("/api/v1/exfiltrate", json={"anything": "ignored"})
    assert response.status_code == 410
    assert response.json()["reason"].startswith("DAF defensive mode")


def test_security_headers_are_present():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["x-frame-options"] == "DENY"
    assert "camera=()" in response.headers["permissions-policy"]
    assert "connect-src 'none'" in response.headers["content-security-policy"]


def test_page_contains_no_collection_or_media_api():
    page = client.get("/").text
    assert "getUserMedia" not in page
    assert "getDisplayMedia" not in page
    assert "navigator.geolocation" not in page
    assert "fetch(" not in page
