from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class TipoAnestesia(Base):
    __tablename__ = "tipo_anestesia"
    idtipoanestecia = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)

    # Relación con anestesia
    anestesias = relationship("Anestesia", back_populates="tipo")


class Anestesia(Base):
    __tablename__ = "anestesia"

    idanestecia = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    tipo_anestesia = Column(Integer, ForeignKey("tipo_anestesia.idtipoanestecia"))
    precio = Column(Numeric(10, 2), nullable=False)

    # Relación con tipo
    tipo = relationship("TipoAnestesia", back_populates="anestesias")
class Medicamentos(Base):
    __tablename__ = "medicamentos"
    idmedicamentos= Column(Integer, primary_key=True, index=True)
    nombremedicamento= Column(String(120), nullable=False)
    precio= Column(Numeric(10,2), nullable=False)
# Insumos idmedicamentos
class Insumos(Base):
    __tablename__ = "insumos"
    idinsumos= Column(Integer, primary_key=True, index=True)
    nombreinsumo= Column(String(120), nullable=False)
    precio= Column(Numeric(10,2), nullable=False)

#equipos
class Equipos(Base):
    __tablename__ = "equipos"
    idequipos= Column(Integer, primary_key=True, index=True)
    nombreequipo= Column(String(120), nullable=False)
    precio= Column(Numeric(10,2), nullable=False)
#tipo cirugia
class TipoCirugia(Base):
    __tablename__ = "tipo_cirugia"
    id_tipo_cirugia= Column(Integer, primary_key=True, index=True)
    nombrecirugia= Column(String(120), nullable=False)

#cirugia
class Cirugia(Base):
    __tablename__ = "cirugia"
    id_cirugia= Column(Integer, primary_key=True, index=True)
    nombre= Column(String(120), nullable=False)
    id_insumo= Column(Integer, ForeignKey("insumos.idinsumos"))
    id_equipo= Column(Integer, ForeignKey("equipos.idequipos"))
    idmedicamentos= Column(Integer, ForeignKey("medicamentos.idmedicamentos"))
    id_anestesia= Column(Integer, ForeignKey("anestesia.idanestecia"))
    id_tipo_cirugia= Column(Integer, ForeignKey("tipo_cirugia.id_tipo_cirugia"))
    precio= Column(Numeric(10,2), nullable=False)
    # Relaciones
    insumo = relationship("Insumos")
    equipo = relationship("Equipos")   
    medicamento = relationship("Medicamentos")
    anestesia = relationship("Anestesia")
    tipo_cirugia = relationship("TipoCirugia")
    

    
