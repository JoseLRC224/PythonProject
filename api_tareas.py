from fastapi import FastAPI
from typing import List

app = FastAPI()

# Esta es nuestra lista en memoria (se borra si reinicias el servidor)
tareas = ["Aprender FastAPI", "Configurar Fedora", "Subir código a GitHub"]

@app.get("/tareas")
def obtener_tareas():
    """Muestra todas las tareas actuales"""
    return {"tus_tareas": tareas}

@app.post("/tareas/{nueva_tarea}")
def agregar_tarea(nueva_tarea: str):
    """Agrega una tarea nueva a la lista"""
    tareas.append(nueva_tarea)
    return {"mensaje": "Tarea agregada con éxito", "lista_actualizada": tareas}
