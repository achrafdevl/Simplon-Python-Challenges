import numpy as np

Conditions = np.array([10,51,10,3,7,8,12])

seuil = 12

Con_seuil = np.where(Conditions > seuil)

print(Con_seuil)

nouveau_array= Conditions[Con_seuil]
print(nouveau_array)