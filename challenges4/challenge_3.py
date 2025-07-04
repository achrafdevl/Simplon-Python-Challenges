import numpy as np

Comparaison1 =np.array([15, 20, 18, 17, 46, 14])
Comparaison2 =np.array([15, 25, 13, 17, 12, 14])

Comparaison = np.where(Comparaison1 != Comparaison2)


print(Comparaison)
print(Comparaison1[Comparaison])
print(Comparaison2[Comparaison])
