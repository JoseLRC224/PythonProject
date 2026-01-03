from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "mensaje": "¡Bloqueo de desarrollador superado!",
        "usuario": "JoseLRC224",
        "estado": "Activo en Fedora"
    }

@app.get("/status")
def get_status():
    return {"status": "Todo funcionando al 100%"}
