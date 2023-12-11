from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_read_main():
    responce = client.get("/")
    assert responce.status_code == 200
    assert responce.json() == {"message": "OK"}


def test_translate_word():
    responce = client.post("/translate/", json={"text": "привет."})
    json_data = responce.json()
    assert responce.status_code == 200
    assert json_data["Translated text"] == "Hey."


def test_translate_pr():
    responce = client.post("/translate/", json={"text": "Коля и Арсен и инженерия."})
    json_data = responce.json()
    assert responce.status_code == 200
    assert json_data["Translated text"] == "Kolya and Arsen and Engineering."



