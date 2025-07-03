# Classe de base
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def afficher_infos(self):
        print("Nom :", self.nom)
        print("Prénom :", self.prenom)
        print("Âge :", self.age)

# Étudiant hérite de Personne
class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule
        self.notes = []

    def ajouter_note(self, note):
        self.notes.append(note)

    def moyenne(self):
        if len(self.notes) > 0:
            return sum(self.notes) / len(self.notes)
        return 0

    def afficher_infos(self):
        super().afficher_infos()
        print("Matricule :", self.matricule)
        print("Moyenne :", self.moyenne())

# Enseignant hérite de Personne
class Enseignant(Personne):
    def __init__(self, nom, prenom, age, specialite, salaire):
        super().__init__(nom, prenom, age)
        self.specialite = specialite
        self.salaire = salaire

    def afficher_infos(self):
        super().afficher_infos()
        print("Spécialité :", self.specialite)
        print("Salaire :", self.salaire)

# Classe École
class Ecole:
    def __init__(self, nom):
        self.nom = nom
        self.etudiants = []
        self.enseignants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def ajouter_enseignant(self, enseignant):
        self.enseignants.append(enseignant)

    def afficher_membres(self):
        print("******* Étudiants *******")
        for e in self.etudiants:
            e.afficher_infos()
            

        print("******* Enseignants *******")
        for ens in self.enseignants:
            ens.afficher_infos()
            

# Exemple
e1 = Etudiant("Chair", "Achraf", 24, "123")
e1.ajouter_note(18)

ens1 = Enseignant("hamid", "hamif", 35, "data analysis", 4000)

ecole = Ecole("Simplon academy")
ecole.ajouter_etudiant(e1)
ecole.ajouter_enseignant(ens1)
ecole.afficher_membres()
