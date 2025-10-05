from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_crud_flow():
    # create
    r = client.post("/items", json={"id": 1, "name": "A"})
    assert r.status_code == 201
    # list
    r = client.get("/items")
    assert r.status_code == 200 and any(i["id"] == 1 for i in r.json())
    # get
    r = client.get("/items/1")
    assert r.status_code == 200 and r.json()["name"] == "A"
    # update
    r = client.put("/items/1", json={"id": 1, "name": "AA"})
    assert r.status_code == 200 and r.json()["name"] == "AA"
    # delete
    r = client.delete("/items/1")
    assert r.status_code == 204
    # not found after delete
    assert client.get("/items/1").status_code == 404

def test_conflict_and_not_found():
    client.post("/items", json={"id": 2, "name": "B"})
    assert client.post("/items", json={"id": 2, "name": "B"}).status_code == 409
    assert client.get("/items/999").status_code == 404
