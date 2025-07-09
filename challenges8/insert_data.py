from database import Session
from models import *

from datetime import datetime

def clear_database():
    """Clear all data from the database"""
    session = Session()
    try:
        session.query(CommandePlat).delete()
        session.query(Commande).delete()
        session.query(Plat).delete()
        session.query(Client).delete()
        session.query(Categorie).delete()
        session.commit()
        print("Database cleared successfully")
    except Exception as e:
        session.rollback()
        print(f"Error clearing database: {e}")
    finally:
        session.close()

def insert_data():
    clear_database()
    
    session = Session()

   
    categories = [
        Categorie(id=1, nom='Entrée'),
        Categorie(id=2, nom='Plat principal'),
        Categorie(id=3, nom='Dessert'),
        Categorie(id=4, nom='Boisson')
    ]
    session.add_all(categories)

    
    plats = [
        Plat(id=1, nom="Salade César", prix=45, description="Salade avec poulet", categorie_id=1),
        Plat(id=2, nom="Soupe de légumes", prix=30, description="Soupe chaude de saison", categorie_id=1),
        Plat(id=3, nom="Steak frites", prix=90, description="Viande grillée et frites", categorie_id=2),
        Plat(id=4, nom="Pizza Margherita", prix=70, description="Pizza tomate & mozzarella", categorie_id=2),
        Plat(id=5, nom="Tiramisu", prix=35, description="Dessert italien", categorie_id=3),
        Plat(id=6, nom="Glace 2 boules", prix=25, description="Glace au choix", categorie_id=3),
        Plat(id=7, nom="Coca-Cola", prix=15, description="Boisson gazeuse", categorie_id=4),
        Plat(id=8, nom="Eau minérale", prix=10, description="Eau plate ou gazeuse", categorie_id=4),
    ]
    session.add_all(plats)

    
    clients = [
        Client(id=1, nom="Amine Lahmidi", email="amine@example.com"),
        Client(id=2, nom="Sara Benali", email="sara.b@example.com"),
        Client(id=3, nom="Youssef El Khalfi", email="youssef.k@example.com")
    ]
    session.add_all(clients)

   
    commandes = [
        Commande(id=1, client_id=1, date_commande=datetime(2025, 7, 7, 12, 30), total=120),
        Commande(id=2, client_id=2, date_commande=datetime(2025, 7, 7, 13, 0), total=85),
        Commande(id=3, client_id=1, date_commande=datetime(2025, 7, 8, 19, 45), total=150)
    ]
    session.add_all(commandes)

    
    commande_plats = [
        CommandePlat(commande_id=1, plat_id=1, quantite=1),
        CommandePlat(commande_id=1, plat_id=3, quantite=1),
        CommandePlat(commande_id=1, plat_id=7, quantite=2),
        CommandePlat(commande_id=2, plat_id=2, quantite=1),
        CommandePlat(commande_id=2, plat_id=4, quantite=1),
        CommandePlat(commande_id=2, plat_id=8, quantite=1),
        CommandePlat(commande_id=3, plat_id=3, quantite=1),
        CommandePlat(commande_id=3, plat_id=5, quantite=1),
        CommandePlat(commande_id=3, plat_id=7, quantite=1),
    ]
    session.add_all(commande_plats)

    session.commit()
    session.close()
