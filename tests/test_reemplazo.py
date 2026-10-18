from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestReemplazo:

    # ----------------------------------- pruebas del backend de reemplazo ----------------------------------- 
    def test_reemplazo1(self):
        response = client.post(
            "/api/reemplazo-equipos",
            json={
                "costoInicial": 500,
                "plazo": 5,
                "vidaUtil": 3,
                "periodos": [
                    { "reventa": 400, "mantenimiento": 30 },
                    { "reventa": 300, "mantenimiento": 40 },
                    { "reventa": 250, "mantenimiento": 60 }
                ]
            },
        )

        assert response.status_code == 200
        assert response.json() == {"resultado": 640, "rutas": [[0,1,2,5],[0,1,4,5],[0,3,4,5]], "tabla": [["t","G(t)","Proximo"],[0,640.0,[1,3]],[1,510.0,[2,4]],[2,380.0,[5]],[3,260.0,[4]],[4,130.0,[5]],[5,0,"fin"]]}

    def test_reemplazo2(self):
        response = client.post(
            "/api/reemplazo-equipos",
            json={
                "costoInicial": 1000,
                "plazo": 4,
                "vidaUtil": 3,
                "periodos": [
                    { "reventa": 700, "mantenimiento": 100},
                    { "reventa": 400, "mantenimiento": 200 },
                    { "reventa": 300, "mantenimiento": 400 }
                ]
            },
        )

        assert response.status_code == 200
        assert response.json() == {"resultado": 1600,"rutas":[[0,1,2,3,4]],"tabla":[["t","G(t)","Proximo"],[0,1600.0,[1]],[1,1200.0,[2]],[2,800.0,[3]],[3,400.0,[4]],[4,0,"fin"]]}

    def test_reemplazo3(self):
        response = client.post(
            "/api/reemplazo-equipos",
            json={
                "costoInicial": 300,
                "plazo": 4,
                "vidaUtil": 4,
                "periodos": [
                    { "reventa": 250, "mantenimiento": 10 },
                    { "reventa": 220, "mantenimiento": 10 },
                    { "reventa": 200, "mantenimiento": 10 },
                    { "reventa": 190, "mantenimiento": 10 }
                ]
            },
        )

        assert response.status_code == 200
        assert response.json() == {"resultado": 150,"rutas":[[0,4]],"tabla":[["t","G(t)","Proximo"],[0,150.0,[4]],[1,130.0,[4]],[2,100.0,[4]],[3,60.0,[4]],[4,0,"fin"]]}     
        

    def test_reemplazo_negativo1(self):
        response = client.post(
            "/api/reemplazo-equipos",
            json={
                "costoInicial": 300,
                "plazo": 4,
                "vidaUtil": 4,
                "periodos": [
                    { "reventa": 250, "mantenimiento": 10 },
                    { "reventa": 220, "mantenimiento": 10 },
                    { "reventa": 200, "mantenimiento": 10 }
                ]
            },
        )

        assert response.status_code == 200
        assert response.json() == {"error": "El arreglo de periodos debe tener una cantidad de elementos igual a VidaUtil"}

    def test_reemplazo_negativo2(self):
        response = client.post(
            "/api/reemplazo-equipos",
            json={
                "costoInicial": 300,
                "plazo": 40,
                "vidaUtil": 4,
                "periodos": [
                    { "reventa": 250, "mantenimiento": 10 },
                    { "reventa": 220, "mantenimiento": 10 },
                    { "reventa": 200, "mantenimiento": 10 },
                    { "reventa": 190, "mantenimiento": 10 }
                ]
            },
        )

        assert response.status_code == 200
        assert response.json() == {"error": "El plazo del proyecto debe ser de 1 a 30"}