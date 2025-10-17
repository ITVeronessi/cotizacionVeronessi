# CORS
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Anestesia, TipoAnestesia, Medicamentos, Insumos, Equipos, TipoCirugia, Cirugia
from schemas import *
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query

app = FastAPI(title="API de Anestesias")
origins = [
    "http://http://0.0.0.0:8000",  # desarrollo
    "https://cotizacionveronessi.onrender.com"  # producción Netlify
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# CRUD: Tipo de Anestesia
# ---------------------------

@app.post("/tipo-anestesia/", response_model=TipoAnestesiaResponse)
def create_tipo_anestesia(data: TipoAnestesiaCreate, db: Session = Depends(get_db)):
    nuevo = TipoAnestesia(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@app.get("/tipo-anestesia/", response_model=List[TipoAnestesiaResponse])
def get_tipos(db: Session = Depends(get_db)):
    return db.query(TipoAnestesia).all()

@app.get("/tipo-anestesia/{id}", response_model=TipoAnestesiaResponse)
def get_tipo(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoAnestesia).filter(TipoAnestesia.idtipoanestecia == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de anestesia no encontrado")
    return tipo

@app.put("/tipo-anestesia/{id}", response_model=TipoAnestesiaResponse)
def update_tipo(id: int, data: TipoAnestesiaCreate, db: Session = Depends(get_db)):
    tipo = db.query(TipoAnestesia).filter(TipoAnestesia.idtipoanestecia == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de anestesia no encontrado")
    tipo.nombre = data.nombre
    db.commit()
    db.refresh(tipo)
    return tipo

@app.delete("/tipo-anestesia/{id}")
def delete_tipo(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoAnestesia).filter(TipoAnestesia.idtipoanestecia == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de anestesia no encontrado")
    db.delete(tipo)
    db.commit()
    return {"message": "Tipo de anestesia eliminado correctamente"}


# ---------------------------
# CRUD: Anestesia
# ---------------------------

@app.post("/anestesia", response_model=AnestesiaResponse)
def create_anestesia(data: AnestesiaCreate, db: Session = Depends(get_db)):
    tipo = db.query(TipoAnestesia).filter(TipoAnestesia.idtipoanestecia == data.tipo_anestesia).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de anestesia no encontrado")

    nueva = Anestesia(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@app.get("/anestesia/", response_model=List[AnestesiaResponse])
def get_anestesias(db: Session = Depends(get_db)):
    return db.query(Anestesia).all()

@app.get("/anestesia/{id}", response_model=AnestesiaResponse)
def get_anestesia(id: int, db: Session = Depends(get_db)):
    anestesia = db.query(Anestesia).filter(Anestesia.idanestecia == id).first()
    if not anestesia:
        raise HTTPException(status_code=404, detail="Anestesia no encontrada")
    return anestesia

@app.put("/anestesia/{id}", response_model=AnestesiaResponse)
def update_anestesia(id: int, data: AnestesiaCreate, db: Session = Depends(get_db)):
    anestesia = db.query(Anestesia).filter(Anestesia.idanestecia == id).first()
    if not anestesia:
        raise HTTPException(status_code=404, detail="Anestesia no encontrada")

    for key, value in data.dict().items():
        setattr(anestesia, key, value)
    db.commit()
    db.refresh(anestesia)
    return anestesia

@app.delete("/anestesia/{id}")
def delete_anestesia(id: int, db: Session = Depends(get_db)):
    anestesia = db.query(Anestesia).filter(Anestesia.idanestecia == id).first()
    if not anestesia:
        raise HTTPException(status_code=404, detail="Anestesia no encontrada")
    db.delete(anestesia)
    db.commit()
    return {"message": "Anestesia eliminada correctamente"}
# ---------------------------
#medicamentos
# ---------------------------
@app.post("/medicamentos", response_model=MedicamentosResponse)
def create_medicamentos(data: MedicamentosCreate, db: Session = Depends(get_db)):
    nuevo = Medicamentos(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
@app.get("/medicamentos/", response_model=List[MedicamentosResponse])
def get_medicamentos(db: Session = Depends(get_db)):
    return db.query(Medicamentos).all()
@app.get("/medicamentos/{id}", response_model=MedicamentosResponse)
def get_medicamento(id: int, db: Session = Depends(get_db)):
    medicamento = db.query(Medicamentos).filter(Medicamentos.idmedicamento == id).first()
    if not medicamento:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    return medicamento
@app.put("/medicamentos/{id}", response_model=MedicamentosResponse)
def update_medicamento(id: int, data: MedicamentosCreate, db: Session = Depends(get_db)):
    medicamento = db.query(Medicamentos).filter(Medicamentos.idmedicamento == id).first()
    if not medicamento:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    medicamento.nombremedicamento = data.nombremedicamento
    medicamento.precio = data.precio
    db.commit()
    db.refresh(medicamento)
    return medicamento
@app.delete("/medicamentos/{id}")
def delete_medicamento(id: int, db: Session = Depends(get_db)):
    medicamento = db.query(Medicamentos).filter(Medicamentos.idmedicamento == id).first()
    if not medicamento:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    db.delete(medicamento)
    db.commit()
    return {"message": "Medicamento eliminado correctamente"}
# ---------------------------
#insumos
# ---------------------------
@app.post("/insumos", response_model=InsumosResponse)
def create_insumos(data: InsumosCreate, db: Session = Depends(get_db)):
    nuevo = Insumos(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
#get insumos
@app.get("/insumos/", response_model=List[InsumosResponse])
def get_insumos(db: Session = Depends(get_db)):
    return db.query(Insumos).all()
@app.get("/insumos/{id}", response_model=InsumosResponse)
def get_insumo(id: int, db: Session = Depends(get_db)):
    insumo = db.query(Insumos).filter(Insumos.idinsumos == id).first()
    if not insumo:
        raise HTTPException(status_code=404, detail="Insumo no encontrado")
    return insumo
@app.put("/insumos/{id}", response_model=InsumosResponse)
def update_insumo(id: int, data: InsumosCreate, db: Session = Depends
(get_db)):
    insumo = db.query(Insumos).filter(Insumos.idinsumo == id).first()
    if not insumo:
        raise HTTPException(status_code=404, detail="Insumo no encontrado")
    insumo.nombreinsumo = data.nombreinsumo
    insumo.precio = data.precio
    db.commit()
    db.refresh(insumo)
    return insumo
@app.delete("/insumos/{id}")
def delete_insumo(id: int, db: Session = Depends(get_db)):
    insumo = db.query(Insumos).filter(Insumos.idinsumo == id).first()
    if not insumo:
        raise HTTPException(status_code=404, detail="Insumo no encontrado")
    db.delete(insumo)
    db.commit()
    return {"message": "Insumo eliminado correctamente"}
# ---------------------------
#equipos
# ---------------------------
@app.post("/equipos", response_model=EquiposResponse)
def create_equipos(data: EquiposCreate, db: Session = Depends(get_db)):
    nuevo = Equipos(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
#get equipos
@app.get("/equipos/", response_model=List[EquiposResponse])
def get_equipos(db: Session = Depends(get_db)):
    return db.query(Equipos).all()
@app.get("/equipos/{id}", response_model=EquiposResponse)
def get_equipo(id: int, db: Session = Depends(get_db)):
    equipo = db.query(Equipos).filter(Equipos.idequipo == id).first()
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return equipo
@app.put("/equipos/{id}", response_model=EquiposResponse)
def update_equipo(id: int, data: EquiposCreate, db: Session = Depends
(get_db)):
    equipo = db.query(Equipos).filter(Equipos.idequipo == id).first()
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    equipo.nombreequipo = data.nombreequipo
    equipo.precio = data.precio
    db.commit()
    db.refresh(equipo)
    return equipo
@app.delete("/equipos/{id}")
def delete_equipo(id: int, db: Session = Depends(get_db)):
    equipo = db.query(Equipos).filter(Equipos.idequipo == id).first()
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    db.delete(equipo)
    db.commit()
    return {"message": "Equipo eliminado correctamente"}
# ---------------------------
#tipo cirugia
# ---------------------------
@app.post("/tipo-cirugia", response_model=TipoCirugiaResponse)
def create_tipo_cirugia(data: TipoCirugiaCreate, db: Session = Depends(get_db)):
    nuevo = TipoCirugia(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
#get tipo cirugia
@app.get("/tipo-cirugia/", response_model=List[TipoCirugiaResponse])
def get_tipos_cirugia(db: Session = Depends(get_db)):
    return db.query(TipoCirugia).all()

@app.get("/tipo-cirugia/{id}", response_model=TipoCirugiaResponse)
def get_tipo_cirugia(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoCirugia).filter(TipoCirugia.id_tipo_cirugia == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de cirugia no encontrado")
    return tipo
@app.put("/tipo-cirugia/{id}", response_model=TipoCirugiaResponse)
def update_tipo_cirugia(id: int, data: TipoCirugiaCreate, db: Session = Depends
(get_db)):
    tipo = db.query(TipoCirugia).filter(TipoCirugia.id_tipo_cirugia == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de cirugia no encontrado")
    tipo.nombrecirugia = data.nombrecirugia
    db.commit()
    db.refresh(tipo)
    return tipo
@app.delete("/tipo-cirugia/{id}")
def delete_tipo_cirugia(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoCirugia).filter(TipoCirugia.id_tipo_cirugia == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de cirugia no encontrado")
    db.delete(tipo)
    db.commit()
    return {"message": "Tipo de cirugia eliminado correctamente"}
# ---------------------------
#cirugia
# ---------------------------
@app.post("/cirugia", response_model=CirugiaResponse)
def create_cirugia(data: CirugiaCreate, db: Session = Depends(get_db)):
    # Verificar que los IDs foráneos existen
    insumo = db.query(Insumos).filter(Insumos.idinsumo == data.id_insumo).first()
    equipo = db.query(Equipos).filter(Equipos.idequipo == data.id_equipo).first()
    medicamento = db.query(Medicamentos).filter(Medicamentos.idmedicamento == data.idmedicamentos).first()
    anestesia = db.query(Anestesia).filter(Anestesia.idanestecia == data.id_anestesia).first()
    tipo_cirugia = db.query(TipoCirugia).filter(TipoCirugia.id_tipo_cirugia == data.id_tipo_cirugia).first()

    if not insumo or not equipo or not medicamento or not anestesia or not tipo_cirugia:
        raise HTTPException(status_code=404, detail="Uno o más IDs foráneos no encontrados")

    nueva = Cirugia(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva
@app.get("/cirugia/", response_model=List[CirugiaResponse])
def get_cirugias(db: Session = Depends(get_db)):
    return db.query(Cirugia).all()


@app.get("/cirugia/{id}", response_model=CirugiaResponse)
def get_cirugia(id: int, db: Session = Depends(get_db)):
    cirugia = db.query(Cirugia).filter(Cirugia.id_cirugia == id).first()
    if not cirugia:
        raise HTTPException(status_code=404, detail="Cirugia no encontrada")
    return cirugia
@app.put("/cirugia/{id}", response_model=CirugiaResponse)
def update_cirugia(id: int, data: CirugiaCreate, db: Session = Depends(get_db)):
    cirugia = db.query(Cirugia).filter(Cirugia.id_cirugia == id).first()
    if not cirugia:
        raise HTTPException(status_code=404, detail="Cirugia no encontrada")

    # Verificar que los IDs foráneos existen
    insumo = db.query(Insumos).filter(Insumos.idinsumo == data.id_insumo).first()
    equipo = db.query(Equipos).filter(Equipos.idequipo == data.id_equipo).first()
    medicamento = db.query(Medicamentos).filter(Medicamentos.idmedicamento == data.idmedicamentos).first()
    anestesia = db.query(Anestesia).filter(Anestesia.idanestecia == data.id_anestesia).first()
    tipo_cirugia = db.query(TipoCirugia).filter(TipoCirugia.id_tipo_cirugia == data.id_tipo_cirugia).first()

    if not insumo or not equipo or not medicamento or not anestesia or not tipo_cirugia:
        raise HTTPException(status_code=404, detail="Uno o más IDs foráneos no encontrados")

    for key, value in data.dict().items():
        setattr(cirugia, key, value)
    db.commit()
    db.refresh(cirugia)
    return cirugia
@app.delete("/cirugia/{id}")
def delete_cirugia(id: int, db: Session = Depends(get_db)):
    cirugia = db.query(Cirugia).filter(Cirugia.id_cirugia == id).first()
    if not cirugia:
        raise HTTPException(status_code=404, detail="Cirugia no encontrada")
    db.delete(cirugia)
    db.commit()
    return {"message": "Cirugia eliminada correctamente"}
# ---------------------------
# Fin del CRUD
