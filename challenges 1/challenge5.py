etudiant_info = ("Yasmine", 22, "Informatique", 17.4)

print("Prénom :", etudiant_info[0])
print("Âge :", etudiant_info[1])
print("Filière :", etudiant_info[2])
print("Moyenne générale :", etudiant_info[3])

try:
    etudiant_info[2] = "Mathématiques"
except TypeError as e:
    print("\nErreur :", e)
    print("Explication : Les tuples sont **immutables**, ce qui veut dire qu'on ne peut pas changer leurs valeurs après leur création.")

print("\nAffichage avec slicing (prénom et âge) :", etudiant_info[0:2])

infos_supplementaires = ("Très Bien", 2024)

etudiant_complet = etudiant_info + infos_supplementaires

print("\nTuple final combiné :", etudiant_complet)
