from fastapi.testclient import TestClient
from main_app import app

client = TestClient(app)


def test_predict():
    response = client.post("/printData", json={"age": 21, "name": "hager", "fav_numbers":[8, 8]})
    assert response.status_code == 200
    assert response.json() == [2]
