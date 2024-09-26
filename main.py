from fastapi import FastAPI, Request, HTTPException
from database import DB_SYSTEM
from models import Aluno
import json

bd = DB_SYSTEM()
app = FastAPI()

@app.get("/aluno/list")
def getAll():
    return bd.get_entities()

@app.get("/aluno/{id}", status_code = 200)
def get_by_id(id : int):
    aluno = bd.get_entity_by_id(id)
    if(aluno):
        return aluno
    raise HTTPException(status_code=404, detail="Aluno não Encontrado!")

@app.post("/aluno/new", status_code = 201)
async def create(request : Request):
    body = await request.body()
    body_json = json.loads(body)

    if(body_json['name'] and body_json['email']):
        aluno = Aluno(body_json['name'], body_json['email'])
        bd.new_data(aluno)
        return aluno
    raise HTTPException(status_code=409, detail="Aluno já Existe!")

@app.put("/aluno/update/{id}", status_code = 201)
async def update(id : int, request : Request):
    body = await request.body()
    body_json = json.loads(body)

    alunos = bd.get_entities()
    for aluno in alunos:
        if(aluno.id == id):
            if(body_json['email']):
                aluno.email = body_json['email']
            if(body_json['name']):
                aluno.name = body_json['name']
            return aluno
    raise HTTPException(status_code=404, detail="Aluno não Encontrado!")

@app.delete("/aluno/delete/{id}", status_code = 204)
def delete(id : int):
    alunos = bd.get_entities()
    for aluno in alunos:
        if(aluno.id == id):
            alunos.remove(aluno)
            return {"message" : "removido"}
    raise HTTPException(status_code=404, detail="Aluno não Encontrado!")


