"""
Example of receiving a client request body
"""

from _util import app
from pydantic import BaseModel


class Car(BaseModel):
    wheels: int = 4
    color: str = "Red"
    top_speed: float = 144.00


@app.post("/cars")
async def create_car(car: Car):
    return car


@app.get("/cars")
async def get_all_cars():
    return [Car()]


"""
(.venv)  si@ubuntu  ~/workspaces/introduction-to-fastapi   main ±  curl -X POST -H "Content-Type: application/json" -d '{"wheels": 3}' localhost:8000/cars     
{"wheels":3,"color":"Red","top_speed":144.0}

(.venv)  si@ubuntu  ~/workspaces/introduction-to-fastapi   main ±  curl localhost:8000/cars                                                                    
[{"wheels":4,"color":"Red","top_speed":144.0}]
"""