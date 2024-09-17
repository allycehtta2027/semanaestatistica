from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

OAuth2PasswordBearer(tokenURL="token")

@app.get("/")
def index():
    return{"mensagem": "Olá mundo!"}
@app.post("/token")
async def logar(data: OAuth2PasswordRequestForm = Depends()):
    if data.username == "kaua" and data.password == "senai123":
        return {"acess_token": "supersecreto","token_tape":"bearer"}
    raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="credenciais inválidas")


    