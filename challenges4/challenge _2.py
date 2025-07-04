import numpy as np

Normalisation = np.array([10, 20, 30, 40, 50])


moyenne = np.mean(Normalisation)
media = np.median(Normalisation)
std = np.std(Normalisation)

result = (Normalisation- moyenne)/std
print(result)


