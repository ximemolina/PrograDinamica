from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestSeries:

    # ----------------------------------- pruebas del backend de series deportivas ----------------------------------- 
    def test_series_deportivas1(self):
        response = client.post(
            "/api/series-deportivas",
            json={
                "juegos": 3,
                "ph": 0.6,
                "pr": 0.4,
                "formato": [True, False, True],
            },
        )

        assert response.status_code == 200
        assert response.json() == {"resultado": [["-", 1, 1], [0, 0.6, 0.76], [0, 0.24, 0.552]]}

    def test_series_deportivas2(self):
        response = client.post(
            "/api/series-deportivas",
            json={
                "juegos": 7,
                "ph": 0.57,
                "pr": 0.49,
                "formato": [True, True, False, False, False, True,True],
            },
        )

        assert response.status_code == 200
        assert response.json() == {"resultado": [["-",1,1,1,1],[0,0.57,0.8151,0.9057,0.9519],[0,0.3249,0.5651,0.732,0.8398],[0,0.1592,0.3581,0.5413,0.7114],[0,0.078,0.2152,0.4011,0.578]]}

    def test_series_deportivas3(self):
        response = client.post(
            "/api/series-deportivas",
            json={
                "juegos": 7,
                "ph": 0.55,
                "pr": 0.55,
                "formato": [True, True, True, False, False, False, True],
            },
        )

        assert response.status_code == 200
        assert response.json() == {"resultado": [["-",1,1,1,1],[0,0.55,0.7975,0.9089,0.959],[0,0.3025,0.5748,0.7586,0.8688],[0,0.1664,0.391,0.5932,0.7448],[0,0.0915,0.2562,0.4415,0.6083]]}     
        

    def test_series_deportivas_negativo1(self):
        response = client.post(
            "/api/series-deportivas",
            json={
                "juegos": -1,
                "ph": 0.6,
                "pr": 0.4,
                "formato": [True, False],
            },
        )

        assert response.status_code == 200
        assert response.json() == {"error": "Los juegos deben ser un número impar de 1 a 11"}

    def test_series_deportivas_negativo2(self):
        response = client.post(
            "/api/series-deportivas",
            json={
                "juegos": 7,
                "ph": -1,
                "pr": 0.4,
                "formato": [True, True, False, False, False, True, True],
            },
        )

        assert response.status_code == 200
        assert response.json() == {"error": "Las probabilidades deben ser un número del 0 al 1"}