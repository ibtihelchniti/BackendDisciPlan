from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import monthly_goals  # Router = fichier qui contient les routes de l'API

app = FastAPI()

# Permet au frontend (Angular) d'accéder à ce backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# On ajoute les routes à l'application
app.include_router(monthly_goals.router, prefix="")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}
