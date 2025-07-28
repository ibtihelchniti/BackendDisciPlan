from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# URL de la base de données (MySQL ici)
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:rooy@localhost/disci_plan_db")

# Création du moteur SQLAlchemy
engine = create_engine(DATABASE_URL)

# Générateur de session DB utilisé dans les routes
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe mère des modèles SQLAlchemy
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()