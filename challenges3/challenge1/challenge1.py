import os

def combiner_fichiers_textes(repertoire):
    contenu_combine = ""
    for fichier in os.listdir(repertoire):
        if fichier.endswith('.txt'):
            with open(os.path.join(repertoire, fichier), 'r') as f:
                contenu_combine += f.read() + "\n"
    return contenu_combine

repertoire = 'challenges3/challenge1/fichier'
texte_combine = combiner_fichiers_textes(repertoire)
print(texte_combine)
