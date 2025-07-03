import os

def creer_repertoires(principal, sous_repertoires):
    if not os.path.exists(principal):
        os.mkdir(principal)
    for nom in sous_repertoires:
        chemin = os.path.join(principal, nom)
        if not os.path.exists(chemin):
            os.mkdir(chemin)

repertoire_principal = 'challenges3/challenge4/fichier'
sous_repertoires = ['sous-répertoires-1', 'sous-répertoires-2', 'sous-répertoires-3']
creer_repertoires(repertoire_principal, sous_repertoires)
