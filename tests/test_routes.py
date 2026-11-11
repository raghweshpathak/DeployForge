from app import create_app
from app.config import TestingConfig


def test_home_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["application"] == "DeployForge"
    assert response.json["status"] == "running"
    assert response.content_type == "application/json"


def test_health_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
    assert response.content_type == "application/json"


def test_unknown_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/invalid")

    assert response.status_code == 404


def test_testing_configuration():
    app = create_app(TestingConfig)

    assert app.config["TESTING"] is True
    assert app.config["DEBUG"] is False
