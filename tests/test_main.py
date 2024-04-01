from http import client
from fastapi.testclient import TestClient
from fastapi_helloworld.main import app

def test_root_path():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello" : "world" }
def test_piaic():
    client = TestClient(app=app)
    response = client.get("/piaic/")
    assert response.status_code == 200
    assert response.json() == {"company" : "pakistan" } 