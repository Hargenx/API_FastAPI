from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from utils import gerar_descricao_produto


app = FastAPI()

class Ordem(BaseModel):
    produto: str
    unidade: int

class Produto(BaseModel):
    nome: str
    nota: str

@app.get("/ok", tags=["status"])
async def ok_endpoint():
    try:
        return {"messagem": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ordens", tags=["ordens"])
async def fazer_encomenda(produto: str, unidade: int):
    try:
        return {"message": f"{unidade} unidade(s) de {produto} feita(s) com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ordens_pydantic", tags=["ordens"])
async def fazer_encomenda(ordem: Ordem):
    try:
        return {"message": f"{ordem.unidade} unidade(s) de {ordem.produto} feita com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


'''@app.post("/produto_descricao", tags=["descricao"])
async def gerar_descricao_produto(produto: Produto):
    try:
        descricao = await gerar_descricao_produto(produto)
        return {"produto_descricao": descricao}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))'''

from typing import Callable
async def gerar_descricao_produto_handler(produto: Produto) -> str:
    try:
        return gerar_descricao_produto(produto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/produto_descricao", tags=["descricao"])
async def produto_descricao_handler(descricao_handler: Callable[[Produto], str] = Depends(gerar_descricao_produto_handler)):
    return {"produto_descricao": descricao_handler}