import pytest
from fastapi.testclient import TestClient
from app.api.router import app
from app.model.model import BlueViGptModel
from app.api.http_status import HTTPStatus

@pytest.fixture(scope="module")
def client():
    app.state.model = BlueViGptModel()
    app.state.model.load_model()
    with TestClient(app) as client:
        yield client

def test_chat_endpoint(client):
    # Call the endpoint with a sample message using the updated key 'prompt'
    response = client.post("/chat", json={"prompt": "test_message"})

    # Assert the response status code is 200
    assert response.status_code == HTTPStatus.OK.value

    # Get the JSON response
    json_response = response.json()

    # Assert the presence of expected keys in the response
    assert "response" in json_response
    assert isinstance(json_response["response"], str) 
    assert json_response["response"] != "" 
