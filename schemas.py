from pydantic import BaseModel
from typing import Optional

# ========================
# Tipo de Anestesia
# ========================
class TipoAnestesiaBase(BaseModel):
    nombre: str

class TipoAnestesiaCreate(TipoAnestesiaBase):
    pass

class TipoAnestesiaResponse(TipoAnestesiaBase):
    idtipoanestecia: int

    class Config:
        orm_mode = True


# ========================
# Anestesia
# ========================
class AnestesiaBase(BaseModel):
    nombre: str
    tipo_anestesia: int
    precio: float

class AnestesiaCreate(AnestesiaBase):
    pass

class AnestesiaResponse(AnestesiaBase):
    idanestecia: int
    tipo: Optional[TipoAnestesiaResponse]  # Relación opcional

    class Config:
        orm_mode = True


# ========================
# Medicamentos
# ========================
class MedicamentosBase(BaseModel):
    nombremedicamento: str
    precio: float

class MedicamentosCreate(MedicamentosBase):
    pass

class MedicamentosResponse(MedicamentosBase):
    idmedicamentos: int

    class Config:
        orm_mode = True


# ========================
# Insumos
# ========================
class InsumosBase(BaseModel):
    nombreinsumo: str
    precio: float

class InsumosCreate(InsumosBase):
    pass

class InsumosResponse(InsumosBase):
    idinsumos: int

    class Config:
        orm_mode = True


# ========================
# Equipos
# ========================
class EquiposBase(BaseModel):
    nombreequipo: str
    precio: float

class EquiposCreate(EquiposBase):
    pass

class EquiposResponse(EquiposBase):
    idequipos: int

    class Config:
        orm_mode = True


# ========================
# Tipo de Cirugia
# ========================
class TipoCirugiaBase(BaseModel):
    nombre: str

class TipoCirugiaCreate(TipoCirugiaBase):
    pass

class TipoCirugiaResponse(TipoCirugiaBase):
    id_tipo_cirugia: int

    class Config:
        orm_mode = True


# ========================
# Cirugia
# ========================
class CirugiaBase(BaseModel):
    nombre: str
    precio: float
    id_tipo_cirugia: Optional[int] = None  # Opcional

class CirugiaCreate(CirugiaBase):
    pass

class CirugiaResponse(CirugiaBase):
    id_cirugia: int
    tipo_cirugia: Optional[TipoCirugiaResponse]  # Relación opcional

    class Config:
        orm_mode = True
