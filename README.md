# PrograDinamica

App web para acceder a algoritmos de programación dinámica. El frontend es una aplicación React con Vite y el backend es una API en FastAPI.

## Requisitos

- [Node.js](https://nodejs.org/) con npm
- [Python 3.11](https://www.python.org/downloads/)

## Instalación

Desde la raíz del proyecto:

```bash
npm install
npm install --prefix frontend
```

Crea un entorno virtual para el backend e instala sus dependencias.

En Windows (PowerShell):

```powershell
python -m venv backend\.venv
backend\.venv\Scripts\Activate.ps1
python -m pip install -r backend\requirements.txt
```

En macOS o Linux:

```bash
python3 -m venv backend/.venv
source backend/.venv/bin/activate
python -m pip install -r backend/requirements.txt
```

Si PowerShell bloquea la activación del entorno, ejecuta una vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Ejecución

Activa el entorno virtual y, desde la raíz, levanta frontend y backend juntos.

Si usas pyenv, no hace falta activar un entorno virtual: el script del backend entra a `backend` y toma la versión de `backend/.python-version` (3.11.0). Esa versión tiene que estar instalada (`pyenv install 3.11.0`).

```bash
npm run dev
```

| Servicio | Dirección |
| --- | --- |
| Frontend | http://localhost:5173 |
| Backend | http://127.0.0.1:8000 |
| Documentación de la API | http://127.0.0.1:8000/docs |

Para detener ambos procesos, presiona `Ctrl+C` en esa terminal.

### Por separado

Con el entorno virtual activado:

```bash
npm run dev:frontend
npm run dev:backend
```

`dev:frontend` inicia Vite. `dev:backend` inicia Uvicorn con recarga automática en el puerto 8000.

## Pruebas

Los tests están en `tests/` y se corren con pytest. No hace falta levantar el servidor: `TestClient` importa la app de FastAPI y le manda la petición en el mismo proceso.

Desde la raíz del proyecto, con las dependencias del backend ya instaladas:

En Windows (PowerShell):

```powershell
backend\.venv\Scripts\python.exe -m pytest tests -v
```

En macOS o Linux:

```bash
backend/.venv/bin/python -m pytest tests -v
```

Si el entorno virtual ya está activado, basta con:

```bash
python -m pytest tests -v
```

pytest solo recoge archivos llamados `test_*.py` o `*_test.py`. `-v` muestra el nombre de cada prueba.
