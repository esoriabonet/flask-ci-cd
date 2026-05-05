import pytest
from unittest.mock import patch, MagicMock
import app as flask_app


@pytest.fixture
def client():
    flask_app.app.config["TESTING"] = True
    with flask_app.app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_get_items(client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [{"id": 1, "name": "test"}]
    mock_conn.cursor.return_value = mock_cursor

    with patch("app.get_db_connection", return_value=mock_conn):
        response = client.get("/items")

    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert data[0]["name"] == "test"


def test_add_item(client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    with patch("app.get_db_connection", return_value=mock_conn):
        response = client.post(
            "/items",
            json={"name": "nouveau"},
            content_type="application/json"
        )

    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Item ajouté"