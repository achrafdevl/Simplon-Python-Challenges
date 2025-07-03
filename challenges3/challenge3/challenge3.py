import os
import shutil

def copier_fichiers_csv(repertoire_source, repertoire_destination):
    for fichier in os.listdir(repertoire_source):
        if fichier.endswith('.csv'):
            shutil.copy(os.path.join(repertoire_source, fichier), repertoire_destination)



repertoire_source = 'challenges3/challenge3/fichiers'
repertoire_destination = 'challenges3/challenge3/fichier2'
copier_fichiers_csv(repertoire_source, repertoire_destination)
