from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
    name: str


@app.get("/hello")
async def root():
    return {"message": "Hello World"}


@app.post("/hello")
async def root(person: Person):
    return {"message": f"Hello World {person.name}"}
