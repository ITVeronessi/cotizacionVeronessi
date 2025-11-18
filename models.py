from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# ========================
# Tipo de Anestesia
# ========================
class TipoAnestesia(Base):
    __tablename__ = "tipo_anestesia"

    idtipoanestecia = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)

    # Relación opcional con Anestesia
    anestesias = relationship("Anestesia", back_populates="tipo", lazy="joined")


# ========================
# Anestesia
# ========================
class Anestesia(Base):
    __tablename__ = "anestesia"

    idanestecia = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    tipo_anestesia = Column(Integer, ForeignKey("tipo_anestesia.idtipoanestecia"))
    precio = Column(Numeric(10, 2), nullable=False)

    # Relación con TipoAnestesia
    tipo = relationship("TipoAnestesia", back_populates="anestesias", lazy="joined")


# ========================
# Medicamentos
# ========================
class Medicamentos(Base):
    __tablename__ = "medicamentos"

    idmedicamentos = Column(Integer, primary_key=True, index=True)
    nombremedicamento = Column(String(120), nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)


# ========================
# Insumos
# ========================
class Insumos(Base):
    __tablename__ = "insumos"

    idinsumos = Column(Integer, primary_key=True, index=True)
    nombreinsumo = Column(String(120), nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)


# ========================
# Equipos
# ========================
class Equipos(Base):
    __tablename__ = "equipos"

    idequipos = Column(Integer, primary_key=True, index=True)
    nombreequipo = Column(String(120), nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)


# ========================
# Tipo de Cirugia
# ========================
class TipoCirugia(Base):
    __tablename__ = "tipo_cirugia"

    id_tipo_cirugia = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)

    # Relación opcional con Cirugia
    cirugias = relationship("Cirugia", back_populates="tipo_cirugia", lazy="joined")


# ========================
# Cirugia
# ========================
class Cirugia(Base):
    __tablename__ = "cirugia"

    id_cirugia = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)
    id_tipo_cirugia = Column(Integer, ForeignKey("tipo_cirugia.id_tipo_cirugia"), nullable=True)

    # Relación opcional con TipoCirugia
    tipo_cirugia = relationship("TipoCirugia", back_populates="cirugias", lazy="joined")
