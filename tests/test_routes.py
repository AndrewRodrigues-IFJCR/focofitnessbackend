from fastapi.testclient import TestClient

from focofitnessbackend.app import app

client = TestClient(app)


def test_ping_route():
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json() == {'message': 'pong'}


def test_signup_route():
    response = client.post(
        url='/auth/signup',
        content={'email': 'example@gmail.com', 'password': 'Senha123'},
    )

    assert response.status_code == 201
    assert response.json()
