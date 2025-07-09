from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Categorie(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)

    plats = relationship("Plat", back_populates="categorie")

class Plat(Base):
    __tablename__ = 'plats'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    prix = Column(Float, nullable=False)
    description = Column(String)
    categorie_id = Column(Integer, ForeignKey('categories.id'))

    categorie = relationship("Categorie", back_populates="plats")
    commande_plats = relationship("CommandePlat", back_populates="plat")

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    email = Column(String, nullable=False)

    commandes = relationship("Commande", back_populates="client")

class Commande(Base):
    __tablename__ = 'commandes'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    date_commande = Column(DateTime)
    total = Column(Float)

    client = relationship("Client", back_populates="commandes")
    plats = relationship("CommandePlat", back_populates="commande")

class CommandePlat(Base):
    __tablename__ = 'commande_plats'
    commande_id = Column(Integer, ForeignKey('commandes.id'), primary_key=True)
    plat_id = Column(Integer, ForeignKey('plats.id'), primary_key=True)
    quantite = Column(Integer)

    commande = relationship("Commande", back_populates="plats")
    plat = relationship("Plat", back_populates="commande_plats")
