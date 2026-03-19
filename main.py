from FastAPI import FastAPI
from pydantic import BaseModel #pentru crearea modelelor de date

app = FastAPI()#initializam aplicatia FastAPI

#am creat un endpoint pentru a verifica daca functioneaza aplicatia(adresa web)
#@app.get("/")
#def read_root():
#    return {"mesaj": "student_wallet functioneaza"}

class Cheltuiala(BaseModel):
    id: int
    name:str
    sum: float
    category: str
    #date: str

cheltuieli = [] #lista pentru a stoca cheltuielile
@app.post("/adauga/") #endpoint pentru adaugarea unei cheltuieli
def adauga_cheltuiala(cheltuiala:Cheltuiala):
    cheltuieli.append(cheltuiala)
    return {"mesaj": "Cheltuiala adaugata cu succes"}