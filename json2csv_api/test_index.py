from typing import Generator
from flask.testing import FlaskClient
from dotenv import load_dotenv
import pytest
import json

from json2csv_api import create_app


@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    load_dotenv()
    app = create_app({'TESTING': True})

    with app.test_client() as client:
        yield client

def test_index(client: FlaskClient) -> None:
    response = client.get('/')
    try:
        data = json.loads(response.data)
        assert 'body' in data
        assert 'message' in data['body']
        assert "Hello World!" == data['body']['message']
    finally:
        response.close()
