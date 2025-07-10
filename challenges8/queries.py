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

    print("*****  Commande la plus récente (avec client) :")
    latest = session.query(Commande).order_by(Commande.date_commande.desc()).first()
    print(latest.id, latest.client.nom, latest.date_commande)

    print("*****  Clients avec commande > 100 :")
    for row in session.query(Client.nom).join(Commande).filter(Commande.total > 100).distinct().all():
        print(row)

    print("*****  Plats plus chers que la moyenne des plats :")
    avg_price = session.query(func.avg(Plat.prix)).scalar()
    for plat in session.query(Plat).filter(Plat.prix > avg_price).all():
        print(plat.nom, plat.prix)

    print("*****  Mise à jour du prix de la Pizza Margherita à 75 :")
    pizza = session.query(Plat).filter(Plat.nom == "Pizza Margherita").first()
    if pizza:
        pizza.prix = 75
        session.commit()
        print("Prix mis à jour.")

    print("*****  Ajouter un nouveau plat dans la catégorie 'Boisson' :")
    boisson_cat = session.query(Categorie).filter(Categorie.nom == "Boisson").first()
    nouveau_plat = Plat(nom="Thé à la menthe", prix=20, description="Thé marocain", categorie_id=boisson_cat.id)
    session.add(nouveau_plat)
    session.commit()
    print("Nouveau plat ajouté.")

    print("*****  Supprimer client 'Youssef El Khalfi' et ses commandes :")
    client = session.query(Client).filter(Client.nom == "Youssef El Khalfi").first()
    if client:
        for cmd in client.commandes:
            session.query(CommandePlat).filter(CommandePlat.commande_id == cmd.id).delete()
        session.query(Commande).filter(Commande.client_id == client.id).delete()
        session.delete(client)
        session.commit()
        print("Client et ses commandes supprimés.")

    print("*****  Pour chaque client : nom, total plats commandés, total dépensé :")
    for client in session.query(Client).all():
        total_plats = session.query(func.sum(CommandePlat.quantite))\
            .join(Commande).filter(Commande.client_id == client.id).scalar() or 0
        total_depense = session.query(func.sum(Commande.total))\
            .filter(Commande.client_id == client.id).scalar() or 0
        print(client.nom, "- Plats commandés :", total_plats, "- Total dépensé :", total_depense)

    print("*****  Top 3 plats les plus commandés :")
    for row in session.query(Plat.nom, func.sum(CommandePlat.quantite).label('total'))\
        .join(CommandePlat).group_by(Plat.nom).order_by(desc('total')).limit(3).all():
        print(row)

    print("*****  Clients et leur dernière commande :")
    for client in session.query(Client).all():
        last_cmd = session.query(Commande)\
            .filter(Commande.client_id == client.id)\
            .order_by(Commande.date_commande.desc()).first()
        if last_cmd:
            print(client.nom, last_cmd.date_commande)

    print("*****  Vue virtuelle : nom du client, plats commandés, quantités, date de commande :")
    results = session.query(Client.nom, Plat.nom, CommandePlat.quantite, Commande.date_commande)\
        .join(Commande).join(CommandePlat).join(Plat).all()
    for row in results:
        print(row)

    session.close()
