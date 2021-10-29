from typing import Generator
from flask.testing import FlaskClient
import pytest
import json

from json2csv_api import create_app

@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    app = create_app({'TESTING': True})

    with app.test_client() as client:
        yield client

def test_convert(client: FlaskClient) -> None:
    mimetype = 'application/json'
    headers = {'Content-Type': mimetype, 'Accept': mimetype}
    in_data = json.dumps({
        "student1": [
            "view_grades",
            "view_classes"
        ],
        "student2": [
            "view_grades",
            "view_classes"
        ],
        "student3": [
            "view_grades",
            "view_classes"
        ],
        "teacher": [
            "view_grades",
            "change_grades",
            "add_grades",
            "delete_grades",
            "view_classes"
        ]
    })
    out_data = "person,view_grades,change_grades,add_grades," \
        + "delete_grades,view_classes,change_classes,add_classes," \
        + "delete_classes\nstudent1,0,1,0,0,0,1,0,0,0\n" \
        + "student2,0,1,0,0,0,1,0,0,0\nstudent3,0,1,0,0,0,1,0,0,0\n" \
        + "teacher,0,1,1,1,1,1,0,0,0\n"
    response = client.post('/v1/convert', data=in_data, headers=headers)
    try:
        result = response.data.decode('utf8')
        assert out_data == result
    finally:
        response.close()