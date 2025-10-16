# backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://neondb_owner:npg_EjfmxRz2p3kn@ep-late-fog-adcm59c3-pooler.c-2.us-east-1.aws.neon.tech/cotizacion?sslmode=require&channel_binding=require'

engine = create_engine(
    DATABASE_URL,
    pool_size=10,        # cantidad de conexiones simultáneas
    max_overflow=20,     # conexiones extra si se saturan
    pool_pre_ping=True   # evita conexiones muertas
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Esto es lo que estabas intentando importar en models.py
Base = declarative_base()

# función para obtener sesión en FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
