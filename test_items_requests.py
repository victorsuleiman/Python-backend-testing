import requests

BASE = "http://127.0.0.1:8000"

def test_creating_items(): 
    r = requests.post(f"{BASE}/items", json={"id": 1, "name": "A"})
    assert r.status_code == 201

def test_list_items():
    r = requests.get(f"{BASE}/items")
    assert r.status_code == 200

def test_list_items_by_id():
    r = requests.get(f"{BASE}/items/1")
    assert r.status_code == 200
    item = r.json()
    assert item["id"] == 1 and item["name"] == "A"
    
def test_update_list_item():
    r = requests.put(f"{BASE}/items/1", json={"id": 1, "name": "AA"})
    assert r.status_code == 200 and r.json()["name"] == "AA"

def test_delete_list_item():
    r = requests.delete(f"{BASE}/items/1")
    assert r.status_code == 204

def test_not_found_after_delete():
    r = requests.get(f"{BASE}/items/1")
    assert r.status_code == 404

def test_conflict():
    r1 = requests.post(f"{BASE}/items", json={"id": 2, "name": "B"})
    r2 = requests.post(f"{BASE}/items", json={"id": 2, "name": "B"})
    assert r2.status_code == 409

def test_not_found():
    r = requests.get(f"{BASE}/items/999")
    assert r.status_code == 404



