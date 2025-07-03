class CompteBancaire:
    def __init__(self, nom):
        self.nom = nom
        self.solde = 0.0

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
        else:
            print("Solde insuffisants.")

    def afficher_solde(self):
        print("Nom :", self.nom)
        print("Solde :", self.solde, "MAD")


# Exemple
compte1 = CompteBancaire("Yasmine")
compte1.deposer(100)
compte1.retirer(30)
compte1.afficher_solde()
