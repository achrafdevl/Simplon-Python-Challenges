from sqlalchemy import func, and_, desc, select
from models import *
from database import Session
from datetime import datetime

def requetes():
    session = Session()

    print("***** Plats triés par prix décroissant :")
    for plat in session.query(Plat).order_by(Plat.prix.desc()).all():
        print(plat.nom, plat.prix)

    print("***** Plats dont le prix est entre 30 et 80 :")
    for plat in session.query(Plat).filter(Plat.prix.between(30, 80)).all():
        print(plat.nom, plat.prix)

    print("***** Clients dont le nom commence par 'S' :")
    for client in session.query(Client).filter(Client.nom.ilike('S%')).all():
        print(client.nom)

    print("***** Plats avec leur nom de catégorie :")
    for plat in session.query(Plat).join(Categorie).all():
        print(plat.nom, "->", plat.categorie.nom)

    print("***** Commandes avec nom du client et date :")
    for commande in session.query(Commande).join(Client).all():
        print(commande.id, commande.client.nom, commande.date_commande)

    print("***** Pour chaque commande, plats commandés avec quantité :")
    for cp in session.query(CommandePlat).join(Plat).join(Commande).all():
        print(f"Commande {cp.commande_id} - {cp.plat.nom} x{cp.quantite}")

    print("***** Nombre de plats par catégorie :")
    for row in session.query(Categorie.nom, func.count(Plat.id)).join(Plat).group_by(Categorie.nom).all():
        print(row)

    print("***** Prix moyen des plats par catégorie :")
    for row in session.query(Categorie.nom, func.avg(Plat.prix)).join(Plat).group_by(Categorie.nom).all():
        print(row)

    print("***** Nombre de commandes par client :")
    for row in session.query(Client.nom, func.count(Commande.id)).join(Commande).group_by(Client.nom).all():
        print(row)

    print("*****  Clients ayant passé plus d'une commande :")
    for row in session.query(Client.nom).join(Commande).group_by(Client.nom).having(func.count(Commande.id) > 1).all():
        print(row)

    print("*****  Plats commandés plus de 2 fois (total quantités) :")
    for row in session.query(Plat.nom, func.sum(CommandePlat.quantite)).join(CommandePlat).group_by(Plat.nom).having(func.sum(CommandePlat.quantite) > 2).all():
        print(row)

    print("*****  Commandes du mois de juillet 2025 :")
    for commande in session.query(Commande).filter(
        func.date_trunc('month', Commande.date_commande) == datetime(2025, 7, 1)
    ).all():
        print(commande.id, commande.date_commande)

    

    session.close()
